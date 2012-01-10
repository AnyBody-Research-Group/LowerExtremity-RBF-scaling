# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09 12:19:16 2012

@author: melund
"""
from __future__ import division

import numpy as np
import os

def findpeaks(data, minheight, axis = None):
    
    Indx = np.nonzero(data > minheight)[0]
    if len(Indx) == 0:
        raise NameError('No peaks are large enough')
    
    
    trend = np.sign(np.diff(data))
    
    idx = np.nonzero(trend==0)[0]
    if len(idx)>0:
        for i in reversed(xrange(idx)):
            if trend(np.min([idx[i]+1, len(trend)])) >=0:
                trend[idx[i]]= 1
            else:
                trend[idx[i]]=-1
       
    trenddiff = np.diff(trend)
    
    if axis is not None :
#        ax.plot(data)
#        ax.plot(data)
        ax.plot(trenddiff)


    idx = np.nonzero(np.diff(trend)==-2)[0]
    locs = np.intersect1d(idx,Indx)
    pks = data[locs]
    
    
    
    return (pks,locs)



def find_heelstrike_from_marker(context, toemarker, sacrummarker, aftertime, axis = None):
    # find dimension of working 
    toemarker = np.array(toemarker)
    sacrummarker = np.array(sacrummarker)
    
    dim = np.std(toemarker,0).argmax()
    toedata = toemarker[:,0]
    sacrdata = sacrummarker[:,0]
    
    data = -(toedata-sacrdata)
    
    pks,locs = findpeaks(data-np.min(data),0.2,axis = axis)
    firstpeak = locs[np.nonzero(locs>aftertime)][0]
    
    return firstpeak
    
        
        
def find_toeoff(context, forcedata, threshold = 10, axis = None):
    forcedata = np.array(forcedata)
    indices = np.nonzero(forcedata < -threshold)[0]       
        
    if len(indices) > 0:
        return int(indices[-1])   
    else:
        return len(forcedata)
    
def foot_contact_times(context, f1,f2,f3,RHeel,LHeel, Sacrum, folder, avratio, axis = None):
    forces = np.array([f1,f2,f3])
    print forces.shape
    peaks = np.argmin(forces,1)
    order = np.argsort(peaks)
    # Find events based on force plate measurements
    HS1 = ( find_heelstrike("",forces[order[1]])/avratio)
    TO = ( find_toeoff("",forces[order[1]]) /avratio)
    CTO = ( find_toeoff("",forces[order[0]])/avratio)
    CHS = ( find_heelstrike("",forces[order[2]]) /avratio)
    
    #Try to find the Left and right HeelStrike after ToeOff from kinmatic data
    try:
        HS2L = find_heelstrike_from_marker("",LHeel,Sacrum,TO)
    except:
        HS2L = 0
    try:
        HS2R= find_heelstrike_from_marker("",RHeel,Sacrum,TO)
    except:
        HS2R = 0
    HS2 = np.max([HS2L,HS2R])
    #If HS2 = 0, then no Heel strike could be found. Then set to Last frame
    if HS2 == 0:
        HS1 = 0
        HS2 = len(RHeel)
       
       
    re = (int(HS1),int(CTO),int(CHS),int(TO),int(HS2))
      
    with open(os.path.join(folder,'HeelStrikeEvents.any'),'w') as f:
        f.write( 'AnyVector Events ={%d,%d,%d,%d,%d};'% (HS1,CTO,CHS,TO,HS2) )
        
    return re
    
    
    
    
    
def find_heelstrike (context, forcedata, threshold = 10, axis = None):
    
    forcedata = np.array(forcedata)
    indices = np.nonzero(forcedata < -threshold)[0]       
        
    if len(indices) > 0:
        return int(indices[0])     
    else:
        return 0
    



if __name__ == "__main__":
    import testdata
    import matplotlib.pyplot as plt
    import numpy as np
    f1 = testdata.f1
    f2 = testdata.f2
    f3 = testdata.f3
    RHeel = testdata.RHeel
    LHeel = testdata.LHeel
    Sacral = testdata.Sacral
    
    
    fig = plt.figure()
    ax = fig.add_subplot(111)

    print foot_contact_times("",f1,f2,f3,RHeel,LHeel,Sacral, os.getcwd(), 10, axis = ax)

#    print 'Heelstrike: ' + str(find_heelstrike("",testdata.FzForce))
#    print 'Toeoff: ' + str(find_toeoff("",testdata.FzForce))
#    print 'ToeoffKIN: ' + str(find_heelstrike_from_marker("",testdata.HeelMarker,testdata.SacrumMarker,axis = ax, aftertime = 200))
    ax.plot(RHeel)
    ax.plot(LHeel)

    plt.show()
    
    