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



def find_heelstrike_from_marker(marker, sacrummarker, beforetime, axis = None):
    # find dimension of working 
    marker = np.array(marker)
    sacrummarker = np.array(sacrummarker)
    
    dim = np.std(marker,0).argmax()  
    data = -(marker[:,dim]-sacrummarker[:,dim])
    
    pks,locs = findpeaks(data-np.min(data),0.2,axis = axis)
    lastpeak = locs[np.nonzero(locs<beforetime)][-1]
    
    return lastpeak


def find_toeoff_from_marker( sacrummarker, aftertime, axis = None):
    # find dimension of working 
    marker = np.array(marker)
    sacrummarker = np.array(sacrummarker)
    
    dim = np.std(marker,0).argmax()  
    data = (marker[:,dim]-sacrummarker[:,dim])
    
    pks,locs = findpeaks(data-np.min(data),0.2,axis = axis)
    firstpeak = locs[np.nonzero(locs>aftertime)][0]
    
    return firstpeak
            
        
def find_toeoff(forcedata, threshold = 10, axis = None):
    forcedata = np.array(forcedata)
    indices = np.nonzero(forcedata < -threshold)[0]       
        
    if len(indices) > 0:
        return int(indices[-1])   
    else:
        return len(forcedata)
    
def foot_contact_times(context, f1,f2,f3,RHeel,LHeel,RToe,LToe, Sacrum, folder, avratio, axis = None):
    forces = np.array([f1,f2,f3])
    print forces.shape
    peaks = np.argmin(forces,1)
    order = np.argsort(peaks)
    # Find events based on force plate measurements
    HS_1 = find_heelstrike( forces[order[0]] ) / avratio
    TO_1 = find_toeoff(forces[order[0]]) / avratio
    HS_2 = find_heelstrike( forces[order[1]] ) / avratio
    TO_2 = find_toeoff(forces[order[1]]) /avratio 
    HS_3 = find_heelstrike(forces[order[2]]) /avratio
    TO_3 = find_toeoff(forces[order[0]])/avratio
    
    #Try to find the left or right toe off before ToeOff from kinmatic data
    try:
        LeftTO_0 = find_toeoff_from_marker(LToe,Sacrum,HS_1)
    except:
        LeftTO_0 = 0
    try:
        RightTO_0 = find_toeoff_from_marker(RToe,Sacrum,HS_1)
    except:
        RightTO_0 = 0
    TO_0 = np.max([LeftTO_0, RightTO_0])
        
    
    #Try to find the Left and right HeelStrike after ToeOff from kinmatic data
    try:
        RightHS_4 = find_heelstrike_from_marker(RHeel,Sacrum,TO_3)
    except:
        RightHS_4 = len(RHeel)
    try:
        LeftHS_4= find_heelstrike_from_marker(LHeel,Sacrum,TO_3)
    except:
        LeftHS_4 = len(LHeel)
    HS_4 = np.min([RightHS_4,LeftHS_4])
       
       
    re = ( int(HS_1), int(TO_0), int(HS_2), int(TO_1) , int(HS_3), int(TO_2) , int(HS_4), int(TO_3) )
      
    with open(os.path.join(folder,'HeelStrikeEvents.any'),'w') as f:
        f.write( 'AnyVector Events ={%d,%d,%d,%d,%d,%d,%d,%d};'% ( HS_1,TO_0, HS_2,TO_1,HS_3,TO_2,HS_4,TO_3 ) )
        
    return re
    
    
    
    
    
def find_heelstrike (forcedata, threshold = 10, axis = None):
    
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
    RToe = testdata.RToe
    LToe = testdata.LToe
    Sacral = testdata.Sacral
    
    
    fig = plt.figure()
    ax = fig.add_subplot(111)

    print foot_contact_times("",f1,f2,f3,RHeel,LHeel,RToe,LToe,Sacral, os.getcwd(), 10, axis = ax)

#    print 'Heelstrike: ' + str(find_heelstrike("",testdata.FzForce))
#    print 'Toeoff: ' + str(find_toeoff("",testdata.FzForce))
#    print 'ToeoffKIN: ' + str(find_heelstrike_from_marker("",testdata.HeelMarker,testdata.SacrumMarker,axis = ax, aftertime = 200))
    ax.plot(RHeel)
    ax.plot(LHeel)

    plt.show()
    
    