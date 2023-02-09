# gemdqm-dev

Development of GEM Local DQM.

CMSSW DQM and official DQM with docker compose

Project structure


```
.
├── dqmgui/
├── README.md 
└── docker-compose.yaml
```

## CMS DQM GUI

- [ ] [CMSDMWM Deployments](https://github.com/dmwm/deployment)

`dqmgui/` folder contains the GEM Local workspaces and layout definitions.

`dqmgui/install-and-run.sh` builds the GUI with the GEM Local and starts it.

## Adding compiled code to a light-weight container

- [ ] [gemsw (QC8 and testbeam)](https://github.com/gem-sw/gemsw)
- [_] image with compiled code
    - gitlab-registry.cern.ch/rrabadan/gemsw:latest

