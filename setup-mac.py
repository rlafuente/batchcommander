from setuptools import setup
import sys, os

# add the Poppler-Qt Python bindings to the syspath
sys.path.insert(os.path.abspath('./qtpoppler/mac'))

setup(
      name='Batch Commander',
      app=['bin/bcommander.py'],
      options={
        "py2app": {
          'argv_emulation': True,
          'includes': [
            "sip",
            "PyQt4._qt",
            "QtPoppler",
            "yaml",
            ]
        }
      },
      setup_requires = ["py2app"],
      packages = ['batchcommander']
      )

