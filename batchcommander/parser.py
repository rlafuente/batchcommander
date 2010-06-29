#!/usr/bin/env python

# parser.py is copyright (C) 2009 by Ricardo Lafuente
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
'''YAML datafile parser for Batch Commander'''

import sys, os
import yaml
from defaults import TOGGLE, COLOR, NUMBER, CHOICE

class DataSet:
    '''Represents the contents of a .data file.
    Accepts a file path and generates a list of sections, accessible
    through Dataset.sections .'''
    def __init__(self, filepath):
        self.name = os.path.basename(filepath)
        self.path = filepath
        # log.info('Loading dataset from ' + self.name + ' ...')
        datadict = parse_datafile(self.path)
        self.sections = generate_fields(datadict)
        self.widget = None
        self.active = False
        
    def __str__(self):
        return self.name

class Section:
    '''A group of Field instances.'''
    def __init__(self, name):
        self.name = name
        self.fields = []

    def add(self, field):
        '''Add a field to this section.'''
        self.fields.append(field)

    def find_field_by_name(self, name):
        '''Returns the field instance whose name matches the input string.'''
        result = None
        for field in self.fields:
            if field.name == name:
                result = field
                break
        return result

    def output_texstyle(self, outfile=sys.stdout):
        '''Returns strings representing TeX style file commands for all fields
        in this section.'''
        outfile.write('%% --------------  %s  --------------\n' % self.name)
        for field in self.fields:
            if field.active:
                outfile.write(field.output_texstyle())
                
    def output_pythonvar(self, outfile=sys.stdout):
        '''Returns strings representing Python variable declarations for all 
        fields in this section.'''
        for field in self.fields:
            if field.active:
                outfile.write(field.output_pythonvar())

    def dump(self, outfile=sys.stdout):
        '''Writes a YAML representation of all the fields in this section 
        into a file.'''
        outfile.write('%s:\n' % self.name)
        for field in self.fields:
            field.dump(outfile)
            outfile.write('\n')

class Field:
    '''Represents a named entity with a variable value, along with
    other properties.'''
    def __init__(self, name, propdict, active=True):
        self.name = name
        self.longname = name
        self.active = active

        if propdict.has_key('longname'):
            self.longname = propdict['longname']

        self.decimals = self.unit = self.choices = None

        self.type = propdict['type']
        # set type-specific attributes for this field
        if self.type == TOGGLE or self.type == COLOR:
            pass
        elif self.type == CHOICE:
            self.choices = []
            for choice in propdict['choices'].split(','):
                self.choices.append(choice.strip())
        elif self.type == NUMBER:
            self.min = propdict['min']
            self.max = propdict['max']
            self.increment = propdict['increment']
            if propdict.has_key('decimals'):
                self.decimals = propdict['decimals']
            if propdict.has_key('unit'):
                self.unit = propdict['unit']
        self.value = propdict['value']
        if propdict.has_key('active'):
            self.active = propdict['active']
        self.always_active = False
        if propdict.has_key('always_active'):
            self.always_active = propdict['always_active']

    def output_texstyle(self):
        '''Returns a string representing a TeX style file command.'''
        value = self.value
        if self.type == TOGGLE:
            if self.value:
                cmd = ' ' * 18
                cmd += '\\'
                cmd += self.name
                cmd += '\n'
                return cmd
        else:
            cmd = ' ' * 18
            cmd += '\\'
            if self.decimals:
                val = str(value)
            else:
                val = str(int(value))
            cmd += self.name + '=' + val
            if self.unit:
                cmd += self.unit
            cmd += '\n'
            return cmd
        return ''
        
    def output_pythonvar(self):
        '''Returns a string representing a Python variable declaration.'''
        if self.type == COLOR:
            value = "'" + str(self.value) + "'"
        else:
            value = str(self.value)
        cmd = self.name + ' = ' + value + '\n'
        return cmd

    def dump(self, outfile=sys.stdout):
        ''' Write a YAML representation of the Field data into a file.
        Useful for re-generating .data files.'''
        outfile.writelines(['    - %s:\n' % self.name,
                            '        longname: %s\n' % self.longname,
                            '        type: %s\n' % self.type,
                            '        value: %s\n' % self.value,
        ])
        if self.type == TOGGLE or self.type == COLOR:
            pass
        elif self.type == CHOICE:
            outfile.write(  '        choices: ' + ', '.join(self.choices) + '\n')
        elif self.type == NUMBER:
            outfile.write(  '        min: %i\n' % self.min)
            outfile.write(  '        max: %i\n' % self.max)
            outfile.write(  '        increment: %i\n' % self.increment)
            if self.decimals:
                outfile.write('        decimals: %i\n' % self.decimals)
            if self.unit:
                outfile.write('        unit: %s\n' % self.unit)

def parse_datafile(datafilename):
    '''Reads a YAML-formatted datafile and returns a dictionary'''
    datafile = open(datafilename, 'r')
    datadict = yaml.load(datafile)
    return datadict

def generate_fields(datadict):
    '''Accepts a datadict and returns a list of Section instances.
    Should be fed the output of the parse_datafile function.'''
    section_list = []
    for section_key in datadict:
        section = Section(section_key)
        fields = datadict[section_key]
        for item in fields:
            # some twisting to sort through the py-yaml ordered
            # mapping implementation, which is one-key dicts inside
            # a list
            fieldname = item.keys()[0]
            properties = item[fieldname]
            field = Field(fieldname, properties)
            section.add(field)
        section_list.append(section)
    return section_list

"""
if __name__ == '__main__':
    '''Read the file specified in stdin and print structure to stdout'''
    filename = sys.argv[1]
    data = parse_datafile(filename)
    sections = generate_fields(data)
    for section in sections:
        section.dump()
"""
