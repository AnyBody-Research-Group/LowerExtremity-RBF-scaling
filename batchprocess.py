# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:33:49 2011

@author: melund
"""

from anypytools.abcutils import AnyBatchProcess

import os

folder = os.path.join(os.getcwd(),'Subjects/SC/Gait Trials/SC_bouncy_og3')
#basemodel = os.path.join(os.getcwd(),'KinematicScaledModel')
#basemodel = os.path.join(os.getcwd(),'AnatomicalLandmarkScaledModel')
basemodel = os.path.join(os.getcwd(),'LinearScaledModel')



abp = AnyBatchProcess(basepath = folder,
                      searchfile='Kinematics.main.any',
                      num_processes = 1,
                      paths={'MODEL_TYPE':basemodel})#,
					  #'H5_OUTPUT':'C:/Users/melund/Documents/AnyBody/rbf_scale_legtd/Application/Projects/Gait_JointOpt/Output/kin'})

macro =  ['load "Kinematics.main.any"', 
          'operation Main.RunMotionAndParameterOptimizationSequence',
          'run',
          'operation Main.SaveResults',
          'run',
          'exit']
          
#macro =  ['load "Kinematics.main.any"', 
#          'operation Main.RunMotionAndParameterOptimizationSequence',
#          'run',
#          'operation Main.JntParameterOptModel.KinematicStudy.Kinematics',
#          'run',
#          'operation Main.JntParameterOptModel.SaveKinOutputToH5File',
#          'run',
#          'exit']
#          

 # abp = AnyBatchProcess(basepath = folder,
                       # searchfile='InversDynamics.main.any',
                       # num_processes = 1,
                      # paths={'MODEL_TYPE':'KinematicScaledModel'}#,
                      # 'H5_OUTPUT':'C:/Users/melund/Documents/AnyBody/rbf_scale_legtd/Application/Projects/Gait_JointOpt/Output'})
 
 
 # macro =  ['load "InversDynamics.main.any"',
 		  # 'operation Main.Load_JointTrialParameters', 'run',
 		  # 'operation Main.LoadFootJointAxis', 'run',
 		  # 'operation Main.AnyBodyGaitAppModel.InverseDynamicStudy.InverseDynamics', 'run',
 		  # 'operation Main.SaveOutputToH5File', 'run',
              # 'exit']



          
abp.start(macro)

