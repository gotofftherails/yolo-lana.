!/bin/sh

# Markus Neteler, 2008
# This script was found on this page http://gis.stackexchange.com/questions/30064/how-to-merge-many-individual-kml-layers-into-one


# merge KML files

PROG=`basename $0`

if [ $# -lt 1 ] ; then
 echo "Merges KML files together (mosaik)"
 echo "Usage:"
 echo "  $PROG *.kml"
 echo "  $PROG a.kml b.kml c.kml"
 echo "At then end of the merge you can select a new name"
 exit 1
fi

LIST="$@"
OUT=file_merged

rm -f $OUT.kml

ogr2ogr -f KML $OUT.kml $1
shift

for i in `seq 1 $#` ; do
  echo "Appending #$i: $1"
  ogr2ogr -f KML -update -append $OUT.kml $1 -nln $OUT `basename $1 .kml`
  shift
done

echo "Written: $OUT.kml"

echo -n "Enter file name for new KML (or CTRL-C): "
read NEW
NEW=`basename $NEW .kml`
mv $OUT.kml $NEW.kml

echo "Written as: $NEW.kml"
