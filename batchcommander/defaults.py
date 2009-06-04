UNITS = ['cm', 'mm', 'in', 'pt']

TOGGLE = 'toggle'
COLOR = 'color'
NUMBER = 'number'
CHOICE = 'choice'

MODE_TEX = 'tex'
MODE_PYTHON = 'python' 

DEFAULT_INPUTFILE = './sarovar.tex'
DEFAULT_SCRIPTFILE = './river_valley.sty'
DEFAULT_OUTPUTFILE = './output.pdf'
DEFAULT_DATAFILES_DIR = '../src/datafiles'
DEFAULT_DATAFILES = []
# FIXME: the pdf output name is not applied, outputfile not considered
DEFAULT_COMMAND = 'pdflatex -halt-on-error %(input_file)s %(output_file)s'
DEFAULT_IMMEDIATE_MODE = True

MAINBOXWIDTH = 370
MAINBOXHEIGHT = 200
FIELDHEIGHT = 36
FIELDWIDTH = 375
       
