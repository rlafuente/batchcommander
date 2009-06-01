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
from PyQt4 import QtGui, QtCore
from batchcommander.controls import ColorChooserControl, NumberControl, ToggleControl, ChoiceControl, create_control_from_field
from batchcommander.parser import Section, Field, parse_datafile, generate_fields
from batchcommander.defaults import UNITS, TOGGLE, COLOR, NUMBER, CHOICE


DEFAULT_INPUTFILE = './sarovar.tex'
DEFAULT_SCRIPTFILE = './river_valley.sty'
DEFAULT_OUTPUTFILE = './output.pdf'
# FIXME: the pdf output name is not applied
DEFAULT_COMMAND = 'pdflatex -halt-on-error %(input_file)s %(output_file)s'
DEFAULT_IMMEDIATE_MODE = True

MAINBOXWIDTH = 370
MAINBOXHEIGHT = 200
FIELDHEIGHT = 36
FIELDWIDTH = 375
MODE_TEX = 'tex'
MODE_PYTHON = 'python'

class BatchCommander:
    '''Launch the Batch Commander UI.'''
    def __init__(self, 
                 datafile, 
                 inputfile=DEFAULT_INPUTFILE, 
                 scriptfile=DEFAULT_SCRIPTFILE, 
                 outputfile=DEFAULT_OUTPUTFILE,
                 command=DEFAULT_COMMAND,
                 immediate_mode=DEFAULT_IMMEDIATE_MODE,
                 output_mode=MODE_TEX):
        self.datafile = datafile
        self.inputfile = inputfile
        self.scriptfile = scriptfile
        self.outputfile = outputfile
        self.outputmode = output_mode
        self.sections = None
        self.immediate_mode = immediate_mode
        self.command = command
        self.process = QtCore.QProcess()
        # self.process.setStandardOutputFile(sys.stdout)
        self.process.setStandardErrorFile('error.log')
        
    def show_ui(self):       
        self.app = QtGui.QApplication(sys.argv)
        self.show_main_window()
        self.show_controls_window()
        
    def show_main_window(self):
        '''Create and display the main interface window.'''
        self.main_window = QtGui.QMainWindow()
        self.tab_bar = QtGui.QTabWidget(self.main_window)
        self.status = self.main_window.statusBar()
        main_frame = QtGui.QFrame()
        
        self.infile_textbox = QtGui.QLineEdit(main_frame)
        self.infile_textbox.setGeometry(100, 14, 200, 24)
        self.infile_textbox.setText(self.inputfile)
        infile_textlabel = QtGui.QLabel('Input file', main_frame)
        infile_textlabel.setGeometry(10, 14, 50, 24)
        infile_button = QtGui.QPushButton('...', main_frame)
        infile_button.setGeometry(310, 14, 30, 24)
        main_frame.connect(self.infile_textbox, 
                           QtCore.SIGNAL('editingFinished()'), 
                           self.set_input_file)
        main_frame.connect(infile_button,
                           QtCore.SIGNAL('clicked()'),
                           self.open_infile_dialog)
                           
        self.scriptfile_textbox = QtGui.QLineEdit(main_frame)
        self.scriptfile_textbox.setGeometry(100, 40, 200, 24)
        self.scriptfile_textbox.setText(self.scriptfile)
        scriptfile_textlabel = QtGui.QLabel('Script file', main_frame)
        scriptfile_textlabel.setGeometry(10, 40, 50, 24)
        scriptfile_button = QtGui.QPushButton('...', main_frame)
        scriptfile_button.setGeometry(310, 40, 30, 24)        
        main_frame.connect(self.scriptfile_textbox, 
                           QtCore.SIGNAL('editingFinished()'), 
                           self.set_script_file)
        main_frame.connect(scriptfile_button,
                           QtCore.SIGNAL('clicked()'),
                           self.open_scriptfile_dialog)

        self.outfile_textbox = QtGui.QLineEdit(main_frame)
        self.outfile_textbox.setGeometry(100, 66, 200, 24)
        self.outfile_textbox.setText(self.outputfile)
        outfile_textlabel = QtGui.QLabel('Output file', main_frame)
        outfile_textlabel.setGeometry(10, 66, 50, 24)
        outfile_button = QtGui.QPushButton('...', main_frame)
        outfile_button.setGeometry(310, 66, 30, 24)
        main_frame.connect(self.outfile_textbox, 
                           QtCore.SIGNAL('editingFinished()'), 
                           self.set_output_file)
        main_frame.connect(outfile_button,
                           QtCore.SIGNAL('clicked()'),
                           self.open_outfile_dialog)
        
        self.run_button = QtGui.QPushButton('&Run', main_frame)
        self.run_button.setGeometry(190, 100, 100, 30)
        main_frame.connect(self.run_button, 
                           QtCore.SIGNAL('clicked()'), 
                           self.run)
        immediate_box = QtGui.QCheckBox('&Immediate mode', main_frame)
        immediate_box.setGeometry(10, 100, 100, 30)
        immediate_box.setChecked(self.immediate_mode)
        main_frame.connect(immediate_box, 
                           QtCore.SIGNAL('stateChanged(int)'), 
                           self.set_immediate_mode)                   
                           
        self.tab_bar.addTab(main_frame, '&Main')
        data_frame = QtGui.QFrame()
        self.tab_bar.addTab(data_frame, '&Data files')
        options_frame = QtGui.QFrame()
        self.tab_bar.addTab(options_frame, '&Options')
        tab_bar_height = MAINBOXHEIGHT - self.status.height()
        self.tab_bar.setGeometry(0, 0, MAINBOXWIDTH, tab_bar_height)
        self.main_window.setGeometry(0, 0, MAINBOXWIDTH, MAINBOXHEIGHT)
        self.main_window.connect(self.process, 
                                 QtCore.SIGNAL('finished(int)'), 
                                 self.on_process_finished)
        self.status.showMessage('Ready.')
        self.main_window.show()

    def show_controls_window(self):
        '''Create and display the controls window.'''
        datadict = parse_datafile(self.datafile)
        self.toolbox = QtGui.QToolBox()
        self.sections = generate_fields(datadict)
        self.controls = []
        for section in self.sections:
            # count fields
            numberOfFields = len(section.fields)
            # make frame        
            container = QtGui.QFrame()
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
                fieldCount += 1
            self.scrollbox = QtGui.QScrollArea()
            self.scrollbox.setWidget(container)
            # make scrollbox flat
            self.scrollbox.setFrameStyle(container.NoFrame)
            self.toolbox.addItem(self.scrollbox, section.name)
        # apply immediate mode settings to all fields
        self.set_immediate_mode(self.immediate_mode)
        self.toolbox.show()
        self.toolbox.setGeometry(0,MAINBOXHEIGHT,FIELDWIDTH+25,400)

        sys.exit(self.app.exec_())

    def run(self):
        self.run_button.setDisabled(True)
        self.toolbox.setDisabled(True)
        self.status.showMessage('Generating %s...' % (self.scriptfile))
        scriptfile = open(self.scriptfile, 'w')
    
        if self.outputmode == MODE_TEX:
            scriptfile.write('\AtBeginDocument{\n')
            for section in self.sections:
                section.output_texstyle(scriptfile)
            scriptfile.write('                }\n')
            
        elif self.outputmode == MODE_PYTHON:
            for section in self.sections:
                section.output_pythonvar(scriptfile)
                
        scriptfile.close()
        self.status.showMessage('Outputting %s...' % (self.outputfile))
        self.process.start(self.command % {'input_file': self.inputfile, 
                                           'output_file': self.outputfile})
                                  
    #### Callbacks ####
    
    def set_input_file(self):
        self.inputfile = str(self.infile_textbox.displayText())
        directory = os.path.dirname(self.inputfile)
        filename = os.path.basename(self.inputfile)
        # track where the log file generated by pdflatex will be
        self.logfile = '%s.log' % (os.path.join(directory,
                                   os.path.splitext(filename)[0]))
        
    def set_script_file(self):
        self.scriptfile = self.scriptfile_textbox.displayText()
        
    def set_output_file(self):
        self.outputfile = self.outfile_textbox.displayText()
        
    def open_infile_dialog(self):
        pwd = os.getcwd()
        # TODO: set parent
        filename = QtGui.QFileDialog.getOpenFileName(self.main_window, 
                                     'Open input file',
                                     pwd,
                                     'TeX/LaTeX files (*.tex)')
        if not filename:
            return False
        # this could be made without repeating set_input_file
        self.inputfile = str(filename)
        self.infile_textbox.setText(self.inputfile)
        directory = os.path.dirname(self.inputfile)
        filename = os.path.basename(self.inputfile)
        # track where the log file generated by pdflatex will be
        self.logfile = '%s.log' % (os.path.join(directory,
                                   os.path.splitext(filename)[0]))
    
    def open_scriptfile_dialog(self):
        pwd = os.getcwd()
        # TODO: set parent
        filename = QtGui.QFileDialog.getSaveFileName(self.main_window, 'Save script file',
                                     pwd,
                                     'TeX/LaTeX style files (*.sty)')
        if not filename:
            return False
        self.scriptfile = str(filename)
        self.scriptfile_textbox.setText(self.scriptfile)
    
    def open_outfile_dialog(self):
        pwd = os.getcwd()
        # TODO: set parent
        filename = QtGui.QFileDialog.getSaveFileName(self.main_window, 'Save output file',
                                     pwd,
                                     'PDF files (*.pdf)')
        if not filename:
            return False
        self.outputfile = str(filename)
        self.outputfile_textbox.setText(self.outputfile)
    
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
        
    def on_process_finished(self, value):
        if value:
            self.status.showMessage('Failed -- see the error.log file for details')
        else:
            self.status.showMessage('Done!')
        self.run_button.setEnabled(True)
        self.toolbox.setEnabled(True)
        
    def add_datafiles(self, filelist):
        self.datafiles.extend()
        
    def remove_datafile(self, name):
        self.datafiles.pop(self.datafiles.index(name))

if __name__ == '__main__':
    bc = BatchCommander(datafile=sys.argv[1])
    bc.show_ui()
