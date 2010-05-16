#!/bin/bash
# script for creating the Batch Commander app bundle

# good advice taken from
# http://stackoverflow.com/questions/96882/how-do-i-create-a-nice-looking-dmg-for-mac-os-x-using-command-line-tools
# http://davidbau.com/archives/2005/10/18/izabella_icons_and_py2app.html

dmg_filename=~/Desktop/BatchCommander.dmg
temp_dmg_filename=batchcommanderpackage.temp.dmg
sourcefolder=dist/Batch\ Commander.app
title=Batch\ Commander
applicationName=$title
backgroundPictureName=batch-dmg-background.png
temp_vol_name=/Volumes/"$title"
docs_dir=/Users/`whoami`/Documents

echo $docs_dir
echo ' *** Deleting build and dist dirs... *** '
rm -fr dist build
echo ' *** Running py2app... *** '
python setup-mac.py py2app --resources datafiles --iconfile batch-icon.icns
echo ' *** Creating a dummy qt.conf... *** '
touch ./dist/Batch\ Commander.app/Contents/Resources/qt.conf
echo ' *** Replacing __boot__.py... ***'
cp -f ./assets/__boot__.py dist/Batch\ Commander.app/Contents/Resources/
echo ' *** Compressing the app into a DMG image file... ***'
if [ -f $temp_dmg_filename ]; then
    rm $temp_dmg_filename
fi
if [ -f $dmg_filename ]; then
    rm $dmg_filename
fi
hdiutil create \
  -srcfolder "$sourcefolder" \
  -volname "${title}" -fs HFS+ -fsargs "-c c=64,a=16,e=16" -format UDRW \
  "$temp_dmg_filename"
echo ' *** Mounting the image file... *** '
device=$(hdiutil attach -readwrite -noverify -noautoopen "$temp_dmg_filename" | egrep '^/dev/' | sed 1q | awk '{print $1}')
echo ' *** Copying the DMG background image and datafiles... ***'
mkdir "$temp_vol_name"/.bg 
cp assets/$backgroundPictureName "$temp_vol_name"/.bg
mkdir "$temp_vol_name"/BatchCommander
cp -r datafiles "$temp_vol_name"/BatchCommander/DataFiles
cp -r examples "$temp_vol_name"/BatchCommander/Examples
echo ' *** Setting DMG metadata... ***'
echo '
   tell application "Finder"
     tell disk "'${title}'"
           open
           set current view of container window to icon view
           set toolbar visible of container window to false
           set statusbar visible of container window to false
           set the bounds of container window to {400, 100, 885, 525}
           set theViewOptions to the icon view options of container window
           set arrangement of theViewOptions to not arranged
           set icon size of theViewOptions to 72
           set background picture of theViewOptions to file ".bg:'${backgroundPictureName}'"
           make new alias file at container window to POSIX file "/Applications" with properties {name:"Applications"}
           set position of item "'${applicationName}'" of container window to {100, 100}
           set position of item "BatchCommander" of container window to {100, 300}
           set position of item "Applications" of container window to {375, 100}
           make new alias file at container window to POSIX file "'${docs_dir}'" with properties {name:"Documents"}
           set position of item "Documents" of container window to {375, 300}
           update without registering applications
           delay 5
           eject
     end tell
   end tell
' | osascript

echo " *** Wrapping up the DMG file... *** "
# chmod -Rf go-w /Volumes/"${title}"
sync
sync
# hdiutil detach ${device}
hdiutil convert $temp_dmg_filename -format UDZO -imagekey zlib-level=9 -o "${dmg_filename}"
rm -f $temp_dmg_filename


