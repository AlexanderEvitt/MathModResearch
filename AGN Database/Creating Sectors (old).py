import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from astroquery.mast import Tesscut
from astropy.coordinates import SkyCoord

ralist = pd.read_csv('agn_catalogue.csv', sep=',', usecols=['Right Ascension'],squeeze=True)
declist = pd.read_csv('agn_catalogue.csv', sep=',', usecols=['Declination'],squeeze=True)

sector_column = np.array([['Start']])
for row in range(46000,46001):
    print(row)
    #Return a list of sectors the object was observed
    coord = SkyCoord(ralist[row],declist[row],unit='deg')
    sector_table = Tesscut.get_sectors(coordinates=coord)
    sector_col = sector_table['sector']
    sector_list = []
    for numbers in sector_col:
        sector_list.append(numbers)
    if sector_list == None:
        sector_list = 0
    else:
        sector_string = np.array([[str(sector_list)]])
    
    sector_column = np.concatenate((sector_column,sector_string),axis=0)

np.savetxt('agn_sectors4.csv', sector_column,  fmt='%s', delimiter=',')

#18286-18287
#40600-40601
#45999-46000