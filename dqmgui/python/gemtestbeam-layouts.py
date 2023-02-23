def GEMTestBeamLayout(i, p, *rows): i["GEMTestBeam/Layouts/" + p] = DQMItem(layout=rows)

_GEMTestBeam_OFF_TWIKI = '<a href="https://twiki.cern.ch/twiki/bin/view/CMS/GEMPPDOfflineDQM">Link to TWiki</a>'

###############################################################################
# Digi Occupancy
###############################################################################
GEMTestBeamLayout(dqmitems, 'Occupancy GE0',
          [{'path': 'GEMTestBeam/Digis/digi_occ_GE0',
            'description': _GEMTestBeam_OFF_TWIKI}])

GEMTestBeamLayout(dqmitems, 'Occupancy GE1',
          [{'path': 'GEMTestBeam/Digis/digi_occ_GE1',
            'description': _GEMTestBeam_OFF_TWIKI}])

GEMTestBeamLayout(dqmitems, 'Occupancy GE2',
          [{'path': 'GEMTestBeam/Digis/digi_occ_GE2',
            'description': _GEMTestBeam_OFF_TWIKI}])
