#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
import sys, os
import QtPoppler

'''
PDF Viewer code taken from OpenLP by Raoul Snyman and others.

###############################################################################
# OpenLP - Open Source Lyrics Projection                                      #
# --------------------------------------------------------------------------- #
# Copyright (c) 2008-2009 Raoul Snyman                                        #
# Portions copyright (c) 2008-2009 Martin Thompson, Tim Bentley, Carsten      #
# Tinggaard, Jon Tibble, Jonathan Corwin, Maikel Stuivenberg, Scott Guerrieri #
# --------------------------------------------------------------------------- #
# This program is free software; you can redistribute it and/or modify it     #
# under the terms of the GNU General Public License as published by the Free  #
# Software Foundation; version 2 of the License.                              #
#                                                                             #
# This program is distributed in the hope that it will be useful, but WITHOUT #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or       #
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for    #
# more details.                                                               #
#                                                                             #
# You should have received a copy of the GNU General Public License along     #
# with this program; if not, write to the Free Software Foundation, Inc., 59  #
# Temple Place, Suite 330, Boston, MA 02111-1307 USA                          #
###############################################################################

'''


if sys.platform == 'darwin':
    ICON_LOCATION_ROOT = '../assets'
else:
    ICON_LOCATION_ROOT = os.path.expanduser('~/.batchcommander/assets')

class PdfViewerWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        self.doc = None
        QtGui.QWidget.__init__(self, *args, **kwargs)
        self.setWindowTitle("PDF Viewer")
        self.isBlanked = False
        self.scale = 1.
        p = QtGui.QPalette()
        p.setColor(QtGui.QPalette.Background, QtCore.Qt.black);
        self.setPalette(p)
        self.setGeometry(QtGui.QApplication.desktop().screenGeometry())
        # self.hide() 

    '''
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Down:
            self.nextPage()
        elif event.key() == QtCore.Qt.Key_Up:
            self.previousPage()
        elif event.key() == QtCore.Qt.Key_Escape:
            self.stop()
    '''

    def paintEvent(self, event):
        if self.isBlanked:
            return
        img = self.getImage(self.currentPage)
        if img is None:
            return
        x = (self.frameSize().width() - img.width()) / 2
        y = (self.frameSize().height() - img.height()) / 2
        painter = QtGui.QPainter(self)
        painter.drawImage(x, y, img)

    def getCurrentPage(self):
        return self.currentPage + 1

    def getPageCount(self):
        if self.doc is None:    
            return 0
        else:
            return self.doc.numPages()

    def load(self, filename):
        self.doc = QtPoppler.Poppler.Document.load(filename)
        self.doc.setRenderHint(QtPoppler.Poppler.Document.Antialiasing and QtPoppler.Poppler.Document.TextAntialiasing)
        self.currentPage = 0
        self.pdfImages = [None for i in range(self.doc.numPages())]
        self.cacheImage(self.currentPage)

    def display(self):
        self.update()
        self.cacheImage(self.currentPage + 1)

    def zoom_in(self):
        if self.isBlanked: return
        self.scale += .2
        self.cacheImage(self.pdfImages[self.currentPage])
        self.update()

    def zoom_out(self):
        if self.isBlanked: return
        self.scale -= .2
        self.cacheImage(self.pdfImages[self.currentPage])
        self.update()

    def zoom_original(self):
        if self.isBlanked: return
        self.scale = 1.
        self.cacheImage(self.pdfImages[self.currentPage])
        self.update()

    def start(self):
        self.showFullScreen()
        self.show()

    def stop(self):
        self.hide()

    def close(self):
        self.stop()
        self.pdfImages = None
        self.doc = None
    
    def blank(self):
        self.isBlanked = True
        self.update()

    def unBlank(self):
        self.isBlanked = False
        self.update()

    def nextPage(self):
        if self.currentPage + 1 < self.doc.numPages():
            self.currentPage += 1
            self.display()

    def previousPage(self):
        if self.currentPage > 0:
            self.currentPage -= 1
            self.display()

    def showPage(self, idx):
        if idx < self.doc.numPages():
            self.currentPage = idx
            self.display()

    def cacheImage(self, idx):        
        if idx >= self.doc.numPages():
            return
        # if self.pdfImages[idx] is not None:
        #    return
        page = self.doc.page(idx)
        ratio = self.scale * self.frameSize().width() / page.pageSize().width()
        yratio = self.scale * self.frameSize().height() / page.pageSize().height()
        if yratio < ratio:
            ratio = yratio   
        self.pdfImages[idx] = page.renderToImage(72 * ratio,72 * ratio)
        
   
    def getImage(self, idx):
        self.cacheImage(idx)
        return self.pdfImages[idx]        

    def getThumbnail(self, idx):
        img = None # self.doc.page(idx).thumbnail()
        if img is None:
            img = self.getImage(idx)
        return img

    
