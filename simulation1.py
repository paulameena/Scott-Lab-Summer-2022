# Tutorial on evolutionary game theory part 2


from bird import Bird
import random
import numpy as np
import pandas as pd
import matplotlib


def initialise():
    """
    Create a population of birds - all dove to begin
    """

    birds = []

    for _ in range(1000):
        birds.append(Bird("dove"))

    return (birds)


def timestep(birds, value, cost):
    """
    Pair up the birds, make them compete
    Then produce next generation, weighted by fitness
    """

    next_generation = []

    random.shuffle(birds)

    for _ in range(1000):

        # pair up random birds to contest
        a, b = random.sample(birds, 2)
        a.contest(b, value, cost)

    # generate next generation
    fitnesses = [bird.fitness for bird in birds]

    draw = random.choices(birds, k=1000, weights=fitnesses)
    next_generation = [bird.spawn() for bird in draw]

    return next_generation


def main():

    birds = initialise()

    rows = []

    V = 4 ; C = 6

    for _ in range(1000):
        
        # add the counts to a new row
        strategy = [bird.strategy for bird in birds]
        n_hawks = strategy.count("hawk")
        n_doves =  strategy.count("dove")
        row = {'n_hawks': n_hawks, 'n_doves': n_doves}
        rows.append(row)

        # run the timestep function
        birds = timestep(birds, V, C)


    # create dataframe and save output

    df = pd.DataFrame(rows)
    df.to_csv('simulation.csv')
    fig = df.plot(y=["n_hawks", "n_doves"]).get_figure()
    fig.savefig('simulation.pdf')

if __name__ == "__main__":
    main()

main()