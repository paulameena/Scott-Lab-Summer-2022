
from appscript import k
import matplotlib as mpl 
import numpy as np
import sys
import os
import pandas as pd
import test
from scipy import special, optimize, integrate, stats

def moran_process(num_muts, r, N, pop_type): 
    ## N is the population size ,
    # r is the relative fitness of muts:wts
    # and num_muts is the initial condition for mutants
    if pop_type == "well-mixed":
        Tpos_func = lambda j: r*j/(r*j + N - j) * (N-j)/N
        Tneg_func = lambda j: (N-j)/(r*j+N-j)* j/N
    elif pop_type == "ring":
        Tpos_func = lambda j: r/(j*r + N -j) if j != 0 | N else 0
        Tneg_func = lambda j: 1/(j*r + N -j) if j != 0 | N else 0
    elif pop_type == "star":
        Tpos_func = lambda j: (1/N-1) * (j*(N-j-1)*r**2)/(N*(N-1)+2*N*j*(r-1)+j*(j+1)*(r-1)**2)
        Tneg_func = lambda j: lambda j: (1/N-1) * (j*(N-j-1))/(N*(N-1)+2*N*j*(r-1)+j*(j+1)*(r-1)**2) 
    else:
        Tpos_func = 0
        Tneg_func = 0
    fix_prob, fix_time = np.array(), np.array()
    for i in range(num_muts, N):
        fix_prob.append(fix_prob(i, N, Tneg_func, Tpos_func))
        fix_time.apend(fix-time(i, N, Tneg_func, Tpos_func))
    return fix_prob, fix_time

def fix_prob(l, N, Tneg_func, Tpos_func):
    first = lambda j,k: np.product([Tneg_func(x)/Tpos_func(x) for x in range(j,k+1)])
    second = lambda k, top: np.sum([first(k, z) for z in range(k, top)])
    numerator = 1 + second(1, l)
    denominator = 1 + second(1, N)
    return numerator/denominator 

def fix_time(l, N, Tneg_func, Tpos_func):
    first = lambda m, k: np.product([Tneg_func(x)/Tpos_func(x) for x in range(m, k+1)])
    second = lambda l,k: np.sum([first(l+1, y) * fix_prob(y, N, Tneg_func, Tpos_func)/Tpos_func(y) for y in range(l,k+1)])
    third = lambda k,top: np.sum([second(k, z) for z in range(k, top)])
    return third(l, N)

moran_process(1, 1.1, 50, "well-mixed")

