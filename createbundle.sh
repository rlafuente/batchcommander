#!/bin/bash
# script for creating the Batch Commander app bundle

DMG_FILE=~/Desktop/BatchCommander.dmg


echo ' *** Deleting build and dist dirs... *** '
rm -fr dist build
echo ' *** Running py2app... *** '
python setup-mac.py py2app --resources datafiles --iconfile batch-icon.icns
echo ' *** Creating a dummy qt.conf... *** '
touch ./dist/Batch\ Commander.app/Contents/Resources/qt.conf
# DMG creation command taken from
# http://davidbau.com/archives/2005/10/18/izabella_icons_and_py2app.html
echo ' *** Compressing the app into a .dmg package... ***'
if [ -f $DMG_FILE ]; then
    rm $DMG_FILE
fi
hdiutil create -imagekey zlib-level=9 -srcfolder dist/Batch\ Commander.app $DMG_FILE
echo ' *** All done -- running Batch Commander! *** '
open dist/Batch\ Commander.app
