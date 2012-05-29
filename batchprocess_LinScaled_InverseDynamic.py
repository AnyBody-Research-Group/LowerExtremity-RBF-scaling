# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:33:49 2011

@author: melund
"""

from anypytools.abcutils import AnyBatchProcess

import os

folder = os.path.join(os.getcwd(),'Subjects/SC/Gait Trials')
basemodel = os.path.join(os.getcwd(),'LinearScaledModel')



abp = AnyBatchProcess(basepath = folder,
                      searchfile='InversDynamics.main.any',
                      num_processes = 3,
                      paths={'MODEL_TYPE':basemodel,
					  'H5_OUTPUT':'z:/model_output/lin_scaled_model/inversedynamics'})

macro =  ['load "InversDynamics.main.any"', 
          'operation Main.InverseDynamicAnalysisSequence',
          'run',
          'operation Main.SaveResults',
          'run',
          'exit']
          


          
abp.start(macro)

