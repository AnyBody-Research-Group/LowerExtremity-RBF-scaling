# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:33:49 2011

@author: melund
"""

from anypytools.abcutils import AnyPyProcess, create_path_load_string

import os
################################ Setup ########################################
def modelpath(path):
    return os.path.join(os.getcwd(), path)
def outputpath(path):
    return os.path.join('z:/model_output/', path)
linear_model = modelpath('LinearScaledModel')
anatomic_model = modelpath('AnatomicalLandmarkScaledModel')
kinematic_model  = modelpath('KinematicScaledModel')
re_string = 'ngait.*\.[M,m]ain\.any'
n_processes = 5

app = AnyPyProcess(basepath = modelpath('Subjects/SC/Gait Trials'),
                   subdir_search= re_string,
                   num_processes = n_processes,
                   disp = True)
###############################################################################



################# RUN ANATOMICAL SCALED MODEL #################################
print '*'*60+'\n','Anatomically scaled model: Kineamtics'
pathdef = create_path_load_string({'MODEL_TYPE':anatomic_model,
                    'H5_OUTPUT':outputpath('anatomical_landmark_model/kinematics')
                    })
macro = ['load "Kinematics.main.any"'+pathdef,
         'operation Main.Load_JointTrialParameters', 'run',
         'operation Main.JntParameterOptModel.KinematicStudy.Kinematics','run',
         'operation Main.JntParameterOptModel.SaveKinOutputToH5File','run',
         'exit']
app.start_batch_job(macro)
print 'Anatomically scaled model: Set foot postions'
macro =  ['load "FootPosition.main.any"'+pathdef, 
          'operation Main.RunApplication',
          'run',
          'exit']
folder = modelpath('Subjects/SC/Static Trials/SC_staticfor_again1')
app.start_batch_job(macro, special_dir= folder)


####################### RUN KINEMATICALLY SCALED MODEL ########################
print '*'*60+'\n','Kinematically scaled model: Kineamtics'
pathdef = create_path_load_string({'MODEL_TYPE':kinematic_model,
                    'H5_OUTPUT':outputpath('kinematic_scaled_model/kinematics')
                    })
           
macro =  ['load "Kinematics.main.any"'+pathdef,
          'operation Main.Load_JointTrialParameters', 'run',
          'operation Main.JntParameterOptModel.KinematicStudy.Kinematics', 'run',
          'operation Main.JntParameterOptModel.SaveKinOutputToH5File', 'run',
          'exit']
app.start_batch_job(macro)
print 'Anatomically scaled model: Set foot postions'
macro =  ['load "FootPosition.main.any"'+pathdef, 
          'operation Main.RunApplication',
          'run',
          'exit']
folder = modelpath('Subjects/SC/Static Trials/SC_staticfor_again1')
app.start_batch_job(macro, special_dir= folder)


####################### RUN LINEARLY SCALED MODEL ########################
print '*'*60+'\n','Linearly scaled model: Kineamtics'
pathdef = create_path_load_string({'MODEL_TYPE':linear_model,
                    'H5_OUTPUT':outputpath('lin_scaled_model/kinematics')
                    })           
macro =  ['load "Kinematics.main.any"'+pathdef, 
          'operation Main.RunMotionAndParameterOptimizationSequence', 'run',
          'operation Main.SaveResults', 'run',
          'exit']
app.start_batch_job(macro)
print 'Linearly scaled model: update static anatomical frames'
macro =  ['load "FindStaticMarkerPos.main.any"'+pathdef, 
          'operation Main.CalculateStaticCoordinateSystemsALL',
          'run',
          'exit']
folder = modelpath('Subjects/SC/Static Trials/SC_staticfor_again1')
app.start_batch_job(macro, special_dir= folder)


#############################################################################
################## INVERSE DYNAMICS #################################
#############################################################################

################# RUN ANATOMICAL SCALED MODEL #################################
print '*'*60+'\n', 'Anatomically scaled model: Inverse dynamics'
pathdef = create_path_load_string({'MODEL_TYPE':anatomic_model,
                    'H5_OUTPUT':outputpath('anatomical_landmark_model/inversedynamics')
                    })                 
macro =  ['load "InversDynamics.main.any"'+pathdef,
 		  'operation Main.Load_JointTrialParameters', 'run',
 		  'operation Main.LoadFootJointAxis', 'run',
		  'operation Main.AnyBodyGaitAppModel.InverseDynamicStudy.InitialConditions',
		  'run',
		  'operation Main.AnyBodyGaitAppModel.HumanModel.Calibration.CalibrationSequence',
		  'run',
 		  'operation Main.AnyBodyGaitAppModel.InverseDynamicStudy.InverseDynamics', 'run',
 		  'operation Main.SaveOutputToH5File', 'run',
		  'exit']  
app.start_batch_job(macro)
####################### RUN KINEMATICALLY SCALED MODEL ########################
print '*'*60+'\n','Kinematically scaled model:  Inverse dynamics'
pathdef = create_path_load_string({'MODEL_TYPE':kinematic_model,
                    'H5_OUTPUT':outputpath('kinematic_scaled_model/inversedynamics')
                    })                 
macro =  ['load "InversDynamics.main.any"'+pathdef,
 		  'operation Main.Load_JointTrialParameters', 'run',
 		  'operation Main.LoadFootJointAxis', 'run',
		  'operation Main.AnyBodyGaitAppModel.InverseDynamicStudy.InitialConditions',
		  'run',
		  'operation Main.AnyBodyGaitAppModel.HumanModel.Calibration.CalibrationSequence',
		  'run',
 		  'operation Main.AnyBodyGaitAppModel.InverseDynamicStudy.InverseDynamics', 'run',
 		  'operation Main.SaveOutputToH5File', 'run',
		  'exit']   
app.start_batch_job(macro)

####################### RUN LINEARLY SCALED MODEL ########################
print '*'*60+'\n','Linearly scaled model: Inverse dynamics'
pathdef = create_path_load_string({'MODEL_TYPE':linear_model,
                    'H5_OUTPUT':outputpath('lin_scaled_model/inversedynamics')
                    })                 
macro =  ['load "InversDynamics.main.any"'+pathdef, 
          'operation Main.InverseDynamicAnalysisSequence',
          'run',
          'operation Main.SaveResults',
          'run',
          'exit']   
app.start_batch_job(macro)
