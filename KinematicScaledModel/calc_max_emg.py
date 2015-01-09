import csv
import numpy as np
from scipy.signal import butter, lp2bp, filtfilt

def get_max_emg(context, filename, order,f_bp1, f_bp2, f_lp, muscle):
    with open(filename) as f:
        reader = csv.reader(f, delimiter=",")
        header = reader.next()
        dataMax = np.array([[float(col) for col in row] for row in reader])

    with open(filename) as f:
        reader = csv.reader(f, delimiter=",")
        header = reader.next()
        dataMin = np.array([[float(col) for col in row] for row in reader])


    fs = len(data)/(data[-1,0]-data[0,0])
    fny = fs/2
    
    
    try:
        idx = header.index(muscle)
    except ValueError:
        return 0
    data = data[:,idx]
    
        
    ## HIGH PASS FILTER
    bp_low = f_bp1
    bp_high = f_bp2
    centerfreq = (bp_high+bp_low)/2
    bandwidthfreq = (bp_high -bp_low)   
    (b,a) = butter(2,0.5)
      # Transform to band pass
    (b,a) = lp2bp(b,a,centerfreq/fny, bandwidthfreq/fny)
    data =  filtfilt(b,a,data)  
    
    data = np.abs(data )
    
    ## Low pass filter envelope
    lp_low = f_lp
    (b,a) = butter(2,lp_low/fny)
    data =  filtfilt(b,a,data)  
    
    ## Get max values
    dmax = np.max( data )
    return (dmax)    
    
        
        
        
if __name__=="__main__":
    filename = 'C:/Users/melund/Documents/AnyBody/rbf_scale_legtd/Application/Projects/Gait_JointOpt/Data/SC/Max Emg/SC_maxEMG.csv'
    with open(filename) as f:
        reader = csv.reader(f, delimiter=",")
        header = reader.next()
        data = np.array([[float(col) for col in row] for row in reader])
        
    dd = get_max_emg(" ", filename,2, 30, 200, 6 , "semimem")
    print(dd)
