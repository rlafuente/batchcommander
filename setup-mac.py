from setuptools import setup
import os

setup(
      name='Batch Commander',
      app=['bin/bcommander.py'],
      options={
        "py2app": {
          'argv_emulation': True,
          'includes': [
            "sip",
            "PyQt4._qt",
            "yaml",
            ]
        }
      },
      setup_requires = ["py2app"],
      packages = ['batchcommander']
      )

