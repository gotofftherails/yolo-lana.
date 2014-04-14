
# Author: chris guest
# run splat script for QTH files in current dir starting with specified prefix.
import sys
import create_output
import os
import glob


myglob = '*.qth'
if len(sys.argv)>1:
    myglob = sys.argv[1] + myglob
i=0
for filename in glob.glob('*.qth'):
    stub = filename[:-4]
    create_output.create(stub)
    i+=1
    if i>300:
        break
  
print '%d files generated.' % i


#convert to world file

png2wld =' bash kml2wld_aus.sh .'


print 'creating world files...'

os.system(png2wld)


myglob = '*.qth'
if len(sys.argv)>1:
    myglob = sys.argv[1] + myglob
i=0
for filename in glob.glob('*.qth'):
    stub = filename[:-4]
    create_output.convert(stub)
    i+=1
    if i>300:
        break
