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
from PyQt4 import QtGui, QtCore
from defaults import UNITS, COLOR, TOGGLE, NUMBER, CHOICE


class Control(QtGui.QWidget):
    '''A Control is a GUI representation of a Field instance.'''
    def __init__(self, field, parent=None, width=250, height=56):
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
        self.hboxwidget.setGeometry(QtCore.QRect(110, 0, 220, self.height))
        self.hbox = QtGui.QHBoxLayout(self.hboxwidget)

        self.label = QtGui.QLabel(self.longname, self)
        self.label.setGeometry(QtCore.QRect(0, 0, self.width, self.height))
        self.label.setAlignment(QtCore.Qt.AlignRight|
                                QtCore.Qt.AlignVCenter)
        self.label.setGeometry(0, 0, 110, self.height)
        self.label.setFont(QtGui.QFont('Lucida Grande', 8))

        self.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, 
                                             QtGui.QSizePolicy.Preferred))
        # create the 'active' checkbox
        self.activebox = QtGui.QCheckBox('', self)
        self.activebox.setChecked(True)
        self.connect(self.activebox, 
                     QtCore.SIGNAL('stateChanged(int)'), 
                     self.set_active)       
        if self.field.always_active:
            self.activebox.setVisible(False)
        # self.set_active(self.active)
        # TODO: tooltip

    def is_active(self):
        return self.active
    def set_active(self, state):
        self.active = self.field.active = bool(state)

    def set_value(self, value):
        pass    
    def get_value(self):
        pass

    def enterEvent(self, ev):
        self.emit(QtCore.SIGNAL('fieldEnter(PyQt_PyObject)'), self)
    def leaveEvent(self, ev):
        self.emit(QtCore.SIGNAL('fieldLeave(PyQt_PyObject)'), self)


class ToggleControl(Control):
    '''A Toggle control contains a checkbox, and represents a TOGGLE field.'''
    def __init__(self, *args, **kwargs):
        Control.__init__(self, *args, **kwargs)

        self.value = self.field.value

        self.checkbox = QtGui.QCheckBox('', self)
        self.checkbox.setChecked(self.value)
        self.connect(self.checkbox, 
                     QtCore.SIGNAL('stateChanged(int)'), 
                     self.set_value)
        self.hbox.addWidget(self.checkbox)
        self.hbox.addStretch()
        self.hbox.addWidget(self.activebox)

        if not self.active:
            self.set_active(self.active)
            self.activebox.setChecked(self.active)

    def set_value(self, value):
        self.value = self.field.value = bool(value)
        self.emit(QtCore.SIGNAL('controlChanged()'))
    
    def set_active(self, state):
        self.active = self.field.active = bool(state)
        self.label.setEnabled(self.active)
        self.checkbox.setEnabled(self.active)

    def get_value(self):
        return self.value

class ChoiceControl(Control):
    '''A Choice control creates a combo box, and represents a CHOICE field.'''
    def __init__(self, *args, **kwargs):
        Control.__init__(self, *args, **kwargs)
        self.choices = self.field.choices
        self.value = str(self.field.value)
        self.choicebox = QtGui.QComboBox(self)
        self.choicebox.addItems(self.choices)
        # select the specified value
        self.choicebox.setCurrentIndex(self.choicebox.findText(self.value))
        self.connect(self.choicebox, 
                     QtCore.SIGNAL('activated(int)'), 
                     self.set_value)
        self.hbox.addWidget(self.choicebox)
        self.hbox.addStretch()
        self.hbox.addWidget(self.activebox)
        if not self.active:
            self.set_active(self.active)
            self.activebox.setChecked(self.active)

    def set_value(self, index):
        self.value = self.field.value = self.choicebox.itemText(index)
        self.emit(QtCore.SIGNAL('controlChanged()'))
        # self.choicebox.setCurrentIndex(self.choicebox.findText(self.value))

    def get_value(self):
        return self.value

    def update_value(self):
        # updates stored values according to user interaction
        self.value = self.field.value = self.choicebox.currentText()
        
    def set_active(self, state):
        self.active = self.field.active = bool(state)
        self.label.setEnabled(self.active)
        self.choicebox.setEnabled(self.active)


