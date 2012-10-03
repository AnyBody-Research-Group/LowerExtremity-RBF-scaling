# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:33:49 2011

@author: melund
"""

from anypytools.abcutils import AnyBatchProcess
import os

folder = os.path.join(os.getcwd(),'Subjects/SC/Gait Trials')
basemodel = os.path.join(os.getcwd(),'AnatomicalLandmarkScaledModel')

abp = AnyBatchProcess(basepath = folder,
                      searchfile='Kinematics.main.any',
                      num_processes = 2,
                      paths={'MODEL_TYPE':basemodel,
					  'H5_OUTPUT':'y:/model_output/anatomical_landmark_model/kinematics'})

macro =  ['load "Kinematics.main.any"',
 		  'operation Main.Load_JointTrialParameters', 'run',
 		  'operation Main.JntParameterOptModel.KinematicStudy.Kinematics', 'run',
 		  'operation Main.JntParameterOptModel.SaveKinOutputToH5File', 'run',
          'exit' ]

         
abp.start(macro)

