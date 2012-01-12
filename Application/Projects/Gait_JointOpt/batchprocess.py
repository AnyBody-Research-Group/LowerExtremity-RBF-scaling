# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:33:49 2011

@author: melund
"""

from anypytools.abcutils import AnyBatchProcess

import os

folder = os.path.join(os.getcwd(),'Data/SC')

abp = AnyBatchProcess(basepath = folder,
                      searchfile='Kinematics.main.any',
                      num_processes = 3)

macro =  ['load "Kinematics.main.any"',
		  'operation Main.Load_JointTrialParameters', 'run',
		  'operation Main.LoadFootJointAxis', 'run',
		  'operation Main.AnyBodyGaitAppModel.InverseDynamicStudy.InverseDynamics', 'run'
		  'classoperation "Save data" --type="Deep" --file="%s"' %


'exit',' ']


#macro =  ['load "Kinematics.main.any"', 
#          'operation Main.Load_JointTrialParameters',
#          'run',
#          'operation Main.JntParameterOptModel.KinematicStudy.Kinematics',
#          'run',' ','exit',' ']
          
abp.start(macro)

