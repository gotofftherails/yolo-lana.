# Author: jamie
import os


#filename = 'MelbourneJJJ'



def create(file_name):
  #create ppm and KML
	cpk = 'splat -t ' + file_name + ' -c 2.0 -o '+ file_name + '.ppm -ngs -kml -metric -d ..'
	print cpk
	#resize ppm file 
	resize = 'pnmscale -xsize 1200 ' + file_name + '.ppm' 
	
	#make opaque here


	#Convert ppm to png
	p2p = 'pnmtopng ' + file_name + '.ppm > ' + file_name + '.png' 
	print p2p

	#White to transparent
	w2t = 'convert -transparent "#FFFFFF" ' + file_name + '.png ' + file_name +'.png'


	#rewrite KML
	rw_kml = "sed -i 's/.ppm/.png/g' " + file_name + ".kml"

	#convert to GeoTIFF


	try:
		print 'Creating coverage map'
		print cpk
		os.system(cpk)
		print 'Coverage map created'
	except:
		print 'Coverage map failed...'	
 
	try:
		print 'Converting ppm to png'
		os.system(p2p)
		print 'Converted ppm to png'

	except:
		print 'Failed converting ppm to png'
	try:
		print 'Converting white to transparency'
		os.system(w2t)
		print 'Converted white to transparency'
	except:
		print 'Converting to white transparency failed'


	try:
		print 'Rewriting KML'
		os.system(rw_kml)
		print 'KML rewritten'
		print 'PNG filename:' + file_name +'.png'
		print 'KML filename:' + file_name +'.kml'
	except:
		print 'Rewriting KML failed'


