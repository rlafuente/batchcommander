from setuptools import setup

setup(
      name='Batch Commander',
      app=['bin/bcommander.py'],
      options={
        "py2app": {
          'argv_emulation': True,
          'includes': [
            "sip",
            "PyQt4", "PyQt4.QtCore", "PyQt4.QtGui", "PyQt4.QtXml",
            "yaml",
            "QtPoppler",
            ],
            'excludes': ['PyQt4.QtDesigner', 'PyQt4.QtNetwork', 
              'PyQt4.QtOpenGL', 'PyQt4.QtScript', 'PyQt4.QtSql', 
              'PyQt4.QtTest', 'PyQt4.QtWebKit', 
              'PyQt4.phonon'],
        }
      },
      setup_requires = ["py2app"],
      packages = ['batchcommander']
      )

