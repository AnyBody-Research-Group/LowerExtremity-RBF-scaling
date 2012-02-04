# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 15:58:34 2011

@author: melund
"""
import os, fnmatch

def subdirs_have_file(pattern, root=os.getcwd(),recursive = True):
    ''' Checks if a file exist in the current directory or subdirectories '''
    for path,dirs, files, in os.walk(os.path.abspath(root)):
        if len(fnmatch.filter(files,pattern)) > 0:
            return True

def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]
            
                      
def create_task_folder(folder,pattern, indent = 0):    
    script = ""
    #Check if folder contains any files that match pattern else return
    for path,dirs, files, in os.walk(os.path.abspath(folder)):
        if len(fnmatch.filter(files,pattern)) > 0:
            break
    else:
        return script
    foldername = os.path.basename(folder)
    
    if subdirs_have_file('*_ERROR.txt',folder):
        anyfoldername = foldername.replace(' ','_')+'_error'
    else:
        anyfoldername = foldername.replace(' ','_')
        
    script += " "*indent + "AnyProjectTaskFolder %s = { \n" % anyfoldername
    for subfolder in get_immediate_subdirectories(os.path.abspath(folder)):
        fullpath = os.path.join(folder,subfolder)
        script += create_task_folder(fullpath,pattern,indent+2)
    for mainfile in fnmatch.filter(os.listdir(folder), pattern):
        filename = os.path.basename(mainfile)            
        script += " "*(indent +2)+"AnyProjectTaskLoadModel  %s= { \n" % filename[0:-9].replace(' ','_')
        script += " "*(indent +4)+'MainFile = PROJECT_PATH+"Data/"+"%s";\n'  % os.path.join(folder,mainfile)
#        script += " "*(indent+4)+ 'Description.Title = "Load ";'
        script += " "*(indent+4)+ 'Description.Files = PROJECT_PATH+"Data/"+"%s";\n' % os.path.join(folder, 'output_log.txt')
        script += " "*(indent +2)+"};\n"
    script += " "*indent +'};\n'
    return script
    

    



if __name__ == '__main__':
    script = "AnyProjectTaskFolder Switch_Trial = { \n"
    for dirname in get_immediate_subdirectories(os.getcwd()):
        script += create_task_folder(dirname,'*.main.any',2)
    script += "};\n"
    
        
    with open('TrialSelector.any','w') as fh:
        fh.write(script)
