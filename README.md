# gemdqm-dev

Development of GEM Local DQM framework

## Prerequisites

- [ ] [gemsw (QC8 and testbeam)](https://github.com/gem-sw/gemsw)

## Integration

```
cmsrel CMSSW_12_1_0
cd CMSSW_12_1_0/src
cmsenv
git cms-init -q
git cms-merge-topic yeckang:testbeam_2022
git clone git@github.com:gem-sw/gemsw.git
git clone ssh://git@gitlab.cern.ch:7999/rrabadan/gemdqm-dev.git DQM/GEMLocal
```

***

## Adding compiled code to a light-weight container
