#!/usr/bin/env python

# updateDatafile.py is copyright (C) 2009 by Ricardo Lafuente
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
'''Command-line tool for converting legacy .data files to the new YAML format'''

import sys

INPUTFILE = sys.argv[1]
##if len(sys.argv) == 3:
##    OUTPUTFILE = open(sys.argv[2], 'w')
##else:
OUTPUTFILE = sys.stdout

KEYS = ['name', 'longname', 'type', 'output', 'position', 'unit', 'min',
        'max', 'choices', 'value', 'increment', 'decimals']
MANDATORY_KEYS = ['longname', 'type', 'value']
ADDITIONAL_KEYS = ['unit', 'min', 'max', 'increment', 'decimals', 'choices']


def parseFieldLine(line):
    values = line.strip().split('\t')
    fieldproperties = {}
    for i in range(len(KEYS)):
        value = None
        # if there's missing fields, pass and warn
        try:
            if values[i] != '-':
                value = values[i]
        except IndexError:
            # print 'Warning: Field has missing values'
            pass
        fieldproperties[KEYS[i]] = value
    # strip quotes from longname and choices
    fieldproperties['longname'] = fieldproperties['longname'].strip('"')
    fieldproperties['value'] = fieldproperties['value'].strip('"')
    if fieldproperties['choices']:
        fieldproperties['choices'] = fieldproperties['choices'].strip('"')
    # 'choice_color' type should be just 'color'
    if fieldproperties['type'] == 'choice_color':
        fieldproperties['type'] = 'color'
    # make types lowercase
    fieldproperties['type'] = fieldproperties['type'].lower()
    return fieldproperties

def generateYAML():
    lines = open(INPUTFILE, 'r').readlines()
    if '\r' in lines[0]:
        # oh no, wrong carriage returns, let's fix that
        lines = lines[0].split('\r')

    file = OUTPUTFILE
    for line in lines:
        if line.startswith('\tthe_name'):
            # first line, ignore it
            pass
        elif line.startswith('=='):
            # end of section
            file.write('\n')
        elif not line.startswith('\t'):
            # beginning of section
            file.write(line.strip() + ':\n')
        elif line.startswith('\n'):
            # single newline
            pass
        elif line.startswith('\t'):
            # field row, let's parse it hard
            values = parseFieldLine(line)
            file.write('    - %s:\n' % values['name'])
            for item in MANDATORY_KEYS:
                file.write('        %s: %s\n' % (item, values[item]))
            for item in ADDITIONAL_KEYS:
                if values[item] is not None:
                    file.write('        %s: %s\n' % (item, values[item]))
        else:
            file.write('OH NOES: ' + line)

    file.close()

generateYAML()
