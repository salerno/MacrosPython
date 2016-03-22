#!/usr/bin/env python

# to run inside ROOT 
# gSystem->Load("libPyROOT.so");TPython::LoadMacro("HH125_BR.py")

import array
from ROOT import *

def set_palette(name='palette', ncontours=999):
    """Set a color palette from a given RGB list
    stops, red, green and blue should all be lists of the same length
    see set_decent_colors for an example"""

    if name == "gray" or name == "grayscale":
        stops = [0.00, 0.34, 0.61, 0.84, 1.00]
        red   = [1.00, 0.84, 0.61, 0.34, 0.00]
        green = [1.00, 0.84, 0.61, 0.34, 0.00]
        blue  = [1.00, 0.84, 0.61, 0.34, 0.00]
    # elif name == "whatever":
        # (define more palettes)
    else:
        # default palette, looks cool
        stops = [0.00, 0.34, 0.61, 0.84, 1.00]
        red   = [0.00, 0.00, 0.87, 1.00, 0.51]
        green = [0.00, 0.81, 1.00, 0.20, 0.00]
        blue  = [0.51, 1.00, 0.12, 0.00, 0.00]

    s = array.array('d', stops)
    r = array.array('d', red)
    g = array.array('d', green)
    b = array.array('d', blue)

    npoints = len(s)
    TColor.CreateGradientColorTable(npoints, s, r, g, b, ncontours)
    gStyle.SetNumberContours(ncontours)


gStyle.SetPalette(1)
set_palette('gray',40)

#branching ratio H125
H125_BR_H1 = [0.577,0.215,0.0857,0.0632,0.0291,0.0264,0.00228,0.00154,0.000220]
H125_BR_H2 = H125_BR_H1[::-1]
dimHBR = len(H125_BR_H1)

histoBR = TH2F("histoBR","histoBR",dimHBR,0,dimHBR,dimHBR,0,dimHBR)
for i in xrange( dimHBR ) :
    for j in xrange( dimHBR ) :
    	if ( j < -i + dimHBR  ) :
            histoBR.SetBinContent(i+1,j+1,H125_BR_H1[i]*H125_BR_H2[j])
    	    if ( j < -i + dimHBR -1 ) :
                 histoBR.SetBinContent(i+1,j+1,2*H125_BR_H1[i]*H125_BR_H2[j])


c1=TCanvas("c1","c1",1200,1200)
c1.SetLogz(1)

histoBR.Draw("COLZNUM")
histoBR.SetStats(0)
histoBR.SetTitle("Title")
histoBR.GetXaxis().SetTitle("X axis title")
histoBR.GetYaxis().SetTitle("Y axis title")
histoBR.GetZaxis().SetRangeUser(0.00000001,1)
#for 
print H125_BR_H1
print H125_BR_H2



