# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:33:49 2011

@author: melund
"""

from anypytools.abcutils import AnyBatchProcess

import os

folder = os.path.join(os.getcwd(),'Subjects/SC/Gait Trials')
re_string = 'ngait.*\.[M,m]ain\.any'

############################################################################
basemodel = os.path.join(os.getcwd(),'AnatomicalLandmarkScaledModel')
print 'Kinematic: AnatomicalScaledModel'
abp = AnyBatchProcess(basepath = folder,
                      searchfile= re_string,
                      num_processes = 5,
                      paths={'MODEL_TYPE':basemodel,
					  'H5_OUTPUT':'y:/model_output/anatomical_landmark_model/kinematics'})
macro =  ['load "Kinematics.main.any"',
 		  'operation Main.Load_JointTrialParameters', 'run',
 		  'operation Main.JntParameterOptModel.KinematicStudy.Kinematics', 'run',
 		  'operation Main.JntParameterOptModel.SaveKinOutputToH5File', 'run',
          'exit' ]         
abp.start(macro)
print 'Set foot position: Anatomically scaled model'
abp = AnyBatchProcess(basepath = os.path.join(os.getcwd(),'Subjects/SC/Static Trials'),
                      searchfile='FootPosition.main.any',
                      num_processes = 1,
                      paths={'MODEL_TYPE':basemodel,
					  'H5_OUTPUT':'y:/model_output/anatomical_landmark_model/kinematics'})
macro =  ['load "FootPosition.main.any"', 
          'operation Main.RunApplication',
          'run',
          'exit']
abp.start(macro)

##########################################################################
basemodel = os.path.join(os.getcwd(),'KinematicScaledModel')
print 'Kinematic: KinematicScaledModel'
abp = AnyBatchProcess(basepath = folder,
                      searchfile= re_string,
                      num_processes = 5,
                      paths={'MODEL_TYPE':basemodel,
					  'H5_OUTPUT':'y:/model_output/kinematic_scaled_model/kinematics'})
macro =  ['load "Kinematics.main.any"',
 		  'operation Main.Load_JointTrialParameters', 'run',
 		  'operation Main.JntParameterOptModel.KinematicStudy.Kinematics', 'run',
 		  'operation Main.JntParameterOptModel.SaveKinOutputToH5File', 'run',
           'exit']
abp.start(macro)
print 'Set foot position: Kinematic scaled model'
abp = AnyBatchProcess(basepath = os.path.join(os.getcwd(),'Subjects/SC/Static Trials'),
                      searchfile='FootPosition.main.any',
                      num_processes = 1,
                      paths={'MODEL_TYPE':basemodel,
					  'H5_OUTPUT':'y:/model_output/kinematic_scaled_model/kinematics'})
macro =  ['load "FootPosition.main.any"', 
          'operation Main.RunApplication',
          'run',
          'exit']
abp.start(macro)



############################################################################
basemodel = os.path.join(os.getcwd(),'LinearScaledModel')
print 'Kinematic: LinearScaledModel'
abp = AnyBatchProcess(basepath = folder,
                      searchfile= re_string,
                      num_processes = 5,
                      paths={'MODEL_TYPE':basemodel,
					  'H5_OUTPUT':'y:/model_output/lin_scaled_model/kinematics'})
macro =  ['load "Kinematics.main.any"', 
          'operation Main.RunMotionAndParameterOptimizationSequence',
          'run',
          'operation Main.SaveResults',
         'run',
         'exit']
abp.start(macro)


folder = os.path.join(os.getcwd(),'Subjects/SC/Static Trials/SC_staticfor_again1')
print 'Kinematic: LinearScaledModel, update static frames'
abp = AnyBatchProcess(basepath = folder,
                      searchfile='FindStaticMarkerPos.main.any',
                      num_processes = 1,
                      paths={'MODEL_TYPE':basemodel,
					  'H5_OUTPUT':'y:/model_output/lin_scaled_model/kinematics'})
macro =  ['load "FindStaticMarkerPos.main.any"', 
          'operation Main.CalculateStaticCoordinateSystemsALL',
          'run',
          'exit']
abp.start(macro)
folder = os.path.join(os.getcwd(),'Subjects/SC/Gait Trials')



#############################################################################
#############################################################################
#############################################################################
basemodel = os.path.join(os.getcwd(),'AnatomicalLandmarkScaledModel')
print 'Inverse: AnatomicalLandmarkScaledModel'
abp = AnyBatchProcess(basepath = folder,
                       searchfile= re_string,
                      num_processes = 5,
                      paths={'MODEL_TYPE':basemodel,
					  'H5_OUTPUT':'y:/model_output/anatomical_landmark_model/inversedynamics'})
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

##############################################################################
basemodel = os.path.join(os.getcwd(),'KinematicScaledModel')
print 'Inverse: KinematicScaledModel'
abp = AnyBatchProcess(basepath = folder,
                       searchfile= re_string,
                      num_processes = 5,
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
#############################################################################
basemodel = os.path.join(os.getcwd(),'LinearScaledModel')
print 'Inverse: LinearScaledModel'
abp = AnyBatchProcess(basepath = folder,
                      searchfile= re_string,
                      num_processes = 5,
                      paths={'MODEL_TYPE':basemodel,
					  'H5_OUTPUT':'y:/model_output/lin_scaled_model/inversedynamics'})
macro =  ['load "InversDynamics.main.any"', 
          'operation Main.InverseDynamicAnalysisSequence',
          'run',
          'operation Main.SaveResults',
          'run',
          'exit']         
abp.start(macro)
##############################################################################
