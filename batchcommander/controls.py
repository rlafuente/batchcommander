#!/usr/bin/python

# controls.py is copyright (C) 2009 by Ricardo Lafuente
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
'''GUI widgets for Batch Commander'''

from __future__ import division
import sys
from PyQt4 import QtGui, QtCore
from defaults import *


class Control(QtGui.QWidget):
    def __init__(self, field, parent=None, width=250, height=36):
        QtGui.QWidget.__init__(self, parent)

        self.width = width
        self.height = height

        self.field = field
        self.active = self.field.active

        self.name = self.field.name

        self.longname = self.name
        if self.field.longname:
            self.longname = self.field.longname

        self.hboxwidget = QtGui.QWidget(self)
        self.hboxwidget.setGeometry(QtCore.QRect(150,0,225,self.height))
        self.hbox = QtGui.QHBoxLayout(self.hboxwidget)

        self.label = QtGui.QLabel(self.longname, self)
        self.label.setGeometry(QtCore.QRect(0,0,self.width,self.height))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.label.setGeometry(0,0,150,self.height)

        self.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred))

        # create the 'active' checkbox
        self.activeBox = QtGui.QCheckBox('', self)
        self.activeBox.setChecked(True)
        self.connect(self.activeBox, QtCore.SIGNAL('stateChanged(int)'), self.setActive)
        
        if self.field.always_active:
            self.activeBox.setVisible(False)
            
        # self.setActive(self.active)
        # TODO: tooltip

    def isActive(self):
        return self.active

    def setValue(self, value):
        pass
    
    def setActive(self, state):
        self.active = self.field.active = bool(state)

    def getValue(self, value):
        pass



class ToggleControl(Control):
    def __init__(self, *args, **kwargs):
        Control.__init__(self, *args, **kwargs)

        self.value = self.field.value

        self.checkBox = QtGui.QCheckBox('', self)
        self.checkBox.setChecked(self.value)
        self.connect(self.checkBox, QtCore.SIGNAL('stateChanged(int)'), self.setValue)
        self.hbox.addWidget(self.checkBox)
        self.hbox.addStretch()
        self.hbox.addWidget(self.activeBox)

        if not self.active:
            self.setActive(self.active)
            self.activeBox.setChecked(self.active)

    def setValue(self, value):
        self.value = self.field.value = bool(value)
        self.emit(QtCore.SIGNAL('controlChanged()'))
    
    def setActive(self, state):
        self.active = self.field.active = bool(state)
        self.label.setEnabled(self.active)
        self.checkBox.setEnabled(self.active)

    def getValue(self):
        return self.value

class ChoiceControl(Control):
    def __init__(self, *args, **kwargs):
        Control.__init__(self, *args, **kwargs)

        self.choices = self.field.choices
        self.value = str(self.field.value)

        self.choiceBox = QtGui.QComboBox(self)
        self.choiceBox.addItems(self.choices)
        # select the specified value
        self.choiceBox.setCurrentIndex(self.choiceBox.findText(self.value))
        self.connect(self.choiceBox, QtCore.SIGNAL('activated(int)'), self.setValue)

        self.hbox.addWidget(self.choiceBox)
        self.hbox.addStretch()
        self.hbox.addWidget(self.activeBox)
        
        if not self.active:
            self.setActive(self.active)
            self.activeBox.setChecked(self.active)

    def setValue(self, index):
        self.value = self.field.value = self.choiceBox.itemText(index)
        self.emit(QtCore.SIGNAL('controlChanged()'))
        # self.choiceBox.setCurrentIndex(self.choiceBox.findText(self.value))

    def getValue(self):
        return self.value

    def updateValue(self):
        # updates stored values according to user interaction
        self.value = self.field.value = self.choiceBox.currentText()
        
    def setActive(self, state):
        self.active = self.field.active = bool(state)
        self.label.setEnabled(self.active)
        self.choiceBox.setEnabled(self.active)


