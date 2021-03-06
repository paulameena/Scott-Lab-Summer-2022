
import matplotlib.pyplot as plt
import numpy as np

def moran_process(num_muts, r, N, pop_type): 
    ## N is the population size ,
    # r is the relative fitness of muts:wts
    # and num_muts is the initial condition for mutants
    if pop_type == "well-mixed":
        Tpos_func = lambda j: r*j/(r*j + N - j) * (N-j)/N
        Tneg_func = lambda j: (N-j)/(r*j+N-j)* j/N
    elif pop_type == "ring":
        Tpos_func = lambda j: r/(j*r + N -j) if j != 0 | N else 0 # was 0 but then there's a divide by 0 error... hmmmq
        Tneg_func = lambda j: 1/(j*r + N -j) if j != 0 | N else 0
    elif pop_type == "star":
        Tpos_func = lambda j: (1/N-1) * (j*(N-j-1)*r**2)/(N*(N-1)+2*N*j*(r-1)+j*(j+1)*(r-1)**2)
        Tneg_func = lambda j: (1/N-1) * (j*(N-j-1))/(N*(N-1)+2*N*j*(r-1)+j*(j+1)*(r-1)**2) 
    else:
        Tpos_func = 0
        Tneg_func = 0
    fix_prob, fix_time = fix_prob_func(1, N, Tneg_func, Tpos_func), fix_time_func(1, N, Tneg_func, Tpos_func)
    #for i in range(num_muts, N):
       # fix_prob.append(fix_prob_func(i, N, Tneg_func, Tpos_func))
        #fix_time.append(fix_time_func(i, N, Tneg_func, Tpos_func))
    return fix_prob, fix_time

def fix_prob_func(l, N, Tneg_func, Tpos_func):
    first = lambda j,k: np.product([Tneg_func(x)/Tpos_func(x) for x in range(j,k)])
    second = lambda k, top: np.sum([first(k, z) for z in range(k, top)])
    numerator = 1 + second(1, l)
    denominator = 1 + second(1, N)
    return numerator/denominator 

def fix_time_func(l, N, Tneg_func, Tpos_func):
    first = lambda m, k: np.product([(Tneg_func(x)) / (Tpos_func(x)) for x in range(m, k)])
    second = lambda l,k: np.sum([first(l+1, y) * fix_prob_func(y, N, Tneg_func, Tpos_func)/Tpos_func(y) for y in range(l,k)])
    third = lambda k,top: np.sum([second(k, z) for z in range(k, top)])
    return third(l, N)

def simulate_moran_process(start_adv, final_adv, increment, N, pop_type):
    fix_prob_array = []
    fix_time_array = []
    adv_array = []
    for r in np.arange(start_adv, final_adv, increment):
        adv_array.append(r)
        intermed = moran_process(1, r, N, pop_type)
        fix_prob_array.append(intermed[0])
        fix_time_array.append(intermed[1])
    return adv_array, fix_prob_array, fix_time_array

def plot_moran_process(axis, advantages, fix_probs, fix_times):
    axis[0].plot(advantages, fix_probs)
    axis[1].plot(advantages, fix_times)
    return


def run():
    figure, axis = plt.subplots(2,1)
    #plt.ticklabel_format(style='sci')
    axis[0].set_ylabel("Fixation Probabilities")
    axis[1].set_ylabel("Fixation Times (generations)")
    advs1, probs1, times1 = simulate_moran_process(1, 5.0, 0.2, 50, "well-mixed")
    plot_moran_process(axis, advs1, probs1, times1)
    advs2, probs2, times2 = simulate_moran_process(1, 5, 0.2, 50, "ring")
    plot_moran_process(axis, advs2, probs2, times2)
    advs3, probs3, times3 = simulate_moran_process(1, 5, 0.2, 50, "star") 
    plot_moran_process(axis, advs3, probs3, times3)
    plt.legend(["well-mixed", "star"])
    plt.show()
    return 


run()





