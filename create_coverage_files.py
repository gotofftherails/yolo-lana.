import os

#filename = 'MelbourneJJJ'



def create(file_name):
	#create ppm and KML
	cpk = 'splat -t ' + file_name + ' -o -c 2.0 '+ file_name + '.ppm -ngs -kml -metric'
	print cpk
	#resize ppm file 
	resize = 'pnmscale -xsize 1200 ' + file_name + '.ppm' 
	
	#make opaque here


	#Convert ppm to png
	p2p = 'pnmtopng ' + file_name + ' > ' + file_name + '.png' 
	print p2p

	#White to transparent
	w2t = 'convert -transparent "#FFFFFF" ' + file_name + '.png ' + file_name +'.png'


	#remove trans file
	rm_trans = 'rm ' + file_name +'_trans.ppm'

	#rewrite KML
	rw_kml = "sed -i 's/.ppm/.png/g' " + file_name + ".kml"

	#convert to GeoTIFF


	try:
		print 'Creating coverage map'
		os.system(cpk)
		print 'Coverage map created'
	except:
		print 'Coverage map failed...'	

		'Converting white to transparency failed' 
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
			
	try:
		print 'Cleaning file'
		os.system(rm_trans)
		print 'File cleaned'
	except:
		print 'Cleaning file failed'

	try:
		print 'Rewriting KML'
		os.system(rw_kml)
		print 'KML rewritten'
		print 'PNG filename:' + file_name +'.png'
		print 'KML filename:' + file_name +'.kml'
	except:
		print 'Rewriting KML failed'

