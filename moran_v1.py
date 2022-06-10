
import matplotlib as mpl 
import numpy as np
import sys
import os
import pandas as pd
import test

def run_moran_process(N, r, num_muts, pop_type): 
    ## N is the population size ,
    # r is the relative fitness of muts:wts
    # and num_muts is the initial condition for mutants
    fix_prob = pd.NA
    fix_time = pd.NA
    ##TODO: purpose of this function is to output fixation probability (fix_prob) and fixation time (fix_time)
    # for given input simulation parameters
    return fix_prob, fix_time

def prob_fixation(num_muts,r, N, pop_type):
    if pop_type == "well_mixed" or "ring":
        return prob_fixation_well_mixed(num_muts, r, N)
    else:
        return prob_fixation_other(num_muts, r, N)

def prob_fixation_well_mixed(num_muts, r, N):
    return (1 - (1/r**num_muts))/(1-(1/r**N))

def prob_fixation_other(num_muts, r, N):
   return (1 - (1/r**(2*num_muts)))/(1-(1/r**(2*N))) 

def ave_time_to_fixation():
    return 