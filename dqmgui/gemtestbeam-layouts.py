# Generated automatically by dqmgui/gem_custom/fillLayouts.py 
#   in https://github.com/quark2/deployment/tree/addingGem
#   Recipe: 
#     cd deployment/dqmgui
#     python3 gem_custom/fillLayouts.py
def GEMTestBeamLayout(i, p, *rows): i["GEMTestBeam/Layouts/" + p] = DQMItem(layout=rows)

_GEMTestBeam_OFF_TWIKI = '<a href="https://twiki.cern.ch/twiki/bin/view/CMS/GEMPPDOfflineDQM">Link to TWiki</a>'

###############################################################################
# Summary Map
###############################################################################
#GEMTestBeamLayout(dqmitems, '00 Summary Map',
#          [{'path': 'GEMTestBeam/EventInfo/reportSummaryMap',
#            'description': _GEMTestBeam_OFF_TWIKI}])

###############################################################################
# RecHit Occupancy
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
