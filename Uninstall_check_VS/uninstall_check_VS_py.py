import os
# 3.5+ support iglob ** recursive
import glob
import shutil


vspath_lists = [
              ("VS2013","C:/Program Files (x86)/Microsoft Visual Studio 12.0/Common7/IDE/Extensions/NVIDIA/Nsight Tegra"),
              ("VS2015","C:/Program Files (x86)/Microsoft Visual Studio 14.0/Common7/IDE/Extensions/NVIDIA/Nsight Tegra"),
              ("VS2017","C:/Program Files (x86)/Microsoft Visual Studio/2017/Enterprise/Common7/IDE/Extensions"),
              ("MSBuild_2013","C:/Program Files (x86)/MSBuild/Microsoft.Cpp/v4.0/v120/Platforms"),
              ("MSBuild_2015","C:/Program Files (x86)/MSBuild/Microsoft.Cpp/v4.0/v140/Platforms"),
              ("MSBuild_2017","C:/Program Files (x86)/Microsoft VisualStudio/2017/Enterprise/Common7/IDE/VC/VCTargets/Platforms"),
           ]


def get_pentaK_path(vspath):
    branch_name = vspath[0]
    install_dir = vspath[1]
    if not os.path.exists(install_dir):
         return None
    
    extension_list = os.listdir(install_dir)
    def find_pentaK(search_path):
        patterns = [ os.path.join(install_dir,search_path,i) for i in ("**\\Nvidia.PentaK*", "Nvidia.PentaK*","*Android-NVIDIA*")]
        #print(patterns)
        return any([glob.glob(pat,recursive=True) for pat in patterns])

    pentak_dir = [ i for i in extension_list if find_pentaK(i)]
    print(install_dir,":",pentak_dir)
    return [os.path.join(install_dir,i) for i in pentak_dir]

def batch_check():
    global vspath_lists
    print([get_pentaK_path(i) for i in vspath_lists])

def cleanup(cleandir):
    for i in cleandir:
        print("delete {} ....".format(i))
        shutil.rmtree(i)

def batch_clean():
    global vspath_lists
    for j in [get_pentaK_path(i) for i in vspath_lists]:
        cleanup(j)


batch_check()

