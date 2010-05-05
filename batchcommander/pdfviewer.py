#!/usr/bin/env python

from PyQt4 import QtCore, QtGui
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

class PdfViewerWidget(QtGui.QWidget):
    def __init__(self, *args, **kwargs):
        self.doc = None
        QtGui.QWidget.__init__(self, *args, **kwargs)
        self.setWindowTitle("PDF Viewer")
        self.isBlanked = False
        p = QtGui.QPalette()
        p.setColor(QtGui.QPalette.Background, QtCore.Qt.black);
        self.setPalette(p)
        self.setGeometry(QtGui.QApplication.desktop().screenGeometry())
        # self.hide() 

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Down:
            self.nextPage()
        elif event.key() == QtCore.Qt.Key_Up:
            self.previousPage()
        elif event.key() == QtCore.Qt.Key_Escape:
            self.stop()

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
        print self.size()

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
        if self.pdfImages[idx] is not None:
            return
        page = self.doc.page(idx)
        ratio = 1.0 * self.frameSize().width() / page.pageSize().width()
        yratio = 1.0 * self.frameSize().height() / page.pageSize().height()
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
    
class PdfViewerWindow:
    def __init__(self, filename):
        self.main_window = QtGui.QMainWindow()
        self.setupUi(self.main_window)
        self.pdfViewer.load(filename)
        self.main_window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(333, 541)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pdfViewer = PdfViewerWidget(self.centralwidget)
        self.pdfViewer.setObjectName("pdfViewer")
        self.verticalLayout.addWidget(self.pdfViewer)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/go-previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionPrevious_Page.setIcon(icon)
        self.actionPrevious_Page.setObjectName("actionPrevious_Page")
        self.actionNext_Page = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../assets/go-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("../assets/go-previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionNext_Page.setIcon(icon1)
        self.actionNext_Page.setObjectName("actionNext_Page")
        self.actionFirst_Page = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../assets/go-first.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFirst_Page.setIcon(icon2)
        self.actionFirst_Page.setObjectName("actionFirst_Page")
        self.actionLast_Page = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../code/batchcommander/assets/go-last.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionLast_Page.setIcon(icon3)
        self.actionLast_Page.setObjectName("actionLast_Page")
        self.toolBar.addAction(self.actionFirst_Page)
        self.toolBar.addAction(self.actionPrevious_Page)
        self.toolBar.addAction(self.actionNext_Page)
        self.toolBar.addAction(self.actionLast_Page)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
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


