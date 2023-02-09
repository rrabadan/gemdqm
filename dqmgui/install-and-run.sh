#! /bin/bash

ARCH=slc7_amd64_gcc630
VER=HG2302a

cd $WDIR
mkdir $WDIR/Gui
cd $WDIR/Gui

git clone https://github.com/dmwm/deployment.git

cd $WDIR/Gui/deployment
git reset --hard $VER

cat $WDIR/dqmgui/workspaces-gem.py >> $WDIR/Gui/deployment/dqmgui/workspaces-online.py
cp -v $WDIR/dqmgui/gemtestbeam-layouts.py $WDIR/Gui/deployment/dqmgui/layouts
cp -v $WDIR/dqmgui/ge21qc8-layouts.py $WDIR/Gui/deployment/dqmgui/layouts

cd $WDIR/Gui

$WDIR/Gui/deployment/Deploy -A $ARCH -r "comp=comp" -R comp@$VER -t MYDEV -s "prep sw post" $WDIR/Gui dqmgui/bare

sed -i -e '/export keytab/,+7 s/^/## /' current/config/dqmgui/manage
sed -i -e 's/127.0.0.1/collector/g' current/config/dqmgui/server-conf-online.py

$PWD/current/config/dqmgui/manage -f online start "I did read documentation"

cd $WDIR

su cmsusr -s /bin/bash "$@"
