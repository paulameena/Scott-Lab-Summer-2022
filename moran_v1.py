
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
    return

def prob_fixation_well_mixed(num_muts, r, N):
    return (1 - (1/r**num_muts))/(1-(1/r**N))

def ave_time_to_fixation():
    return 

def t_plus_well_mixed(r, num_muts, N):
    return (r*num_muts)/(r*num_muts + N - num_muts) * (N-num_muts)/N

def t_minus_well_mixed(r, num_muts, N):
    return (num_muts)/(r*num_muts + N - num_muts) * (N-num_muts)/N 

def pi_fxn_prob(limit, pop_type):
    reserve = 1
    j = 1
    if pop_type == "well-mixed":
        while j <= limit:
            reserve *= t_minus_well_mixed(j)/t_plus_well_mixed(j)
            j += 1
        return reserve
    elif pop_type == "ring":
        while j <= limit:
            reserve *= 
            j += 1
        return reserve 
    elif pop_type == "star":
        while j <= limit:
            reserve *= 
            j += 1
        return reserve 


def sigma_fxn_prob(limit, pop_type):
    reserve = 0
    k = 1
    while k <= limit:
        reserve += pi_fxn_prob(k, pop_type)
