TARGET = QtPoppler.so
OFILES = sipQtPopplercmodule.o sipQtPopplerQList0101PopplerEmbeddedFile.o sipQtPopplerQList0100PopplerFontInfo.o sipQtPopplerQList0101PopplerTextBox.o sipQtPopplerPopplerDocument.o sipQtPopplerPopplerPage.o sipQtPopplerPopplerEmbeddedFile.o sipQtPopplerPopplerFontInfo.o sipQtPopplerPopplerTextBox.o sipQtPopplerPoppler.o
HFILES = sipAPIQtPoppler.h 

CC = gcc
CXX = g++
LINK = g++
CPPFLAGS = -DNDEBUG -DQT_NO_DEBUG -DQT_CORE_LIB -DQT_GUI_LIB -I. -I/usr/include/poppler -I/usr/include/qt4/ -I/usr/include/qt4/QtXml/ -I/usr/include/python2.6 -I/usr/share/qt4/mkspecs/linux-g++ -I/usr/include/qt4/QtCore -I/usr/include/qt4/QtGui -I/usr/include/qt4 -I/usr/X11R6/include
CFLAGS = -pipe -fPIC -Os -Wall -W -D_REENTRANT
CXXFLAGS = -pipe -fPIC -g -O2 -Os -Wall -W -D_REENTRANT
LFLAGS = -shared -Wl,-Bsymbolic-functions -Wl,-O1 -Wl,--version-script=QtPoppler.exp
LIBS = -L/usr/lib -L/usr/X11R6/lib -lpoppler-qt4 -lQtCore -lQtGui
MOC = moc-qt4
.SUFFIXES: .c .o .cpp .cc .cxx .C


.cpp.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cc.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cxx.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.C.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.c.o:
	$(CC) -c $(CFLAGS) $(CPPFLAGS) -o $@ $<

all: $(TARGET)

$(OFILES): $(HFILES)

$(TARGET): $(OFILES)
	@echo '{ global: initQtPoppler; local: *; };' > QtPoppler.exp
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/usr/lib/python2.6/dist-packages || mkdir -p $(DESTDIR)/usr/lib/python2.6/dist-packages
	cp -f $(TARGET) $(DESTDIR)/usr/lib/python2.6/dist-packages/$(TARGET)
	@test -d $(DESTDIR)/usr/share/sip/QtPoppler || mkdir -p $(DESTDIR)/usr/share/sip/QtPoppler
	cp -f poppler-qt4.sip $(DESTDIR)/usr/share/sip/QtPoppler/poppler-qt4.sip
	@test -d $(DESTDIR)/usr/lib/python2.6/dist-packages || mkdir -p $(DESTDIR)/usr/lib/python2.6/dist-packages
	cp -f pypopplerqt4config.py $(DESTDIR)/usr/lib/python2.6/dist-packages/pypopplerqt4config.py

clean:
	-rm -f $(TARGET)
	-rm -f sipQtPopplercmodule.o
	-rm -f sipQtPopplerQList0101PopplerEmbeddedFile.o
	-rm -f sipQtPopplerQList0100PopplerFontInfo.o
	-rm -f sipQtPopplerQList0101PopplerTextBox.o
	-rm -f sipQtPopplerPopplerDocument.o
	-rm -f sipQtPopplerPopplerPage.o
	-rm -f sipQtPopplerPopplerEmbeddedFile.o
	-rm -f sipQtPopplerPopplerFontInfo.o
	-rm -f sipQtPopplerPopplerTextBox.o
	-rm -f sipQtPopplerPoppler.o
	-rm -f QtPoppler.exp
