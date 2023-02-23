def GE21QC8Layout(i, p, *rows): i["GE21QC8/Layouts/" + p] = DQMItem(layout=rows)

_GE21QC8_OFF_TWIKI = '<a href="https://twiki.cern.ch/twiki/bin/view/CMS/GEMPPDOfflineDQM">Link to TWiki</a>'

###############################################################################
# RecHit Occupancy
###############################################################################

GE21QC8Layout(dqmitems, 'Occupancy CH0',
          [{'path': 'GEM/QC8//rechit/rechit_occ_ch1',
            'description': _GE21QC8_OFF_TWIKI}])

GE21QC8Layout(dqmitems, 'Occupancy CH3',
          [{'path': 'GEM/QC8/rechit/rechit_occ_ch3',
            'description': _GE21QC8_OFF_TWIKI}])

GE21QC8Layout(dqmitems, 'Occupancy CH5',
          [{'path': 'GEM/QC8/rechit/rechit_occ_ch5',
            'description': _GE21QC8_OFF_TWIKI}])

GE21QC8Layout(dqmitems, 'Occupancy CH7',
          [{'path': 'GEM/QC8/rechit/rechit_occ_ch7',
            'description': _GE21QC8_OFF_TWIKI}])

GE21QC8Layout(dqmitems, 'Occupancy CH9',
          [{'path': 'GEM/QC8/rechit/rechit_occ_ch9',
            'description': _GE21QC8_OFF_TWIKI}])

GE21QC8Layout(dqmitems, 'Occupancy CH11',
          [{'path': 'GEM/QC8/rechit/rechit_occ_ch11',
            'description': _GE21QC8_OFF_TWIKI}])

GE21QC8Layout(dqmitems, 'Occupancy CH13',
          [{'path': 'GEM/QC8/rechit/rechit_occ_ch13',
            'description': _GE21QC8_OFF_TWIKI}])
