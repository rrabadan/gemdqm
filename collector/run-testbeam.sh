#! /bin/bash

CMSSW_RELEASE=CMSSW_12_3_5_patch1

cd $WDIR
mkdir $WDIR/Gui
cd $WDIR/Gui

cp -v $WDIR/collector/dqm_run_config $WDIR/$CMSSW_RELEASE/src/gemsw/Validation/test
cd $WDIR/$CMSSW_RELEASE/src
cmsenv
cd gemsw/Validation/test

sleep 60

mkdir upload

cmsRun gemtestbeam_dqm_sourceclient-live_cfg.py inputFiles=file:/data/testbeam.raw maxEvents=300000 runNumber=350588

cd $WDIR

su cmsusr -s /bin/bash "$@"
