# -*- coding: utf-8 -*-
"""
Created on Tue Nov 01 11:17:31 2011

@author: melund
"""
from __future__ import print_function

import os.path as op
from subprocess import check_output
import threading
import sys

print = lambda x: sys.stdout.write("%s\n" % x)

NUM_PROCESSES = 10


# Find run.bat files in subfolders 
tasklist = []
def collectBatFiles(arg,dirname, names):
    for name in [_ for _ in names if _.endswith('.bat')]:
        tasklist.append(op.join(dirname,name))
    
            
op.walk(op.abspath('.'), collectBatFiles,' ')

bat1 = tasklist[0]

def process(batfile):
    (folder, name) = op.split(batfile)
    check_output(batfile,cwd = folder)
    print( 'Done: ' + op.split(folder)[-1])


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
