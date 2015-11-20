# Brian Blaylock
# Summer 2015

# Download and plot observed soundings on a SkewT diagram with 
# data from the Wyoming sounding website http://weather.uwyo.edu/upperair/sounding.html
# Requires:
#     skewt module for ploting you can download and view documentation here: https://pypi.python.org/pypi/SkewT
#     BeautifulSoup which is used for HTML parsing: http://www.crummy.com/software/BeautifulSoup/

from skewt import SkewT
import urllib2
from bs4 import BeautifulSoup

stn = '72572' # this is the id number for KSLC
year = '2015'
month= '06'
day  = '18'
hour = '00' # hour in UTC, 00 and 12 z usually available


# Download, process and add to plot the Wyoming Data
# 1)
# Wyoming URL to download Sounding from
url = 'http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE=TEXT%3ALIST&YEAR='+year+'&MONTH='+month+'&FROM='+day+hour+'&TO='+day+hour+'&STNM='+stn
content = urllib2.urlopen(url).read()

# 2)
# Remove the html tags
soup = BeautifulSoup(content)
data_text = soup.get_text()

# 3)
# Split the content by new line.
splitted = data_text.split("\n",data_text.count("\n"))

#4)
# Must save the processed data as a .txt file to be read in by the skewt module.
# Write this splitted text to a .txt document. Save in current directory.
Sounding_dir = './'
Sounding_filename = str(stn)+'.'+str(year)+str(month)+str(day)+str(hour)+'.txt'
f = open(Sounding_dir+Sounding_filename,'w')
for line in splitted[4:]:
    f.write(line+'\n')
f.close()   

#5) 
# Add skewt data to plot
S = SkewT.Sounding(filename=Sounding_dir+Sounding_filename)
S.make_skewt_axes(tmin=-40.,tmax=50.,pmin=100.,pmax=1050.)
S.add_profile(bloc=0)
parcel=S.get_parcel()
S.lift_parcel(*parcel)
