from distutils.core import setup
import os
# import py2exe

# windows install is not yet ready, but this is here for when i code the rest
try:
    from win32com.shell import shellcon, shell            
    homedir = shell.SHGetFolderPath(0, shellcon.CSIDL_APPDATA, 0, 0) 
except ImportError: # quick semi-nasty fallback for non-windows/win32com case
    homedir = os.path.expanduser("~")

localdir = os.path.join(homedir, '.batchcommander/')

# copy datafiles to ~/.batchcommander
# datafile globbing-fu taken from Mercurial's setup.py script
datafiles = []
datafiles.extend([(os.path.join(localdir, root) ,[os.path.join(root, file_)
for file_ in files]) for root,dir,files in os.walk('datafiles')])
datafiles.extend([(os.path.join(localdir, root) ,[os.path.join(root, file_)
for file_ in files]) for root,dir,files in os.walk('examples')])

# do it
setup(name="batchcommander",
      version="0.1",
      author="Ricardo Lafuente",
      author_email="r@sollec.org",
      url="http://bitbucket.org/rlafuente/batchcommander",
      license="GNU General Public License (GPL)",
      packages=['batchcommander'],
      data_files = datafiles,
      scripts=["bin/bcommander.py"],
#      windows=[{"script": "bin/batchcommander"}],
#      options={"py2exe": {"skip_archive": True, "includes": ["sip"]}}
      )

# hacky hacky post-install
# setup() makes the .batchcommander/ dir be owned by root,
# so we need to chown it to the user who ran the command

# get the user name
username = homedir.split('/')[-1]
# get uid and gid
import pwd
pw = pwd.getpwnam(username)
uid, gid = pw[2:4]
for root, dir, files in os.walk(localdir):
    os.chown(root, uid, gid)
    for f in files:
        filename = os.path.join(root, f)
        os.chown(filename, uid, gid)

