# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 13:44:38 2012

@author: mel
"""

from anypytools.datagen import anydatah5
from os import getcwd
import matplotlib.pyplot as plt
import numpy as np 

folder = getcwd()
emg_alias = {'semimem': ['/Output/Validation/EMG/Semimembranosus/cActivity','/Output/Validation/EMG/Semimembranosus/mEMG'],
          'bifem': ['/Output/Validation/EMG/BicepsFemoris/cActivity', '/Output/Validation/EMG/BicepsFemoris/mEMG'],
          'vasmed':['/Output/Validation/EMG/VastusMedialis/cActivity', '/Output/Validation/EMG/VastusMedialis/mEMG'],
          'vaslat':['/Output/Validation/EMG/VastusLateralis/cActivity', '/Output/Validation/EMG/VastusLateralis/mEMG'],
          'rf':['/Output/Validation/EMG/RectusFemoris/cActivity','/Output/Validation/EMG/RectusFemoris/mEMG'],
          'medgas':['/Outp[ut/Validation/EMG/GastrocnemiusMedialis/cActivity','/Output/Validation/EMG/GastrocnemiusMedialis/mEMG'],
          'latgas':['/Output/Validation/EMG/GastrocnemiusLateralis/cActivity','/Output/Validation/EMG/GastrocnemiusLateralis/mEMG'],
          'tfl':['/Output/Validation/EMG/TensorFasciaeLatae/cActivity','/Output/Validation/EMG/TensorFasciaeLatae/mEMG'],
          'tibant':['/Output/Validation/EMG/TibialisAnterior/cActivity','/Output/Validation/EMG/TibialisAnterior/mEMG'],
          'peronl':['/Output/Validation/EMG/PeroneusLongus/cActivity','/Output/Validation/EMG/PeroneusLongus/mEMG'],
          'soleus':['/Output/Validation/EMG/Soleus/cActivity','/Output/Validation/EMG/Soleus/mEMG'],
          'addmag':['/Output/Validation/EMG/AdductorMagnus/cActivity','/Output/Validation/EMG/AdductorMagnus/mEMG'],
          'gmax':['/Output/Validation/EMG/GluteusMaximus/cActivity','/Output/Validation/EMG/GluteusMaximus/mEMG'],
          'gmed':['/Output/Validation/EMG/GluteusMedius/cActivity','/Output/Validation/EMG/GluteusMedius/mEMG'  ]}
    
    
events =  '/Output/EnvironmentModel/ContactEvents/'
    
    
    
    
figEMG = plt.figure()
ax = figEMG.add_subplot(111)


key = '/Output/Validation/EMG/RightGastrocnemiusLateralis/cActivity'

for (h5file, filename) in anydatah5(folder):
    if sum( h5file['/Output/EnvironmentModel/ForcePlate1/ContactDetectionLimb1/NodeWithInBox/WithinBoxAndVelBelowThreshold']) >  \
       sum( h5file['/Output/EnvironmentModel/ForcePlate1/ContactDetectionLimb2/NodeWithInBox/WithinBoxAndVelBelowThreshold']  ):
        print 'Left foot on middle forceplate'
    else:
        print 'Right foot on middle forceplate'

#    if data('Output.EnvironmentModel.ForcePlate1.ContactDetectionLimb1.InContactMuscle.S')
#    sig = data[key]
#    ax.plot(sig) 

#plt.show()
