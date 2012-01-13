# -*- coding: utf-8 -*-
"""
Created on Mon Jan 09 12:19:16 2012

@author: melund
"""
from __future__ import division

import numpy as np
import os

def findpeaks(data, minheight, axis = None):
    # Find Indx of the signal higher than min hieght   
    Indx = np.nonzero(data > minheight)[0]
    if len(Indx) == 0:
        raise NameError('No peaks are large enough')
    # Find the signal trends to detect peaks 
    trend = np.sign(np.diff(data))
    # Find flat peaks )trend == 0) and remove them  
    idx = np.nonzero(trend==0)[0]
    if len(idx)>0:
        for i in reversed(xrange(idx)):
            if trend(np.min([idx[i]+1, len(trend)])) >=0:
                trend[idx[i]]= 1
            else:
                trend[idx[i]]=-1
    # Differentiate the trend and find location 'locs' of all peaks     
    trenddiff = np.diff(trend)
    idx = np.nonzero(np.diff(trend)==-2)[0]
    # Remove locs with peaks less than min height
    locs = np.intersect1d(idx,Indx)
    pks = data[locs]
    # create plot if an axis object is provided 
    if axis is not None :
#        ax.plot(data)
#        ax.plot(data)
        ax.plot(trenddiff)
    return (pks,locs)



def find_heelstrike_from_marker(marker, sacrummarker, beforetime, axis = None):
    # find dimension of working 
    marker = np.array(marker)
    sacrummarker = np.array(sacrummarker)
    # find dimention with largest variability (direction of walking) 
    dim = np.std(marker,0).argmax()  
    # Calculate the movement of marker with respect to sacrum marker
    data =  -(marker[:,dim]-sacrummarker[:,dim])
    # Find peaks of data (Where marker start moving backward)
    pks,locs = findpeaks(data-np.min(data),0.2,axis = axis)
    # Get last peak before 'beforetime''...
    lastpeak = locs[np.nonzero(locs<beforetime)][-1]
    if axis is not None:
        axis.plot(marker[:,0])        
    return lastpeak


def find_toeoff_from_marker( marker, sacrummarker, aftertime, axis = None):
    marker = np.array(marker)
    sacrummarker = np.array(sacrummarker)
    # find dimention with largest variability (direction of walking) 
    dim = np.std(marker,0).argmax()  
    # Calculate the movement of marker with respect to sacrum marker
    data = (marker[:,dim]-sacrummarker[:,dim])
    # Find peaks of data (Where marker start moving forward)
    pks,locs = findpeaks(data-np.min(data),0.2,axis = axis)
    # Get first peak after 'aftertime...
    firstpeak = locs[np.nonzero(locs>aftertime)][0]
    if axis is not None:
        axis.plot(marker[:,0])        
    return firstpeak
            
def find_toeoff(forcedata, threshold = 10, axis = None):
    forcedata = np.array(forcedata)
    indices = np.nonzero(forcedata < -threshold)[0]       
    if len(indices) > 0:
        return int(indices[-1])   
    else:
        return len(forcedata)
    
def find_heelstrike (forcedata, threshold = 10, axis = None):
    forcedata = np.array(forcedata)
    indices = np.nonzero(forcedata < -threshold)[0]       
    if len(indices) > 0:
        return int(indices[0])     
    else:
        return 0    
    
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
    TO_3 = find_toeoff(forces[order[2]])/avratio
    
    #Try to find the left or right toe off before ToeOff from kinmatic data
    try:
        LeftTO_0 = find_toeoff_from_marker(LToe,Sacrum,HS_1)
    except:
        LeftTO_0 = len(LToe)
    try:
        RightTO_0 = find_toeoff_from_marker(RToe,Sacrum,HS_1)
    except:
        RightTO_0 = len(LToe)
    TO_0 = np.min([LeftTO_0, RightTO_0])
    
    if TO_0 == len(LToe):
        TO_0 = 0
    
    #Try to find the Left and right HeelStrike after ToeOff from kinmatic data
    try:
        RightHS_4 = find_heelstrike_from_marker(RHeel,Sacrum,TO_3)
    except:
        RightHS_4 = 0
    try:
        LeftHS_4= find_heelstrike_from_marker(LHeel,Sacrum,TO_3)
    except:
        LeftHS_4 = 0
    HS_4 = np.max([RightHS_4,LeftHS_4])
    if HS_4 == 0:
        HS_4 = len(RHeel)
       
    print TO_3
    re = ( int(TO_0), int(HS_2), int(TO_1) , int(HS_3), int(TO_2) , int(HS_4))
    
    with open(os.path.join(folder,'HeelStrikeEvents.any'),'w') as f:
        f.write( 'AnyVector Events ={%d,%d,%d,%d,%d,%d};'% (TO_0, HS_2,TO_1,HS_3,TO_2,HS_4 ) )
        
    return re
    



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

    ret = foot_contact_times("",f1,f2,f3,RHeel,LHeel,RToe,LToe,Sacral, os.getcwd(), 10, axis = ax)
    print ret
    ax.plot(np.array(ret),np.zeros((len(ret),)), 'r^' )
    ax.plot(np.array(RHeel)[:,0] )
    ax.plot(np.array(LHeel)[:,0] )
#    print 'Heelstrike: ' + str(find_heelstrike("",testdata.FzForce))
#    print 'Toeoff: ' + str(find_toeoff("",testdata.FzForce))
#    print 'ToeoffKIN: ' + str(find_heelstrike_from_marker("",testdata.HeelMarker,testdata.SacrumMarker,axis = ax, aftertime = 200))
    time = np.linspace(0,len(RHeel), len(f1))
    ax.plot(time,np.array(f1)*0.002)
    ax.plot(time,np.array(f2)*0.002)
    ax.plot(time,np.array(f3)*0.002)
    plt.show()
    
    