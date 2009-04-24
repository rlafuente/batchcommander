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

import yaml
import sys
from defaults import *

class Section:
    # this class represents a section which contains one or more
    # Field instances
    def __init__(self, name):
        self.name = name
        self.fields = []

    def add(self, field):
        self.fields.append(field)

    def findFieldByName(self, name):
        result = None
        for field in self.fields:
            if field.name == name:
                result = field
                break
        return result

    def dump(self, file=sys.stdout):
        file.write('%s:\n' % self.name)
        for field in self.fields:
            field.dump(file)
            file.write('\n')

    def styleOutput(self, file=sys.stdout):
        file.write('%% --------------  %s  --------------\n' % self.name)
        for field in self.fields:
            if field.active:
                file.write(field.styleOutput())

class Field:
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

    def dump(self, file=sys.stdout):
        # dump yaml representation
        file.writelines(['    - %s:\n' % self.name,
                        '        longname: %s\n' % self.longname,
                        '        type: %s\n' % self.type,
                        '        value: %s\n' % self.value,
        ])
        if self.type == TOGGLE or self.type == COLOR:
            pass
        elif self.type == CHOICE:
            file.write('        choices: ' + ', '.join(self.choices) + '\n')
        elif self.type == NUMBER:
            file.write('        min: %i\n' % self.min)
            file.write('        max: %i\n' % self.max)
            file.write('        increment: %i\n' % self.increment)
            if self.decimals:
                file.write('        decimals: %i\n' % self.decimals)
            if self.unit:
                file.write('        unit: %s\n' % self.unit)

    def styleOutput(self):
        ''' Output a TeX style file command '''
        value = self.value
        cmd = ' ' * 18
        cmd += '\\'
        if self.type == 'toggle':
            if self.value:
                cmd += self.name
        else:
            cmd += self.name + '=' + str(value)
        if self.unit:
            cmd += self.unit
        cmd += '\n'
        return cmd

def parse_datafile(datafilename):
    # reads a YAML-formatted datafile and returns a dictionary
    datafile = open(datafilename, 'r')
    datadict = yaml.load(datafile)
    return datadict

def generate_fields(datadict):
    # Accepts a datadict and returns a list of Section instances
    section_list = []
    for section in datadict:
        s = Section(section)
        fields = datadict[section]
        for item in fields:
            # some twisting to sort through the py-yaml ordered
            # mapping implementation, which is one-key dicts inside
            # a list
            fieldname = item.keys()[0]
            properties = item[fieldname]
            c = Field(fieldname, properties)
            s.add(c)
        section_list.append(s)
    return section_list

def dumpSectionList(sectionList, file=sys.stdout):
    for section in sectionList:
        section.dump(file)

if __name__ == '__main__':
    # read file specified in stdin and print structure to stdout
    datafilename = sys.argv[1]
    datadict = parse_datafile(datafilename)
    sectionList = generate_fields(datadict)
    dumpSectionList(sectionList)

    '''
    for section in generate_fields(datadict):
        print section.name
        for field in section.fields:
            field.dump()
    '''
