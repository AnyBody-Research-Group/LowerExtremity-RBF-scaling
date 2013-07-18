import os.path as op

from IPython import parallel



# create client & view
rc = parallel.Client()
dv = rc[:]
v = rc.load_balanced_view()

# scatter 'id', so id=0,1,2 on engines 0,1,2
dv.scatter('id', rc.ids, flatten=True)
print("Engine IDs: ", dv['id'])


# Find run.bat files in subfolders 
tasklist = []
def collectBatFiles(arg,dirname, names):
    for name in [_ for _ in names if _.endswith('.bat')]:
        tasklist.append(op.join(dirname,name))
op.walk(op.abspath('.'), collectBatFiles,' ')


def process(batfile):
    import os.path as op
    from subprocess import check_output
    (folder, name) = op.split(batfile)
    check_output(batfile,cwd = folder)
    return op.split(folder)[-1]
    
    
amr = v.map(process, tasklist)
for i,r in enumerate(amr):
    print("Done: %i: %s" % (i, r))
