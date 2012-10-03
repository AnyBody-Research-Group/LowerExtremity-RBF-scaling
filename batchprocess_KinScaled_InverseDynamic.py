# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:33:49 2011

@author: melund
"""

from anypytools.abcutils import AnyBatchProcess

import os

folder = os.path.join(os.getcwd(),'Subjects/SC/Gait Trials/SC_ngait_og5')
basemodel = os.path.join(os.getcwd(),'KinematicScaledModel')
print 'Inverse: KinematicScaledModel'

abp = AnyBatchProcess(basepath = folder,
                       searchfile='InversDynamics.main.any',
                      num_processes = 1,
                      paths={'MODEL_TYPE':basemodel,
					  'H5_OUTPUT':'y:/model_output/kinematic_scaled_model/inversedynamics'})


macro =  ['load "InversDynamics.main.any"',
 		  'operation Main.Load_JointTrialParameters', 'run',
 		  'operation Main.LoadFootJointAxis', 'run',
		  'operation Main.AnyBodyGaitAppModel.InverseDynamicStudy.InitialConditions',
		  'run',
		  'operation Main.AnyBodyGaitAppModel.HumanModel.Calibration.CalibrationSequence',
		  'run',
 		  'operation Main.AnyBodyGaitAppModel.InverseDynamicStudy.InverseDynamics', 'run',
 		  'operation Main.SaveOutputToH5File', 'run',
		  'exit']



          
abp.start(macro)

