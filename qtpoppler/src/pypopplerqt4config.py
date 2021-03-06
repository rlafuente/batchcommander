import pyqtconfig

# These are installation specific values created when Hello was configured.
# The following line will be replaced when this template is used to create
# the final configuration module.
_pkg_config = {
    'pypopplerqt4_sip_dir':    '/usr/share/sip',
    'pypopplerqt4_sip_flags':  '-x VendorID -t WS_X11 -x PyQt_NoPrintRangeBug -t Qt_4_6_2 -x Py_v3 -g'
}

_default_macros = None

class Configuration(pyqtconfig.Configuration):
    """The class that represents Hello configuration values.
    """
    def __init__(self, sub_cfg=None):
        """Initialise an instance of the class.

        sub_cfg is the list of sub-class configurations.  It should be None
        when called normally.
        """
        # This is all standard code to be copied verbatim except for the
        # name of the module containing the super-class.
        if sub_cfg:
            cfg = sub_cfg
        else:
            cfg = []

        cfg.append(_pkg_config)

        pyqtconfig.Configuration.__init__(self, cfg)

class HelloModuleMakefile(pyqtconfig.QtModuleMakefile):
    """The Makefile class for modules that %Import hello.
    """
    def finalise(self):
        """Finalise the macros.
        """
        # Make sure our C++ library is linked.
        self.extra_libs.append("QtPoppler")

        # Let the super-class do what it needs to.
        pyqtconfig.QtModuleMakefile.finalise(self)