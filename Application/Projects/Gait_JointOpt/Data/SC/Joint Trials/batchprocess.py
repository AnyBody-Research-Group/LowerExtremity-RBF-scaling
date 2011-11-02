# -*- coding: utf-8 -*-
"""
Created on Tue Nov 01 11:17:31 2011

@author: melund
"""

import os.path as op
import os
from subprocess import check_output
import threading

NUM_PROCESSES = 4


# Find run.bat files in subfolders 
tasklist = []
def collectBatFiles(arg,dirname, names):
    for name in [_ for _ in names if _.endswith('.bat')]:
        tasklist.append(op.join(dirname,name))
    
            
op.walk(op.abspath('.'), collectBatFiles,' ')


def process(batfile):
    (folder, name) = op.split(batfile)
    check_output(batfile,cwd = folder)
    print 'Processed ended' 


threads = []
# run until all the threads are done, and there is no data left
while threads or tasklist:
    # if we aren't using all the processors AND there is still data left to
    # compute, then spawn another thread
    if (len(threads) < NUM_PROCESSES) and tasklist:
        t = threading.Thread(target=process, args=[ tasklist.pop() ])
        t.setDaemon(True)
        t.start()
        threads.append(t)
    else:
        for thread in threads:
            if not thread.isAlive():
                threads.remove(thread)
