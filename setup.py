from distutils.core import setup
import os
# import py2exe

try:
    from win32com.shell import shellcon, shell            
    homedir = shell.SHGetFolderPath(0, shellcon.CSIDL_APPDATA, 0, 0) 
except ImportError: # quick semi-nasty fallback for non-windows/win32com case
    homedir = os.path.expanduser("~")

local = os.path.join(homedir, '.batchcommander/')
print local

# this will work someday
datafiles = []
datafiles.extend([(os.path.join('local', root) ,[os.path.join(root, file_)
for file_ in files]) for root,dir,files in os.walk('datafiles')])

setup(name="batchcommander",
      version="0.1",
      author="Ricardo Lafuente",
      author_email="r@sollec.org",
      url="http://bitbucket.org/rlafuente/batchcommander",
      license="GNU General Public License (GPL)",
      packages=['batchcommander'],
#      data_files = datafiles,
      scripts=["bin/batchcommander"],
#      windows=[{"script": "bin/batchcommander"}],
#      options={"py2exe": {"skip_archive": True, "includes": ["sip"]}}
      )