class NumberControl(Control):
    def __init__(self, *args, **kwargs):
        Control.__init__(self, *args, **kwargs)

        self.value = self.field.value
        self.min = self.field.min
        self.max = self.field.max
        self.increment = self.field.increment
        self.decimals = self.field.decimals

        if not self.decimals:
            self.decimals = 0

        self.floating = False
        if type(self.value) == float or \
                type(self.min) == float or \
                type(self.max) == float or \
                type(self.increment) == float or \
                self.decimals:
            self.floating = True

        if self.floating:
            self.numberbox = QtGui.QDoubleSpinBox(self)
            if not self.decimals:
                self.decimals = 1
            self.numberbox.setDecimals(self.decimals)
        else:
            self.numberbox = QtGui.QSpinBox(self)
        self.numberbox.setMinimum(self.min)
        self.numberbox.setMaximum(self.max)
        self.numberbox.setSingleStep(self.increment)

        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.slider.setRange(self.min * pow(10,self.decimals), self.max * pow(10,self.decimals))
        self.slider.setSingleStep(self.increment)

        # set widgets to initial value before connecting
        self.setValue(self.value)
        
        # and now connect the signals
        #self.connect(self.slider, QtCore.SIGNAL('activated()'), self.updateNumberboxFromSlider)
        self.connect(self.slider, QtCore.SIGNAL('sliderReleased()'), self.setValueFromSlider)
        self.connect(self.slider, QtCore.SIGNAL('valueChanged(int)'), self.updateNumberboxFromSlider)
        if self.floating:
            self.connect(self.numberbox, QtCore.SIGNAL('valueChanged(double)'), self.setValue)
        else:
            self.connect(self.numberbox, QtCore.SIGNAL('valueChanged(int)'), self.setValue)

        self.hbox.addWidget(self.slider)
        self.hbox.addWidget(self.numberbox)
        self.hbox.addWidget(self.activeBox)

        if self.field.unit:
            self.unitComboBox = QtGui.QComboBox(self)
            self.unitComboBox.addItems(UNITS)
            # select the specified unit
            self.unitComboBox.setCurrentIndex(self.unitComboBox.findText(self.field.unit))
            self.unitComboBox.connect(self.unitComboBox, QtCore.SIGNAL('activated(int)'), self.setUnit)
            self.hbox.insertWidget(2, self.unitComboBox)

        if not self.active:
            self.setActive(self.active)
            self.activeBox.setChecked(self.active)

    def setUnit(self, index):
        self.unit = self.field.unit = self.unitComboBox.itemText(index)

    def setValue(self, value):
        self.value = self.field.value = value
        self.slider.setValue(value * pow(10, self.decimals))
        self.numberbox.setValue(value)
        self.emit(QtCore.SIGNAL('controlChanged()'))

    def setValueFromSlider(self):
        v = self.slider.value() / pow(10, self.decimals)
        self.setValue(v)
        
    def updateNumberboxFromSlider(self, value):
        v = value / pow(10, self.decimals)
        # quick hack to prevent numberbox to sending the valueChanged
        # signal
        self.disconnect(self.numberbox, QtCore.SIGNAL('valueChanged(double)'), self.setValue)
        self.disconnect(self.numberbox, QtCore.SIGNAL('valueChanged(int)'), self.setValue)
        self.numberbox.setValue(v)
        if self.floating:
            self.connect(self.numberbox, QtCore.SIGNAL('valueChanged(double)'), self.setValue)
        else:
            self.connect(self.numberbox, QtCore.SIGNAL('valueChanged(int)'), self.setValue)

    def getValue(self):
        return self.value
    
    def setActive(self, state):
        self.active = self.field.active = bool(state)
        self.label.setEnabled(self.active)
        self.numberbox.setEnabled(self.active)
        if self.field.unit:
            self.unitComboBox.setEnabled(self.active)
        self.slider.setEnabled(self.active)

