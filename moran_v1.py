
from appscript import k
import matplotlib as mpl 
import numpy as np
import sys
import os
import pandas as pd
import test
from scipy import special, optimize, integrate

def run_moran_process(num_muts, r, N, pop_type): 
    ## N is the population size ,
    # r is the relative fitness of muts:wts
    # and num_muts is the initial condition for mutants
    fix_prob, fix_time = 0,0
    return fix_prob, fix_time

def fix_prob(l, N, r, Tneg_Tpos_func):
    first = lambda j,k: np.product([Tneg_Tpos_func(x) for x in range(j,k+1)])
    second = lambda k, top: np.sum([first(k, z) for z in range(k, top)])
    numerator = 1 + second(1, l)
    denominator = 1 + second(1, N)
    return numerator/denominator 

def well_mixed_prob(l, N, r):
    return fix_prob(l, N, r, lambda x: 1/r)

def ring_prob(l,N,r):
    return well_mixed_prob(l, N, r)

def star_prob(l,N,r):
    return fix_prob(l, N, r, lambda x: 1/r**2)

def test_fix_prob():
    x= round(well_mixed_prob(1, 50, 2), 3)
    print(x)
    assert(x == 0.500)
    y = round(star_prob(1, 50,2), 3)
    print(y)
    assert(y == 0.750)
    return

test_fix_prob()

