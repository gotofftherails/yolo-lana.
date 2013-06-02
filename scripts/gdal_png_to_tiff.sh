# script to convert pngs to  geotiff files
# author: chris guest
# looks for input files in ./*.png 
# outputs geotifs to ./*.tif
for img in *.png
do 
  baseN=$(basename $img .png)
	echo "img: $img base $baseN"
	gdalwarp $img $baseN.tif
done
