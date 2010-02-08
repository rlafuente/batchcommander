#!/usr/bin/env python

# This file is part of the Batch Commander application.
#
#   copyright (C) 2009 by Ricardo Lafuente
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
'''Batch Commander console launcher'''

import os
from batchcommander import BatchCommander

if __name__ == '__main__':
    
    import sys
    if sys.platform == 'linux2':
        homedir = os.path.expanduser("~")
        localdir = os.path.join(homedir, '.batchcommander/')
        datadir = os.path.join(localdir, 'datafiles/')
        examplesdir = os.path.join(localdir, 'examples/')
    elif sys.platform == 'darwin':
        homedir = os.path.expanduser("~")
        localdir = os.path.join(homedir, 'Documents', 'BatchCommander/')
        datadir = os.path.join(localdir, 'DataFiles/')
        examplesdir = os.path.join(localdir, 'Examples/')
        # have the files be output to the desktop in OSX
        homedir = os.path.join(homedir, 'Desktop/')

    DEFAULT_INPUTFILE = os.path.join(examplesdir, 'sarovar.tex')
    DEFAULT_SCRIPTFILE = os.path.join(examplesdir, 'river_valley.sty')
    DEFAULT_OUTPUTFILE = os.path.join(homedir, 'output.pdf')
    # FIXME: the pdf output name is not applied, outputfile not considered
    DEFAULT_COMMAND = 'pdflatex -halt-on-error %(input_file)s %(output_file)s'
    DEFAULT_IMMEDIATE_MODE = False
    
    DEFAULT_DATAFILES_DIR = datadir
    DEFAULT_DATAFILES = []

    for result in os.walk(DEFAULT_DATAFILES_DIR):
        directory, dirs, files = result
        for filename in files:
            if os.path.splitext(filename)[1] == '.data':
                filepath = os.path.join(directory, filename)
                DEFAULT_DATAFILES.append(filepath)

    bc = BatchCommander(datafiles=DEFAULT_DATAFILES,
                        inputfile=DEFAULT_INPUTFILE,
                        scriptfile=DEFAULT_SCRIPTFILE,
                        outputfile=DEFAULT_OUTPUTFILE,
                        command=DEFAULT_COMMAND,
                        immediate_mode=DEFAULT_IMMEDIATE_MODE,
                        output_mode='tex',
                        )
    bc.show_ui()
