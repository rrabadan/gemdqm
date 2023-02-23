#! /bin/bash

CMSSW_RELEASE=CMSSW_12_1_0

cd $WDIR
echo $PWD

source /cvmfs/cms.cern.ch/cmsset_default.sh

cd $WDIR/$CMSSW_RELEASE/src
echo $PWD
cmsenv
cd gemsw/Validation/test
echo $PWD

#sleep 30

mkdir upload

cmsRun gemtestbeam_dqm_live_cfg.py inputFiles=file:/data/00000397-0-0.raw,file:/data/00000397-1-0.raw firstRun=350588

#cd $WDIR

/bin/bash "$@"
