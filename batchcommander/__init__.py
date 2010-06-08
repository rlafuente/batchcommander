#!/usr/bin/env python

# This file is copyright (C) 2009 by Ricardo Lafuente
#
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions are met:
#
#   Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
#   Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
#   The name of the author may not be used to endorse or promote products
#   derived from this software without specific prior written permission.
#
#   THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR IMPLIED
#   WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
#   MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
#   EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#   PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
#   OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
#   WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
#   OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
#   ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''Launch the Batch Commander GUI utility'''

import sys, os
import logging
import shutil
from datetime import datetime
from PyQt4 import QtGui, QtCore

from batchcommander.controls import create_control_from_field
from batchcommander.parser import DataSet
from batchcommander.pdfviewer import PdfViewerWindow
from batchcommander.defaults import *

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("BatchCommander")

class TitleBarWidget(QtGui.QLabel):
    def __init__(self, *args, **kwargs):
        super(TitleBarWidget, self).__init__(*args, **kwargs)
    def mousePressEvent(self, event):
        self.emit(QtCore.SIGNAL('titleClicked(PyQt_PyObject)'), self.parent())

class BatchCommander:
    '''Batch Commander UI runner'''
    def __init__(self,
                 datafiles=None,
                 inputfile=None,
                 scriptfile=None,
                 outputfile=None,
                 command=None,
                 immediate_mode=None,
                 output_mode=MODE_TEX):
        self.datasets = []
        for path in datafiles:
            self.datasets.append(DataSet(path))
        self.inputfile = inputfile
        self.scriptfile = scriptfile
        self.outputfile = outputfile
        self.outputmode = output_mode
        self.is_pdfviewer_open = False
        self.sections = None
        self.immediate_mode = immediate_mode
        self.command = command
        self.process = QtCore.QProcess()
        # self.process.setStandardOutputFile(sys.stdout)
        self.error_log_filename = 'error.log'
        self.output_log_filename = 'output.log'
        self.process.setStandardErrorFile(self.error_log_filename)
        self.process.setStandardOutputFile(self.output_log_filename)

        self.app = QtGui.QApplication(sys.argv)

        self.pdfviewer = PdfViewerWindow()

        # we need this here for now, otherwise it borks
        # this will refer to the combobox in the control window
        self.dataset_selector = None

        # check for PDFTeX before anything else
        self.check_for_tex()


    def show_ui(self):
        self.show_main_window()
        self.show_controls_window()
        # make sure the dirs are set
        self.set_input_file()
        sys.exit(self.app.exec_())

    def show_main_window(self):
        '''Create and display the main interface window.'''
        self.main_window = QtGui.QMainWindow()
        self.main_window.setWindowTitle('Batch Commander: Main')
        self.tab_bar = QtGui.QTabWidget()
        self.status = self.main_window.statusBar()
        
        ### Main tab ###

        main_frame = QtGui.QFrame()

        tooltip_text = 'The location of the source TeX file used\nto create the output.'
        self.infile_textbox = QtGui.QLineEdit(main_frame)
        self.infile_textbox.setText(self.inputfile)
        self.infile_textbox.setGeometry(100, 14, 200, 24)
        self.infile_textbox.setAlignment(QtCore.Qt.AlignRight)
        self.infile_textbox.setDisabled(True)
        self.infile_textbox.setToolTip(tooltip_text)
        infile_textlabel = QtGui.QLabel('Input file', main_frame)
        infile_textlabel.setGeometry(*dim_infile_textlabel)
        infile_textlabel.setToolTip(tooltip_text)
        infile_button = QtGui.QPushButton('...', main_frame)
        infile_button.setGeometry(*dim_infile_button)
        infile_button.setToolTip(tooltip_text)
        main_frame.connect(self.infile_textbox,
                           QtCore.SIGNAL('editingFinished()'),
                           self.set_input_file)
        main_frame.connect(infile_button,
                           QtCore.SIGNAL('clicked()'),
                           self.open_infile_dialog)

        tooltip_text = 'The location of the style file that will\nbe created by Batch Commander. Note that\nthe source document must reference this file.'
        self.scriptfile_textbox = QtGui.QLineEdit(main_frame)
        self.scriptfile_textbox.setText(self.scriptfile)
        self.scriptfile_textbox.setGeometry(100, 40, 200, 24)
        self.scriptfile_textbox.setAlignment(QtCore.Qt.AlignRight)
        self.scriptfile_textbox.setToolTip(tooltip_text)
        scriptfile_textlabel = QtGui.QLabel('Script file', main_frame)
        scriptfile_textlabel.setGeometry(10, 40, 90, 24)
        scriptfile_textlabel.setToolTip(tooltip_text)
        scriptfile_button = QtGui.QPushButton('...', main_frame)
        scriptfile_button.setGeometry(310, 40, 30, 24)
        scriptfile_button.setToolTip(tooltip_text)
        main_frame.connect(self.scriptfile_textbox,
                           QtCore.SIGNAL('editingFinished()'),
                           self.set_script_file)
        main_frame.connect(scriptfile_button,
                           QtCore.SIGNAL('clicked()'),
                           self.open_scriptfile_dialog)

        tooltip_text = 'The location of the output PDF file to be\ngenerated.'
        self.outfile_textbox = QtGui.QLineEdit(main_frame)
        self.outfile_textbox.setGeometry(100, 66, 200, 24)
        self.outfile_textbox.setText(self.outputfile)
        self.outfile_textbox.setAlignment(QtCore.Qt.AlignRight)
        self.outfile_textbox.setToolTip(tooltip_text)
        outfile_textlabel = QtGui.QLabel('Output file', main_frame)
        outfile_textlabel.setGeometry(10, 66, 90, 24)
        outfile_textlabel.setToolTip(tooltip_text)
        outfile_button = QtGui.QPushButton('...', main_frame)
        outfile_button.setGeometry(310, 66, 30, 24)
        outfile_button.setToolTip(tooltip_text)
        main_frame.connect(self.outfile_textbox,
                           QtCore.SIGNAL('editingFinished()'),
                           self.set_output_file)
        main_frame.connect(outfile_button,
                           QtCore.SIGNAL('clicked()'),
                           self.open_outfile_dialog)

        self.run_button = QtGui.QPushButton('&Run', main_frame)
        self.run_button.setGeometry(200, 92, 100, 30)
        main_frame.connect(self.run_button,
                           QtCore.SIGNAL('clicked()'),
                           self.run)
        self.pdfview_button = QtGui.QPushButton('&Show PDF View', main_frame)
        self.pdfview_button.setGeometry(310, 92, 100, 30)
        main_frame.connect(self.pdfview_button,
                           QtCore.SIGNAL('clicked()'),
                           self.on_pdfview_button_clicked)

        immediate_box = QtGui.QCheckBox('&Immediate mode', main_frame)
        immediate_box.setGeometry(10, 92, 150, 30)
        immediate_box.setChecked(self.immediate_mode)
        immediate_box.setToolTip('If enabled, Batch Commander will immediately \ngenerate the output file once a control is changed.')
        main_frame.connect(immediate_box,
                           QtCore.SIGNAL('stateChanged(int)'),
                           self.set_immediate_mode)
        self.tab_bar.addTab(main_frame, '&Main')

        ### Datafiles tab ###

        data_frame = QtGui.QFrame()
        list_container = QtGui.QScrollArea(data_frame)
        list_container.setGeometry(10,10, 220, 120)

        self.add_button = QtGui.QPushButton('+', data_frame)
        self.add_button.setGeometry(235,10,20,20)
        self.remove_button = QtGui.QPushButton('-', data_frame)
        self.remove_button.setGeometry(235,35,20,20)
        self.main_window.connect(self.add_button,
                                 QtCore.SIGNAL('clicked()'),
                                 self.add_dataset)
        self.main_window.connect(self.remove_button,
                                 QtCore.SIGNAL('clicked()'),
                                 self.remove_dataset)

        self.data_list = QtGui.QListWidget(list_container)
        # list widget size is the same as the container
        self.data_list.setGeometry(list_container.contentsRect())
        self.data_list_items = []
        for dataset in self.datasets:
            self.add_list_item(dataset)
        self.data_list.connect(self.data_list,
                               QtCore.SIGNAL('itemChanged(QListWidgetItem *)'),
                               self.on_list_item_changed)
        # should instead check the first dataset
        for item in self.data_list_items:
            if item.text() == self.datasets[0].name:
                item.setCheckState(QtCore.Qt.Checked)

        self.tab_bar.addTab(data_frame, '&Data files')

        ### Options tab ###
        # options_frame = QtGui.QFrame()
        # self.tab_bar.addTab(options_frame, '&Options')

        ### wrap up main window ###
        self.main_window.setGeometry(0, 60, MAINBOXWIDTH+40, MAINBOXHEIGHT)
        self.main_window.connect(self.process, QtCore.SIGNAL('finished(int)'), self.on_process_finished)
        self.status.showMessage('Ready.')
        self.main_window.setCentralWidget(self.tab_bar)
        self.main_window.show()

    def show_controls_window(self):
        '''Create and display the controls window.'''

        self.controls_window = QtGui.QMainWindow()
        self.controls_window.setWindowTitle('Batch Commander: Controls')
        self.control_status = self.controls_window.statusBar()
        self.control_status.showMessage(' ')

        self.toolbar = QtGui.QToolBar(self.controls_window)
        self.dataset_selector = QtGui.QComboBox()
        # self.dataset_selector.setGeometry(5, 5, 150, 30)
        self.update_selector()
        self.controls_window.connect(self.dataset_selector,
                                     QtCore.SIGNAL('activated(int)'),
                                     self.on_selector_changed)
        self.reload_button = QtGui.QPushButton('&Reload')
        self.reload_button.setGeometry(FIELDWIDTH - 80, 5, 100, 30)
        self.controls_window.connect(self.reload_button,
                                     QtCore.SIGNAL('clicked()'),
                                     self.reload_current_dataset)
        self.toolbar.setAllowedAreas(QtCore.Qt.TopToolBarArea)
        self.toolbar.addWidget(self.dataset_selector)
        self.toolbar.addWidget(self.reload_button)
        self.toolbar.setFloatable(False)
        self.toolbar.setMovable(False)


        # Check if there are any datafiles
        try:
            self.current_dataset = self.datasets[0]
        except IndexError:
            self.current_dataset = None
        self.docks = []
        self.update_docks()

        self.set_immediate_mode(self.immediate_mode)
        # self.toolbox.setGeometry(0,40,FIELDWIDTH+25,400)
        self.controls_window.setGeometry(0,MAINBOXHEIGHT+60,FIELDWIDTH+25,450)
        self.controls_window.addToolBar(self.toolbar)
        self.controls_window.show()

    def update_selector(self):
        if self.dataset_selector:
            self.dataset_selector.clear()
            active_datasets = [dataset.name for dataset in self.datasets \
                                    if dataset.active]
            self.dataset_selector.addItems(active_datasets)

    def reload_current_dataset(self):
        path = self.current_dataset.path
        new_dataset = DataSet(path)
        self.current_dataset = new_dataset
        self.update_toolbox()

    def update_docks(self):
        # clear it
        for d in self.docks:
            d.destroy()

        self.controls = []
        for section in self.current_dataset.sections:
            scrollbox = QtGui.QScrollArea()
            # count fields
            numberOfFields = len(section.fields)
            # make frame
            container = QtGui.QFrame(scrollbox)
            container.setGeometry(0,0,FIELDWIDTH, FIELDHEIGHT*numberOfFields)
            fieldCount = 0
            for field in section.fields:
                control = create_control_from_field(field, parent=container,
                                                    width=FIELDWIDTH,
                                                    height=FIELDHEIGHT)
                # place the control in absolute coords -- sucks but works
                control.setGeometry(0,fieldCount*FIELDHEIGHT,
                                    FIELDWIDTH, FIELDHEIGHT)
                self.controls.append(control)
                self.controls_window.connect(control,
                                             QtCore.SIGNAL('fieldEnter(PyQt_PyObject)'),
                                             self.on_control_entered)
                self.controls_window.connect(control,
                                             QtCore.SIGNAL('fieldLeave(PyQt_PyObject)'),
                                             self.on_control_left)
                fieldCount += 1
            scrollbox.setWidget(container)
            # make scrollbox flat
            scrollbox.setFrameStyle(container.NoFrame)

            # create dock widget
            dock = QtGui.QDockWidget(section.name)
            t = TitleBarWidget(section.name, dock)
            dock.setTitleBarWidget(t)
            dock.setWidget(scrollbox)
            self.docks.append(dock)
            self.controls_window.connect(t,
                                         QtCore.SIGNAL('titleClicked(PyQt_PyObject)'),
                                         self.toggle_dock_visibility)
            self.controls_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dock)
            if len(self.docks) > 1:
                dock.widget().setVisible(False)
        #for d in self.docks:
        #    self.controls_window.tabifyDockWidget(self.docks[0], d)


    def run(self):
        # make sure input file exists
        if not os.path.exists(self.inputfile):
            self.status.showMessage("Input file doesn't exist!", 2000)
            return
        self.run_button.setDisabled(True)
        # self.toolbox.setDisabled(True)
        self.status.showMessage('Generating %s...' % (self.scriptfile))
        
        try:
            scriptfile = open(self.scriptfile, 'w')
            self.start_time = datetime.now()

            if self.outputmode == MODE_TEX:
                scriptfile.write('\AtBeginDocument{\n')
                for dataset in self.datasets:
                    if dataset.active:
                        for section in dataset.sections:
                            section.output_texstyle(scriptfile)
                scriptfile.write('                }\n')

            elif self.outputmode == MODE_PYTHON:
                for dataset in self.datasets:
                    if dataset.active:
                        for section in dataset.sections:
                            section.output_pythonvar(scriptfile)

            scriptfile.close()
            self.status.showMessage('Outputting %s...' % (self.outputfile))
            self.process.start(self.command % {'input_file': self.inputfile})

        except NotInstalledError:
            self.run_button.setEnabled(True)
            # self.toolbox.setEnabled(True)
            self.status.showMessage('Failed :(')
        except:
            self.run_button.setEnabled(True)
            # self.toolbox.setEnabled(True)
            self.status.showMessage('Failed :(')
            

    #### Callbacks ####

    def set_input_file(self):
        self.inputfile = str(self.infile_textbox.displayText())
        directory = os.path.dirname(self.inputfile)
        filename = os.path.basename(self.inputfile)
        # track where the log file generated by pdftex will be
        self.logfile = '%s.log' % (os.path.join(directory,
                                   os.path.splitext(filename)[0]))
        # set the working directory for QProcess (otherwise pdflatex will fail)
        self.process.setWorkingDirectory(directory)

    def set_script_file(self):
        self.scriptfile = self.scriptfile_textbox.displayText()

    def set_output_file(self):
        self.outputfile = self.outfile_textbox.displayText()

    def open_infile_dialog(self):
        pwd = os.getcwd()
        filename = QtGui.QFileDialog.getOpenFileName(self.main_window,
                                     'Open input file',
                                     pwd,
                                     'TeX/LaTeX files (*.tex)')
        if not filename:
            return False
        # FIXME: this could be made without repeating set_input_file
        self.inputfile = str(filename)
        self.infile_textbox.setText(self.inputfile)
        directory = os.path.dirname(self.inputfile)
        filename = os.path.basename(self.inputfile)
        # track where the log file generated by pdflatex will be
        self.logfile = '%s.log' % (os.path.join(directory,
                                   os.path.splitext(filename)[0]))

    def open_scriptfile_dialog(self):
        pwd = os.getcwd()
        filename = QtGui.QFileDialog.getSaveFileName(self.main_window, 'Save script file',
                                     pwd,
                                     'TeX/LaTeX style files (*.sty)')
        if not filename:
            return False
        self.scriptfile = str(filename)
        self.scriptfile_textbox.setText(self.scriptfile)

    def open_outfile_dialog(self):
        pwd = os.getcwd()
        filename = QtGui.QFileDialog.getSaveFileName(self.main_window, 'Save output file',
                                     pwd,
                                     'PDF files (*.pdf)')
        if not filename:
            return False
        self.outputfile = str(filename)
        self.outfile_textbox.setText(self.outputfile)

    def set_immediate_mode(self, value):
        self.immediate_mode = bool(value)
        if self.immediate_mode:
            for control in self.controls:
                control.connect(control,
                                QtCore.SIGNAL('controlChanged()'),
                                self.run)
        else:
            for control in self.controls:
                control.disconnect(control,
                                   QtCore.SIGNAL('controlChanged()'),
                                   self.run)

    def toggle_dock_visibility(self, dock):
        if dock.widget().isVisible():
            dock.widget().setVisible(False)
        else:
            dock.widget().setVisible(True)

    def on_list_item_changed(self, item):
        value = bool(item.checkState())
        for dataset in self.datasets:
            if item.text() == dataset.name:
                if value:
                    self.enable_dataset(dataset)
                else:
                    self.disable_dataset(dataset)

    def on_selector_changed(self, index):
        prev_dataset_name = self.current_dataset.name
        new_dataset_name = self.dataset_selector.itemText(index)

        if prev_dataset_name != new_dataset_name:
            for dataset in self.datasets:
                if dataset.name == new_dataset_name:
                    self.current_dataset = dataset
            self.update_toolbox()

    def on_control_entered(self, control):
        self.control_status.showMessage(control.name)

    def on_control_left(self, field):
        self.control_status.showMessage(' ')

    def on_process_finished(self, value):
        # error codes from QProcess are not to be trusted, so we also
        # check if the log file has stuff in it
        try:
            log = open(self.error_log_filename, 'r')
            error_log_has_stuff = bool(log.read())
        except IOError:
            error_log_has_stuff = False
        if value or error_log_has_stuff:
            self.status.showMessage('Failed -- see the error.log file for details')
        else:
            # pdflatex creates the output pdf inside the directory that contains
            # the TeX file, so we have to move it to the place specified in the UI
            outfilename = self.inputfile.replace('.tex', '.pdf')
            shutil.move(outfilename, self.outputfile)
            # the following hack is equivalent to the 'touch' command in bash
            fhandle = file(self.outputfile, 'a')
            try:
                os.utime(self.outputfile, None)
            finally:
                fhandle.close()

            '''
            # on OSX, we open Preview, and if it's already open we poke it for auto-reloading
            if sys.platform == 'darwin':
                if sys.version_info < (2,6):
                    os.system('open %s' % self.outputfile)
                else:
                    import subprocess
                    subprocess.call('open %s' % self.outputfile, shell=True)
            '''
            if self.is_pdfviewer_open:
                self.pdfviewer.load(self.outputfile)

            self.end_time = datetime.now()
            elapsed = self.end_time - self.start_time
            s = elapsed.seconds
            if s > 5:
                minutes, seconds = divmod(s, 60)
                timestring = '%02d:%02d' % (minutes, seconds)
            else:
                timestring = '00:%02d.%d' % (s, elapsed.microseconds)
            self.status.showMessage('Done in ' + timestring + '.')
        self.run_button.setEnabled(True)
        # self.toolbox.setEnabled(True)

    def on_pdfview_button_clicked(self):
        self.is_pdfviewer_open = not self.is_pdfviewer_open
        if self.is_pdfviewer_open:
            # show the pdf viewer
            self.pdfviewer.show()
            self.pdfview_button.setText('Hide PDF View')
        else:
            # hide the pdf viewer
            self.pdfviewer.hide()
            self.pdfview_button.setText('Show PDF View')

    def add_list_item(self, dataset):
        name = dataset.name
        it = QtGui.QListWidgetItem(name, self.data_list)
        dataset.widget = it
        it.setFlags(QtCore.Qt.ItemIsEnabled|
                    QtCore.Qt.ItemIsUserCheckable|
                    QtCore.Qt.ItemIsSelectable)
        it.setCheckState(QtCore.Qt.Unchecked)
        self.data_list_items.append(it)

    def add_dataset(self):
        pwd = os.getcwd()
        # TODO: set parent
        filename = QtGui.QFileDialog.getOpenFileName(self.main_window,
                                     'Open input file',
                                     pwd,
                                     'Batch Commander data files (*.data)')
        if not filename:
            return False
        dataset = DataSet(str(filename))
        self.datasets.append(dataset)
        self.add_list_item(dataset)
        self.remove_button.setEnabled(True)
        
    def remove_dataset(self):
        selected_item = self.data_list.currentItem() 
        selected_row = self.data_list.currentRow()  
        for dataset in self.datasets:
            if dataset.name == selected_item.text():
                if dataset.active:
                    self.disable_dataset(dataset)
                    self.data_list.takeItem(selected_row)    
                self.datasets.pop(self.datasets.index(dataset))
                self.data_list_items.pop(self.data_list_items.index(selected_item))
                self.data_list.takeItem(selected_row)
                print 'dataset disabled'
                break
        if len(self.datasets) == 1:
            self.remove_button.setDisabled(True)        

    def enable_dataset(self, dataset):
        log.debug('Enabling dataset ' + dataset.name)
        dataset.active = True
        
        self.update_selector()
        
        if self.dataset_selector:
            index = self.dataset_selector.findText(self.current_dataset.name)
            self.dataset_selector.setCurrentIndex(index)

    def disable_dataset(self, dataset):
        dataset_count = 0
        for ds in self.datasets:
            if ds.active:
                dataset_count += 1
        # is it the last active one?
        if dataset_count < 2:
            # keep the item checked
            for item in self.data_list_items:
                if item.text() == dataset.name:
                    item.setCheckState(QtCore.Qt.Checked)
            self.status.showMessage('At least one dataset must be selected.', 2500)
            return
        # otherwise, let's disable it
        log.debug('Disabling dataset ' + dataset.name)
        dataset.active = False
               
        if dataset == self.current_dataset:
            for dataset in self.datasets:
                if dataset.active:
                    self.current_dataset = dataset
                    self.update_toolbox()
            log.debug('Current dataset set to ' + self.current_dataset.name)
        self.update_selector()

    def dataset_by_name(self, name):
        for dataset in self.datasets:
            if name == dataset.name:
                return dataset
        return None

    def check_for_tex(self):
        # MacTeX places the TeX binaries somewhere else
        if sys.platform == 'darwin':
            tex_cmd = '/usr/texbin/tex -version'
            pdflatex_cmd = '/usr/texbin/pdflatex -version'
        else:
            tex_cmd = 'tex -version'
            pdflatex_cmd = 'pdflatex -version'

        # bug 1068268 in Python prevents us from using subprocess.call
        # in versions under 2.6
        retcode = os.system(tex_cmd)
        if retcode:
            self.show_error_window('TeX is not installed.', 
                                   'Batch Commander requires TeX to run.')
            sys.exit()

        retcode = os.system(pdflatex_cmd)
        if retcode:
            self.show_error_window('PDFLaTeX is not installed.', 
                                   'Batch Commander requires PDFLaTeX to run.')
            sys.exit()

    def show_error_window(self, text, infotext):
        msgbox = QtGui.QMessageBox()
        msgbox.setText(text)
        msgbox.setInformativeText(infotext)
        msgbox.setIcon(QtGui.QMessageBox.Critical)
        msgbox.exec_()

if __name__ == '__main__':
    bc = BatchCommander(datafile=sys.argv[1])
    bc.show_ui()
