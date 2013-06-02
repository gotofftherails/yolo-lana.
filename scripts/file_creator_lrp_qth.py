
# Grab data from an ABC.net.au  CSV file
# Usage :
# python file_creator_lrp_qth.py AMTowers.CSV
#
# Create the QTH & LRP files needed for Splat!

# Author: chris guest

"""
Name = [Area]+[Callsign]

Frequency
Antenna Height
Antenna Pattern
MAX EIRP
Lat - Strip trailing character and preserve space
Long - Strip trailing character and preserve space

Build QTH file - four lines /n

Name
Lat (-ve)
Long
Antenna height - must have m

Build lrp file

15.000 ; Earth Dielectric Constant (Relative permittivity)
0.005 ; Earth Conductivity (Siemens per meter)
301.000 ; Atmospheric Bending Constant (N-units)
300.000 ; Frequency in MHz (20 MHz to 20 GHz)
5 ; Radio Climate (5 = Continental Temperate)
0 ; Polarization (0 = Horizontal, 1 = Vertical)
0.5 ; Fraction of situations (50% of locations)
0.5 ; Fraction of time (50% of the time)
qth and lrp to have the same name
"""

import csv 
import sys
from decimal import Decimal

csv_filename = sys.argv[1]
reader = csv.reader(file(csv_filename), delimiter=',')
header = reader.next()
print header

# ['Area Served', 'Callsign', 'Frequency(kHz)', 'Purpose', 'Polarisation', 'Mast Height (m)', 'Antenna Pattern', 'Maximum CMF (V)', 'Transmitter Power (W)', 'Technical Specification Number', 'Licence Number', 'Site Id', 'Site Name', 'Zone', 'Easting', 'Northing', 'Latitude', 'Longitude', 'State', 'BSL', 'Licence Area', 'Licence Area ID', 'Hours of Operation', 'Status']

prefix = csv_filename.replace('Towers.csv','')
headerMap=dict([(h,i) for i,h in enumerate(header)])
headerMapInv=dict([(i,h) for i,h in enumerate(header)])
print headerMap
print headerMapInv
frequencyType = {'Frequency(kHz)' : 'K', 'Frequency(MHz)': 'M',}[header[2]]
frequencyidx = 2

mastheightidx =  headerMap.get('Antenna Height (m)', 0) or headerMap.get('Antenna Height', 0) or headerMap.get('Mast Height (m)', 0)

erpidx = headerMap.get('Maximum ERP (W)', 0) or headerMap.get('ERP(W)', 0)

i = 0
for row in reader:
    print row[headerMap['Callsign']]
    #print '%r' % row
    if 'JJJ' in row[headerMap['Callsign']]:

        base_filename = '%s_%s_%s' % (prefix, row[headerMap['Area Served']].replace(' ','').replace('/',''), row[headerMap['Callsign']])
        lat = '-' + row[headerMap['Latitude']].strip().replace('S','')
        lon = '-' + row[headerMap['Longitude']].strip().replace('E','')
        # height = row[headerMap['Mast Height (m)']].strip() + 'm'
        height = row[mastheightidx].strip() + 'm'
        g = file('%s.qth' % base_filename, 'w')
        print >> g, base_filename
        print >> g, lat
        print >> g, lon
        print >> g, height
        g.close()

        g = file('%s.lrp' % base_filename, 'w')
        #freq = Decimal(row[headerMap['Frequency(kHz)']]) 
        freq = Decimal(row[2])
        if frequencyType=='K':
            freq = freq/1000
        erp = Decimal(row[erpidx])
        print 'erp = idx%r = %s' % (erpidx, erp)

        print >> g, """15.000 ; Earth Dielectric Constant (Relative permittivity)
0.005 ; Earth Conductivity (Siemens per meter)
301.000 ; Atmospheric Bending Constant (N-units)
%.3f; Frequency in MHz (20 MHz to 20 GHz)
5 ; Radio Climate (5 = Continental Temperate)
1 ; Polarization (0 = Horizontal, 1 = Vertical)
0.5 ; Fraction of situations (50%% of locations)
0.5 ; Fraction of time (50%% of the time)
%.6f ; ERP
""" % (freq, erp)
        g.close()
    
        #i+=1
        if i>10:
             break


