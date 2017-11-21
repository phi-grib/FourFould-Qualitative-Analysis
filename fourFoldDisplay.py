# -*- coding: utf-8 -*-

##    Description    Tools for qualitative endpoints
##                   
##    Authors:      Kevin Pinto Gil (kevin.pinto@upf.edu)
##                  Manuel Pastor (manuel.pastor@upf.edu) 
##
##    Copyright 2013 Manuel Pastor
##
##    This file is part of eTOXlab.
##
##    eTOXlab is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation version 3.
##
##    eTOXlab is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with eTOXlab.  If not, see <http://www.gnu.org/licenses/>.

import urllib
import os
import sys
import getopt
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

def FourfoldDisplay(TP, TN, FP, FN, label, name, endpoint):
    """ Draws confusion matrix graphical representaion

    """
    print TP, TN, FP, FN
    sensitivity = TP/(TP+FN)
    specificity = TN/(TN+FP)
    print 'sens', sensitivity, 'spec', specificity
    width = np.pi / 2.0
    theta = np.radians([0,90,180,270])
    table = [FP,TP,FN,TN]
##    plt.figure("RF-Qualitative_validation")
    plt.figure()
    plt.clf()
    ax = plt.subplot(121, polar=True, adjustable='box', aspect=1)    
    bars = ax.bar(theta, table, width=width, color=["red", "lightblue", "red", "lightblue"])
##    plt.title( label )

    ax.set_xticklabels(["","FP (%s) \n\n" % str(int(FP)), "",  "TP (%s) \n\n" % str(int(TP)), "", "\n\n\nFN (%s)" % str(int(FN)), 
                        "",  "\n\n\nTN (%s)" % str(int(TN))], fontsize=14)
    ax.set_yticks([])
    ax.grid(False)
    ax.axes.spines['polar'].set_visible(False)
    
    ax2 = plt.subplot(122, adjustable='box', aspect=3)
    plt.ylim([0,1])
##    plt.title(endpoint+'\n')
    
    bar_width = 0.5
    y = [0, sensitivity, specificity, 0]
    index = np.arange(4)
    ax2.bar(index, y, bar_width, color=["lightgreen","lightgrey"])
    #ax.offset(0.5)
    plt.xticks( index + bar_width / 2.0, ("", 'Sensitivity', 'Specifity', ""))
    
    plt.savefig(name)

def usage ():
    """Prints in the screen the command syntax and argument"""
    print '44Display.py -a TP -b  TN -c FP -d FN -l label -n name'
    print '44Display.py -a 10 -b 50 -c 20 -d 50 -l "PLS Predicted Confusion Matrix" -n RF_predicted_confusion_matrix.png -e Nonneoplasic'
    sys.exit(1)

def main ():

    TP = None
    TN = None
    FP = None
    FN = None
    label = None
    name = None
    endpoint = None

    try:
       opts, args = getopt.getopt(sys.argv[1:],'a:b:c:d:l:n:e:')
    except getopt.GetoptError:
        print "Arguments not recognized"
        usage()
    
    if not len(opts):
        print "Arguments not recognized"
        usage()

    if len(opts)>0:
        for opt, arg in opts:
            if opt in '-a':
                TP = arg
                TP = float(TP)
            elif opt in '-b':
                TN = arg
                TN = float(TN)
            elif opt in '-c':
                FP = arg
                FP = float(FP)
            elif opt in '-d':
                FN = arg
                FN = float(FN)
            elif opt in '-l':
                label = arg
            elif opt in '-n':
                name = arg
            elif opt in '-e':
                endpoint = arg
             
    if TP == None and TN == None and FP == None and FN == None and label == None and name == None and endpoint == None:
        usage()
        print "Error. Missing arguments"

    FourfoldDisplay(TP, TN, FP, FN, label, name, endpoint)
    
if __name__ == '__main__':    
    main()
