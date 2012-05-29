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
                      searchfile='Kinematics.main.any',
                      num_processes = 4,
                      paths={'MODEL_TYPE':basemodel,
					  'H5_OUTPUT':'z:/model_output/lin_scaled_model/kinematics'})

macro =  ['load "Kinematics.main.any"', 
          'operation Main.RunMotionAndParameterOptimizationSequence',
          'run',
          'operation Main.SaveResults',
          'run',
          'exit']
          


          
abp.start(macro)

