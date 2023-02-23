#! /bin/bash

source current/apps/dqmgui/128/etc/profile.d/env.sh
sed -i -e '/export keytab/,+7 s/^/## /' $PWD/current/config/dqmgui/manage
#sed -i -e 's/127.0.0.1/collector/g' current/config/dqmgui/server-conf-online.py

$PWD/current/config/dqmgui/manage -f online start "I did read documentation"

/bin/bash "$@"