class NumberControl(Control):
    '''A number control contains a slider and a spin box, and represents
    a NUMBER field.
    
    It creates a DoubleSpinBox behind the scenes in case the Field has 
    decimal values, and has some hacks to make the slider behave accordingly.'''
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
        coef = pow(10, self.decimals)
        self.slider.setRange(self.min * coef, self.max * coef)
        self.slider.setSingleStep(self.increment)

        # set widgets to initial value before connecting
        self.set_value(self.value)
        # and now connect the signals
        self.connect(self.slider, 
                     QtCore.SIGNAL('sliderReleased()'), 
                     self.set_value_from_slider)
        self.connect(self.slider, 
                     QtCore.SIGNAL('valueChanged(int)'), 
                     self.update_numberbox_from_slider)
        if self.floating:
            self.connect(self.numberbox, 
                         QtCore.SIGNAL('valueChanged(double)'), 
                         self.set_value)
        else:
            self.connect(self.numberbox, 
                         QtCore.SIGNAL('valueChanged(int)'), 
                         self.set_value)
        self.hbox.addWidget(self.slider)
        self.hbox.addWidget(self.numberbox)
        self.hbox.addWidget(self.activebox)

        if self.field.unit:
            self.unit_combobox = QtGui.QComboBox(self)
            self.unit_combobox.addItems(UNITS)
            # select the specified unit
            current_unit = self.unit_combobox.findText(self.field.unit)
            self.unit_combobox.setCurrentIndex(current_unit)
            self.unit_combobox.connect(self.unit_combobox, 
                                      QtCore.SIGNAL('activated(int)'), 
                                      self.set_unit)
            self.hbox.insertWidget(2, self.unit_combobox)

        if not self.active:
            self.set_active(self.active)
            self.activebox.setChecked(self.active)

    def set_unit(self, index):
        self.unit = self.field.unit = self.unit_combobox.itemText(index)

    def set_value(self, value):
        self.value = self.field.value = value
        self.slider.setValue(value * pow(10, self.decimals))
        self.numberbox.setValue(value)
        self.emit(QtCore.SIGNAL('controlChanged()'))

    def set_value_from_slider(self):
        value = self.slider.value() / pow(10, self.decimals)
        self.set_value(value)
        
    def update_numberbox_from_slider(self, val):
        value = val / pow(10, self.decimals)
        # quick hack to prevent numberbox to sending the valueChanged
        # signal
        self.disconnect(self.numberbox, 
                        QtCore.SIGNAL('valueChanged(double)'), 
                        self.set_value)
        self.disconnect(self.numberbox, 
                        QtCore.SIGNAL('valueChanged(int)'), 
                        self.set_value)
        self.numberbox.setValue(value)
        if self.floating:
            self.connect(self.numberbox, 
                         QtCore.SIGNAL('valueChanged(double)'), 
                         self.set_value)
        else:
            self.connect(self.numberbox, 
                         QtCore.SIGNAL('valueChanged(int)'), 
                         self.set_value)
    def get_value(self):
        return self.value
    
    def set_active(self, state):
        self.active = self.field.active = bool(state)
        self.label.setEnabled(self.active)
        self.numberbox.setEnabled(self.active)
        if self.field.unit:
            self.unit_combobox.setEnabled(self.active)
        self.slider.setEnabled(self.active)

class ColorChooserControl(Control):
    '''A color chooser control creates a text box where color values can be
    input, along with a colored button that reflects the currently set color.
    
    The button, when clicked, pops up the OS-specific color chooser dialog.
    
    The textbox accepts colors in hex format, as well as X11 color names --
    see http://en.wikipedia.org/wiki/Web_colors#X11_color_names) for a
    complete list.'''
    def __init__(self, *args, **kwargs):
        Control.__init__(self, *args, **kwargs)

        self.color = QtGui.QColor(self.field.value)

        self.colorbutton = QtGui.QPushButton('', self)
        self.colorbutton.setMaximumSize(QtCore.QSize(20, 20))
        self.connect(self.colorbutton, 
                     QtCore.SIGNAL('clicked()'), 
                     self.show_color_dialog)
        self.textbox = QtGui.QLineEdit(self)
        self.textbox.setText(self.color.name())
        self.textbox.setObjectName("textbox")
        self.connect(self.textbox, 
                     QtCore.SIGNAL('editingFinished()'), 
                     self.apply_textbox_color)
        self.hbox.addWidget(self.colorbutton)
        self.hbox.addWidget(self.textbox)
        # self.hbox.addStretch(10)
        self.hbox.addWidget(self.activebox)

        # set the control to the initial colour
        self.update_color()
        
        if not self.active:
            self.set_active(self.active)

    def update_color(self):
        self.colorbutton.setStyleSheet(
            "QPushButton { background-color: %s }"
            "QPushButton:pressed { background-color: %s }" 
            % (self.color.name(), self.color.light(125).name())
        )
        # update the textbox
        self.textbox.setText(self.color.name())
        self.field.value = self.color.name()
        self.emit(QtCore.SIGNAL('controlChanged()'))

    def show_color_dialog(self):
        self.color = QtGui.QColorDialog.getColor(self.color)
        self.update_color()

    def apply_textbox_color(self):
        color = QtGui.QColor(self.textbox.displayText())
        self.color = color
        self.update_color()

    def set_value(self, color):
        # TODO: Validate input so that the color value doesn't reset;
        # or maybe parse the value before passing it to QColor.setNamedValue()
        self.color = QtGui.QColor(color)
        self.update_color()

    def get_value(self):
        return self.field.value
    
    def set_active(self, state):
        self.active = self.field.active = bool(state)
        self.activebox.setChecked(self.active)
        self.label.setEnabled(self.active)
        self.textbox.setEnabled(self.active)
        self.colorbutton.setEnabled(self.active)

def create_control_from_field(field, parent=None, width=250, height=36):
    '''Given a Field instance, an appropriate Control instance is returned.'''
    control = None
    if field.type == TOGGLE:
        control = ToggleControl(field, parent, 
                                width=width, height=height)
    elif field.type == COLOR:
        control = ColorChooserControl(field, parent, 
                                      width=width, height=height)
    elif field.type == NUMBER:
        control = NumberControl(field, parent, 
                                width=width, height=height)
    elif field.type == CHOICE:
        control = ChoiceControl(field, parent, 
                                width=width, height=height)
    else:
        print 'Wrong field type: '
        print field.type
    return control

