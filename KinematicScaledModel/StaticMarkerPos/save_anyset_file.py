
def formstring(varname, value):
    if isinstance(value[0],float):
        return '%s={%f,%f,%f};\n' % (varname, value[0],value[1],value[2])
    else:
        return '%s={{%f,%f,%f},{%f,%f,%f},{%f,%f,%f}};\n' % (varname, 
                value[0][0],value[0][1],value[0][2], 
                value[1][0],value[1][1],value[1][2], 
                value[2][0],value[2][1],value[2][2]  )

def save_vec3(context,filename, varname, value):
    save_variable(filename, varname, value)
    return 1

def save_anymat33(context,filename, varname, value):
    save_variable(filename, varname, value)
    return 1


def save_variable(filename, varname, value):
    import os
    
#    pymodule = context[0]
#    pyfunction = context[1]
#    anybodymonofun =  context[2]
#    anymainfile =  context[3]
    
    if not os.path.exists(filename):
        with open(filename,'w') as f:
            pass

    with open(filename, 'r') as f:
        lines = f.readlines()
        for idx in range(0,len(lines)):
            if lines[idx].startswith(varname):
                lines[idx] = formstring(varname, value)
                break
        else:
            lines.append(formstring(varname, value))

    with open(filename,'w') as f:
        f.write("".join(lines))
        
	
    return (1)

if __name__ == '__main__':
    context = 'test'
    
    filename = """C:/Users/melund/Documents/AnyBody/rbf_scale_legtd/Application/Projects/Gait_JointOpt/BaseModel/FootPosModel/test.anyset"""
    varname = 'Main.AnyBodyGaitAppModel.HumanModel.BodyModel.Right.Leg.Seg.Talus.SubTalarJoint.sRel'
    value = [4.0, 2.3, 1.3]
    save_variable( filename, varname,value)
    filename = """C:/Users/melund/Documents/AnyBody/rbf_scale_legtd/Application/Projects/Gait_JointOpt/BaseModel/FootPosModel/test.anyset"""
    varname = 'Main.AnyBodyGaitAppModel.HumanModel.BodyModel.Right.Leg.Seg.Talus.AnkleJoint.ARel'
    value = [(2,2,2),(2,2,2), (2,2,2)]
    save_variable( filename, varname, value)