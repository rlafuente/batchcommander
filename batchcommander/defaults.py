import os

UNITS = ['cm', 'mm', 'in', 'pt']

TOGGLE = 'toggle'
COLOR = 'color'
NUMBER = 'number'
CHOICE = 'choice'

MODE_TEX = 'tex'
MODE_PYTHON = 'python' 

# TODO: windows version
homedir = os.path.expanduser("~")
localdir = os.path.join(homedir, '.batchcommander/')
datadir = os.path.join(localdir, 'datafiles/')
examplesdir = os.path.join(localdir, 'examples/')
print homedir
print localdir
print datadir
print examplesdir

DEFAULT_INPUTFILE = os.path.join(examplesdir, 'sarovar.tex')
DEFAULT_SCRIPTFILE = os.path.join(examplesdir, 'river_valley.sty')
DEFAULT_OUTPUTFILE = os.path.join(homedir, 'output.pdf')
DEFAULT_DATAFILES_DIR = '../src/datafiles'
DEFAULT_DATAFILES = []
# FIXME: the pdf output name is not applied, outputfile not considered
DEFAULT_COMMAND = 'pdflatex -halt-on-error %(input_file)s %(output_file)s'
DEFAULT_IMMEDIATE_MODE = True

MAINBOXWIDTH = 370
MAINBOXHEIGHT = 200
FIELDHEIGHT = 36
FIELDWIDTH = 375
       
