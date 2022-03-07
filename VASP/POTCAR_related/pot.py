#!/home/jinho93/miniconda3/bin/python

'''
-----------------------------------------------------------------------------
Description: 

A script to generate VASP input files including INCAR, KPOINTS, POTCAR and
vasp_job.sh script.

Important notes:

(1) Before running this script, check if your VASP_Pseudopotentials library
has following structure:

        VASP_Pseudopotentials (root directory)
                          |
       ---------------------------------------
      |         |         |         |         |
     PAW     PAW_GGA   PAW_PBE     US       US_GGA

(2) Specify the location of VASP_pseudopotentials library of your machine.
You need to find the following line: 

PPS_dirs_path = ""

and modify it, like:
PPS_dirs_path = "/home/shuang/softwares/VASP/Pseudopotentials"

(3) To generate the POTCAR, the geometry file POSCAR is needed. Make sure 
it's in the working directory!

(4) The vasp_job.sh script generated by VASPIN_GEN.py is a template of job 
script to run VASP. You can modify the part of 'VASP_Run_scprit generator' 
based on your machine environment.

-----------------------------------------------------------------------------
Author: ShuangLeung (sleung1924@gmail.com)                         
Date of last version: 2020/03/30
-----------------------------------------------------------------------------
'''

import os, stat, sys, re, linecache

#========================================= POTCAR_generator =========================================

print("="*92)

# set the location of VASP pseudopotentials
# Add the absolute path of VASP_pseudopotentials library of your machine!!! 
# For example: PPS_dirs_path = "/home/shuang/softwares/VASP/Pseudopotentials"
PPS_dirs_path = "/opt/vasp/Potential"

# initialize POTCAR file
if os.path.exists("POTCAR"):
    with open("POTCAR", "r+") as f:
        f.truncate()

# detect the POSCAR file
if os.path.exists("POSCAR"):
    element_types = (linecache.getline('POSCAR',6)).split( ) # obtain the element_types in POSCAR

else:
    print("POSCAR file doesn't exist, generating POTCAR fails! Please try again!\n")
    sys.exit(0)

print("+"+"-"*90+"+")

# select the pseudopotentials(PP)
inputstr = input("Pseudopotentials options:\n\n %s %s %s %s %s %s" % ("1: potpaw_LDA.54;\n",
								      "2: PAW_PW91;\n",
								      "3: POT_GGA_PAW_PBE_54;\n",
                                                                      "4: US_LDA;\n",
								      "5: US_GGA.\n",
								      "\n--->>Enter your option:"))
PP_option = inputstr.strip()
PP_dict = {"1":"potpaw_LDA.54","2":"PAW_GGA","3":"potpaw_PBE.54","4":"US","5":"US_GGA"}
# set the default PP option
if PP_option not in PP_dict.keys():
    print("\n*** WARNING: The input has syntax errors. Select the PAW_PBE PP automatically. ***\n")
    PP_option = "3"

print("+"+"-"*90+"+")

# get the path of PP ("PAW_LDA/PAW_GGA/PAW_PBE/US/US_GGA") directory 
# and the names of its sub-folders
PP_dirs_path = os.path.join(PPS_dirs_path,'%s'% PP_dict[PP_option])
PP_dirs = os.listdir(PP_dirs_path)
# specify the PP_version of the corresponding element
print("We note that your POSCAR has following elements: %s" % (' '.join(element_types)))

for element in element_types:
    PP_versions = []
    for PP_dir in PP_dirs:
        matchObj = re.match(r'%s[0-9_.]|%s\b'%(element,element),"%s"%PP_dir)
        if matchObj != None:
            PP_versions.append(PP_dir)

    # For the element which has more than one PP_version, selection is needed.
    if len(PP_versions) > 1:
        print("\nFor element %s, several versions of pseudopotentials are available:\n"%element)
        # version counts
        version_count = 1
        version_options = {}
        for v in PP_versions:
            version_options["%s"%version_count] = v
            print("%d:%s"%(version_count,v))
            version_count +=1

        inputstr = input("\n--->>>Your option:")
        version_option = inputstr.strip()
        # set the default version_option
        if version_option not in version_options.keys():
	        print("\n*** WARNING: The input has syntax errors. Select the standard version automatically. ***\n")
	        version_option = "1"

        # get the POTCAR path of specialized PP version
        potcar_dirs_path = os.path.join(PP_dirs_path,version_options["%s"%version_option])

    else:
        potcar_dirs_path = os.path.join(PP_dirs_path,PP_versions[0])
        
    pot_file = os.path.join(potcar_dirs_path,"POTCAR")

    #write the POTCAR file
    with open('POTCAR','a') as f_total:
        f = open("%s"%pot_file,'r')
        file_detial = f.read()
        f_total.write(file_detial)

print("+"+"-"*90+"+\n")