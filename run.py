#!/usr/bin/env python

# run.py is copyright (C) 2009 by Ricardo Lafuente
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

import sys
from PyQt4 import QtGui, QtCore
from batchcommander.controls import ColorChooserControl, NumberControl, ToggleControl, ChoiceControl, createControlFromField
from batchcommander.parser import *
from batchcommander.defaults import *

DATAFILE = sys.argv[1]
INPUTFILE = '/home/rlafuente/work/bc/texfiles/sarovar.tex'
OUTPUTFILE = '/home/rlafuente/work/bc/texfiles/river_valley.sty'

IMMEDIATE = True


def outputStyFile():
    global sections

    file = open(OUTPUTFILE, 'w')

    file.write('\AtBeginDocument{\n')
    for section in sections:
        section.styleOutput(file)
    file.write('                }\n')
    file.close()
    import os
    os.system('pdflatex %s output.pdf' % INPUTFILE)

def alarm():
    print 'wooot!'

app = QtGui.QApplication(sys.argv)
datadict = parse_datafile(DATAFILE)
toolbox = QtGui.QToolBox()
sections = generate_fields(datadict)

for section in sections:
    container = QtGui.QWidget()
    box = QtGui.QVBoxLayout(container)
    for field in section.fields:
        control = createControlFromField(field)
        if IMMEDIATE:
            control.connect(control, QtCore.SIGNAL('controlChanged()'), outputStyFile)
        box.addWidget(control)

    toolbox.addItem(container, section.name)

##if IMMEDIATE:
##    toolbox.connect(toolbox, QtCore.SIGNAL('controlChanged()'), alarm)
toolbox.show()
toolbox.setGeometry(0,0,400,400)

groupBox = QtGui.QGroupBox()
runButton = QtGui.QPushButton('Run', groupBox)
groupBox.connect(runButton, QtCore.SIGNAL('clicked()'), outputStyFile)
# groupBox.addWidget(runButton)
groupBox.show()

sys.exit(app.exec_())
