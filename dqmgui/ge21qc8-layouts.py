def GE21QC8Layout(i, p, *rows): i["GE21QC8/Layouts/" + p] = DQMItem(layout=rows)

_GE21QC8_OFF_TWIKI = '<a href="https://twiki.cern.ch/twiki/bin/view/CMS/GEMPPDOfflineDQM">Link to TWiki</a>'

###############################################################################
# RecHit Occupancy
###############################################################################

GE21QC8Layout(dqmitems, 'Occupancy CH0',
          [{'path': 'GEM/QC8//rechit/rechit_occ_ch0',
            'description': _GE21QC8_OFF_TWIKI}])

GE21QC8Layout(dqmitems, 'Occupancy CH1',
          [{'path': 'GEM/QC8/rechit/rechit_occ_ch1',
            'description': _GE21QC8_OFF_TWIKI}])

GE21QC8Layout(dqmitems, 'Occupancy CH2',
          [{'path': 'GEM/QC8/rechit/rechit_occ_ch2',
            'description': _GE21QC8_OFF_TWIKI}])

GE21QC8Layout(dqmitems, 'Occupancy CH3',
          [{'path': 'GEM/QC8/rechit/rechit_occ_ch3',
            'description': _GE21QC8_OFF_TWIKI}])

GE21QC8Layout(dqmitems, 'Occupancy CH4',
          [{'path': 'GEM/QC8/rechit/rechit_occ_ch4',
            'description': _GE21QC8_OFF_TWIKI}])

GE21QC8Layout(dqmitems, 'Occupancy CH5',
          [{'path': 'GEM/QC8/rechit/rechit_occ_ch5',
            'description': _GE21QC8_OFF_TWIKI}])

GE21QC8Layout(dqmitems, 'Occupancy CH6',
          [{'path': 'GEM/QC8/rechit/rechit_occ_ch6',
            'description': _GE21QC8_OFF_TWIKI}])

GE21QC8Layout(dqmitems, 'Occupancy CH7',
          [{'path': 'GEM/QC8/rechit/rechit_occ_ch7',
            'description': _GE21QC8_OFF_TWIKI}])
