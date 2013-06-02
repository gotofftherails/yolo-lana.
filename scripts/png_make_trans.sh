# script to convert pngs with whitebackgrounds to transparencies.
# useful for making map overlays
# author: chris guest
# looks for input files in ./*.png 
# outputs to ./trans/*.png
for img in *.png
  do echo "Processing $img  file.."
	convert $img -transparent white trans/$img
done
