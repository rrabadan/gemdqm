import FWCore.ParameterSet.Config as cms

from DQM.GEMLocal.GEMLocal_cfi import *

GEMDQM = cms.Sequence(
  GEMLocal
)

#from Configuration.Eras.Modifier_phase2_GEM_cff import phase2_GEM
#phase2_GEM.toModify(GEMDigiSource, digisInputLabel = "simMuonGEMDigis")
