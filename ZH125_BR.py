#!/usr/bin/env python

# to run inside ROOT 
# gSystem->Load("libPyROOT.so");TPython::LoadMacro("ZH125_BR.py")

from ROOT import *

gROOT.Reset()
gStyle.SetPalette(1)

#branching ratio H125
H125_BR = [0.577,0.215,0.0857,0.0632,0.0291,0.0264,0.00228,0.00154,0.000220]
Z_BR = [0.55,0.20,0.16,0.06,0.03]
Z_BR = Z_BR[::-1]


dimHBR = len(H125_BR)
dimZBR = len(Z_BR)

histoBR = TH2F("histoBR","histoBR",dimHBR,0,dimHBR,dimZBR,0,dimZBR)
for i in xrange( dimHBR ) :
    for j in xrange( dimZBR ) :
    	    #histoBR.SetBinContent(i+1,j+1,H125_BR[i]*Z_BR[j])
            histoBR.SetBinContent(i+1,j+1,H125_BR[i]*Z_BR[j])

c1=TCanvas("c1","c1",1200,600)
c1.SetLogz(1)

histoBR.Draw("COLZNUM")
histoBR.SetStats(0)
histoBR.SetTitle("Title")
histoBR.GetXaxis().SetTitle("X axis title")
histoBR.GetYaxis().SetTitle("Y axis title")
histoBR.GetZaxis().SetRangeUser(0.00000001,1)
