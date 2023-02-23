#! /bin/bash

source current/apps/dqmgui/128/etc/profile.d/env.sh

$PWD/current/config/dqmgui/manage -f online restart "I did read documentation"

/bin/bash "$@"
