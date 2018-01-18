import os
import glob
import shutil
vs2013="C:/Program Files (x86)/Microsoft Visual Studio 12.0/Common7/IDE/Extensions"
vs2015="C:/Program Files (x86)/Microsoft Visual Studio 14.0/Common7/IDE/Extensions"
vs2017="C:/Program Files (x86)/Microsoft Visual Studio/2017/Enterprise/Common7/IDE/Extensions"

def get_pentaK_path(vspath):
    extension_list = os.listdir(vspath)
    pentak_dir = [ i for i in extension_list if glob.glob(os.path.join(vspath,i,"Nvidia.PentaK*"))]
    print(vspath,":",pentak_dir)
    return [os.path.join(vspath,i) for i in pentak_dir]

def batch_check():
    global vs2013
    global vs2015
    global vs2017
    print([get_pentaK_path(i) for i in (vs2013,vs2015,vs2017)])

def cleanup(cleandir):
    for i in cleandir:
        print("delete {} ....".format(i))
        shutil.rmtree(i)

def batch_clean():
    global vs2013
    global vs2015
    global vs2017
    for j in [get_pentaK_path(i) for i in (vs2013,vs2015,vs2017)]:
        cleanup(j)


batch_check()

