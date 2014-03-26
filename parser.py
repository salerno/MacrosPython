import os
import glob
from tempfile import mkstemp
from shutil import move
from os import remove, close

def replace(file_path, file_path_out, pattern, subst):
    #Create temp file
    #abs_path = mkstemp()
    #new_file = open(abs_path,'w')
    new_file = open(file_path_out,'w')
    old_file = open(file_path)
    for line in old_file:
        new_file.write(line.replace(pattern, subst))
    #close temp file
    new_file.close()
    old_file.close()
    #Remove original file
    #remove(file_path)
    #Move new file
    #move(abs_path, file_path)


path = '/Users/salerno/Desktop/FinitiCHEF/'
path_out = '/Users/salerno/Desktop/FinitiCHEF/CodeReadFiles/'
##current directory
#for filename in os.listdir(os.getcwd()):
##directory specified in path
#for filename in os.listdir(path):
for filename in glob.glob(os.path.join(path, 'CH*.pdf')):
    # do stuff
    print(filename)
    print(path_out+filename.split('/')[-1])
    replace(filename,path_out+filename.split('/')[-1],'Creator (TeX)','Creator (Rob)')
    print(path_out+filename.split('/')[-1])
    print(path_out+'new'+filename.split('/')[-1])
    replace(path_out+filename.split('/')[-1],path_out+'new'+filename.split('/')[-1],'/Producer (pdfTeX-1.40.14)','')