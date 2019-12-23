import numpy as np
from astropy.io import fits
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

file = 'Gaia_unWISE_AGNs.fits'

hdu_list = fits.open(file)
data = hdu_list[1].data
hdr = hdu_list[1].header

def print_stats():
    print(hdr)
    
def fill(numtargets,filename):
    f = open(filename, "w+")
    f.close()
    
    numrows = numtargets
    cataloguearray = [np.array(['Right Ascension','Declination','Gaia ID','unWISE ID','Parallax','Parallax Error','Proper Motion - Right Ascension','Proper Motion - Right Ascension Error','Proper Motion - Declination','Proper Motion - Declination Error','Parallax Significance','Proper Motion Significance','Galactic E(B-V) Reddening','Number of Observations for G-Band Photometry','Gaia G-Band Mean Magnitude','Gaia BP-Band Mean Magnitude','Gaia RP-Band Mean Magnitude','unWISE W1 Band Magnitude','unWISE W2 Band Magnitude','BP-G Color','BP-RP Color','G-RP Color','G-W1 Color','Gaia-unWISE Separation','W1-W2 Color','G-Band Variation','BP/RP Excess Factor','Astronomic Excess Noise','Goodness-of-fit','Gaia Sources Within 1" Radius','Gaia Sources Within 2" Radius','Gaia Sources Within 4" Radius','Gaia Sources Within 8 Radius','Gaia Sources Within 16" Radius','Gaia Sources Within 32" Radius','Photometric Redshift Predicted','AGN Probability'])]
    for number in range(0,numrows):
        rowlist = []
        for numbers in range(0,37):
            rowlist = rowlist + [hdu_list[1].data[number].field(numbers)]
        cataloguearray = np.append(cataloguearray,[np.array(rowlist)],axis=0)

    np.savetxt(filename, cataloguearray,  fmt='%s', delimiter=',')

    
def fill_southern_targets(numtargets,startposition,filename,cutoff):
    counter = 0
    f = open(filename, "w+")
    
    numrows = numtargets
    cataloguearray = [np.array(['Right Ascension','Declination','Gaia ID','unWISE ID','Parallax','Parallax Error','Proper Motion - Right Ascension','Proper Motion - Right Ascension Error','Proper Motion - Declination','Proper Motion - Declination Error','Parallax Significance','Proper Motion Significance','Galactic E(B-V) Reddening','Number of Observations for G-Band Photometry','Gaia G-Band Mean Magnitude','Gaia BP-Band Mean Magnitude','Gaia RP-Band Mean Magnitude','unWISE W1 Band Magnitude','unWISE W2 Band Magnitude','BP-G Color','BP-RP Color','G-RP Color','G-W1 Color','Gaia-unWISE Separation','W1-W2 Color','G-Band Variation','BP/RP Excess Factor','Astronomic Excess Noise','Goodness-of-fit','Gaia Sources Within 1" Radius','Gaia Sources Within 2" Radius','Gaia Sources Within 4" Radius','Gaia Sources Within 8 Radius','Gaia Sources Within 16" Radius','Gaia Sources Within 32" Radius','Photometric Redshift Predicted','AGN Probability'])]
    np.savetxt(filename, cataloguearray,  fmt='%s', delimiter=',')
    for number in range(0,numrows):
        rowlist = []
        if float(hdu_list[1].data[number+startposition].field("DEC")) < 0 and float(hdu_list[1].data[number+startposition].field("PROB_RF")) > cutoff:
            for numbers in range(0,37):
                rowlist = rowlist + [hdu_list[1].data[number+startposition].field(numbers)]
            cataloguearray = np.append(cataloguearray,[np.array(rowlist)],axis=0)
        else:
            counter = counter + 1
    print(counter)

    np.savetxt(filename, cataloguearray,  fmt='%s', delimiter=',')
    f.close()

def fill_refined(probabilitycutoff,declinationcutoff,brightnesscutoff,file):
    data = hdu_list[1].data
    mask = data['DEC'] < declinationcutoff
    newdata = data[mask]
    mask2 = newdata['PROB_RF'] > probabilitycutoff
    newerdata = newdata[mask2]
    mask3 = newerdata['G'] < brightnesscutoff
    newestdata = newerdata[mask3]
    f = open(file, 'w')
    np.savetxt(file, newestdata,  fmt='%s', delimiter=',')
    f.close()
    
fill_refined(0.939,0,18,'refined_catalogue.csv')