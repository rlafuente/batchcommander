from distutils.core import setup
import py2exe

setup(name="batchcommander",
      version="0.1",
      author="Ricardo Lafuente",
      author_email="r@sollec.org",
      url="http://bitbucket.org/rlafuente/batchcommander",
      license="GNU General Public License (GPL)",
      packages=['batchbommander'],
      package_data={"batchbommander": ["datafiles/*"]},
      scripts=["bin/batchcommander"],
      windows=[{"script": "bin/batchcommander"}],
      options={"py2exe": {"skip_archive": True, "includes": ["sip"]}})

