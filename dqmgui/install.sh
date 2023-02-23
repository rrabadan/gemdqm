#! /bin/bash

ARCH=slc7_amd64_gcc630
VER=HG2302a

if [ -z "$MY_UID" ]; then
    MY_UID=$(id -u cmsusr)
    echo "MY_UID variable not specified, defaulting to cmsusr user id ($MY_UID)"
fi

if [ -z "$MY_GID" ]; then
    MY_GID=$(id -g cmsusr)
    echo "MY_GID variable not specified, defaulting to cmsusr user group id ($MY_GID)"
fi

echo $PWD

git clone https://github.com/dmwm/deployment.git

cd /code/deployment
git reset --hard $VER
echo $PWD

cat /code/python/workspaces-gem.py >> /code/deployment/dqmgui/workspaces-online.py
cp -v /code/python/gemtestbeam-layouts.py /code/deployment/dqmgui/layouts
cp -v /code/python/ge21qc8-layouts.py /code/deployment/dqmgui/layouts

cd /code
echo $PWD

$PWD/deployment/Deploy -A $ARCH -r "comp=comp" -R comp@$VER -t MYDEV -s "prep sw post" $PWD dqmgui/bare

#su cmsusr -s /bin/bash "$@"