class PdfViewerWindow(QtGui.QMainWindow):
    def __init__(self, filename=None, *args, **kwargs):
        super(PdfViewerWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.filename = filename
        if self.filename:
            self.pdfViewer.load(self.filename)
        else:
            self.pdfViewer.blank()
        self.show()

    def load(self, filename):
        if filename == self.filename:
            page = self.pdfViewer.currentPage
        else:
            page = 1
        self.filename = filename
        self.pdfViewer.unBlank()
        self.pdfViewer.load(self.filename)
        self.pdfViewer.showPage(page)

    def reload(self):
        currentpage = self.pdfViewer.currentPage
        self.pdfViewer.load(self.filename)
        self.pdfViewer.showPage(currentpage)

    @QtCore.pyqtSlot()
    def next_page(self):
        self.pdfViewer.nextPage()
    @QtCore.pyqtSlot()
    def previous_page(self):
        self.pdfViewer.previousPage()
    @QtCore.pyqtSlot()
    def first_page(self):
        self.pdfViewer.showPage(0)
    @QtCore.pyqtSlot()
    def last_page(self):
        self.pdfViewer.showPage(self.pdfViewer.doc.numPages() - 1)

    def zoom_in(self):
        self.pdfViewer.zoom_in()
    def zoom_out(self):
        self.pdfViewer.zoom_out()
    def zoom_original(self):
        self.pdfViewer.zoom_original()

    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Plus):
            self.zoom_in()
        elif (event.key() == QtCore.Qt.Key_Minus):
            self.zoom_out()
        else:
            QtGui.QMainWindow.keyPressEvent(self, event)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(333, 541)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pdfViewer = PdfViewerWidget(self.centralwidget)
        self.pdfViewer.setObjectName("pdfViewer")

        self.scrollbox = QtGui.QScrollArea()
        self.scrollbox.setWidget(self.pdfViewer)
        self.scrollbox.setFrameStyle(QtGui.QFrame.NoFrame)
        size = self.scrollbox.maximumViewportSize()
        x = size.width()
        y = size.height()
        self.scrollbox.horizontalScrollBar().setValue(x/2)
        self.scrollbox.verticalScrollBar().setValue(y/2)
        self.verticalLayout.addWidget(self.scrollbox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)

        self.actionPrevious_Page = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("go-previous")
        self.actionPrevious_Page.setIcon(icon)
        self.actionPrevious_Page.setObjectName("actionPrevious_Page")
        self.actionPrevious_Page.triggered.connect(self.previous_page)

        self.actionNext_Page = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("go-next")
        self.actionNext_Page.setIcon(icon)
        self.actionNext_Page.setObjectName("actionNextPage")
        self.actionNext_Page.triggered.connect(self.next_page)

        self.actionFirst_Page = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("go-first")
        self.actionFirst_Page.setIcon(icon)
        self.actionFirst_Page.setObjectName("actionFirst_Page")
        self.actionFirst_Page.triggered.connect(self.first_page)

        self.actionLast_Page = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("go-last")
        self.actionLast_Page.setIcon(icon)
        self.actionLast_Page.setObjectName("actionLast_Page")
        self.actionLast_Page.triggered.connect(self.last_page)

        self.actionZoom_In = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("zoom-in")
        self.actionZoom_In.setIcon(icon)
        self.actionZoom_In.setObjectName("actionZoom_In")
        self.actionZoom_In.triggered.connect(self.zoom_in)

        self.actionZoom_Out = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("zoom-out")
        self.actionZoom_Out.setIcon(icon)
        self.actionZoom_Out.setObjectName("actionZoom_Out")
        self.actionZoom_Out.triggered.connect(self.zoom_out)

        self.actionZoom_Original = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon.fromTheme("zoom-original")
        self.actionZoom_Original.setIcon(icon)
        self.actionZoom_Original.setObjectName("actionZoom_Original")
        self.actionZoom_Original.triggered.connect(self.zoom_original)

        self.toolBar.addAction(self.actionFirst_Page)
        self.toolBar.addAction(self.actionPrevious_Page)
        self.toolBar.addAction(self.actionNext_Page)
        self.toolBar.addAction(self.actionLast_Page)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionZoom_In)
        self.toolBar.addAction(self.actionZoom_Original)
        self.toolBar.addAction(self.actionZoom_Out)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow",
            "Batch Commander", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrevious_Page.setText(QtGui.QApplication.translate("MainWindow", "Previous Page", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNext_Page.setText(QtGui.QApplication.translate("MainWindow", "Next Page", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNext_Page.setToolTip(QtGui.QApplication.translate("MainWindow", "Next Page", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFirst_Page.setText(QtGui.QApplication.translate("MainWindow", "First Page", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLast_Page.setText(QtGui.QApplication.translate("MainWindow", "Last Page", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)

    viewer = PdfViewerWindow(sys.argv[1])

    sys.exit(app.exec_())