class ColorChooserControl(Control):
    def __init__(self, *args, **kwargs):
        Control.__init__(self, *args, **kwargs)

        self.color = QtGui.QColor(self.field.value)

        self.colorbtn = QtGui.QPushButton('', self)
        self.colorbtn.setMaximumSize(QtCore.QSize(20, 20))
        self.connect(self.colorbtn, QtCore.SIGNAL('clicked()'), self.popColorDialog)

        self.textbox = QtGui.QLineEdit(self)
        self.textbox.setText(self.color.name())
        self.textbox.setObjectName("textbox")
        self.connect(self.textbox, QtCore.SIGNAL('editingFinished()'), self.applyTextBoxColor)

        self.hbox.addWidget(self.colorbtn)
        self.hbox.addWidget(self.textbox)
        # self.hbox.addStretch(10)
        self.hbox.addWidget(self.activeBox)

        # set the control to the initial colour
        self.updateColor()
        
        if not self.active:
            self.setActive(self.active)

    def updateColor(self):
        self.colorbtn.setStyleSheet(
            "QPushButton { background-color: %s }"
            "QPushButton:pressed { background-color: %s }" % (self.color.name(), self.color.light(125).name())
        )
        # update the textbox
        self.textbox.setText(self.color.name())
        self.field.value = self.color.name()
        self.emit(QtCore.SIGNAL('controlChanged()'))

    def popColorDialog(self):
        self.color = QtGui.QColorDialog.getColor(self.color)
        self.updateColor()

    def applyTextBoxColor(self):
        color = QtGui.QColor(self.textbox.displayText())
        self.color = color
        self.updateColor()

    def setValue(self, color):
        # TODO: Validate input so that the color value doesn't reset;
        # or maybe parse the value before passing it to QColor.setNamedValue()
        self.color = QtGui.QColor(color)
        self.updateColor()

    def getValue(self):
        return self.field.value
    
    def setActive(self, state):
        self.active = self.field.active = bool(state)
        self.activeBox.setChecked(self.active)
        self.label.setEnabled(self.active)
        self.textbox.setEnabled(self.active)
        self.colorbtn.setEnabled(self.active)

def createControlFromField(field, parent=None, w=250, h=36):
    control = None
    if field.type == TOGGLE:
        control = ToggleControl(field, parent, width=w, height=h)
    elif field.type == COLOR:
        control = ColorChooserControl(field, parent, width=w, height=h)
    elif field.type == NUMBER:
        control = NumberControl(field, parent, width=w, height=h)
    elif field.type == CHOICE:
        control = ChoiceControl(field, parent, width=w, height=h)
    else:
        print 'Wrong field type: '
        print field.type
    return control

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    #win = QtGui.QWidget()

    container1 = QtGui.QWidget()
    box = QtGui.QVBoxLayout(container1)
    box.addWidget(ColorChooserControl(name='color1'))
    box.addWidget(NumberControl(name='number1'))
    box.addWidget(ColorChooserControl(name='color2'))
    box.addWidget(ColorChooserControl(name='color3'))

    container2 = QtGui.QWidget()
    box2 = QtGui.QVBoxLayout(container2)
    box2.addWidget(ColorChooserControl(name='color4'))
    box2.addWidget(NumberControl(name='number2'))
    box2.addWidget(ColorChooserControl(name='color5'))
    box2.addWidget(ColorChooserControl(name='color6'))
    #height = 40 * box.count()

    toolbox = QtGui.QToolBox()
    toolbox.addItem(container1, 'one')
    toolbox.addItem(container2, 'two')
##    toolbox.addItem(ColorChooserControl(name='color4'), 'one')
##    toolbox.addItem(ColorChooserControl(name='color5'), 'two')
    toolbox.show()
    #win.resize(400,600)
    #win.show()

    sys.exit(app.exec_())

