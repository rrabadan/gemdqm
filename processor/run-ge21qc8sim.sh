#! /bin/bash

CMSSW_RELEASE=CMSSW_12_3_5_patch1

cd $WDIR
echo $PWD
#mkdir $WDIR/Gui
#cd $WDIR/Gui

#cp -v $WDIR/collector/dqm_run_config $WDIR/$CMSSW_RELEASE/src/gemsw/Validation/test
cd $WDIR/$CMSSW_RELEASE/src
echo $PWD
cmsenv
cd gemsw/Validation/test
echo $PWD

sleep 100

mkdir upload

sed -i -e 's/5000/50000/g' ge21qc8sim_dqm_sourceclient-live_cfg.py
cmsRun ge21qc8sim_dqm_sourceclient-live_cfg.py

cd $WDIR

/bin/bash "$@"
