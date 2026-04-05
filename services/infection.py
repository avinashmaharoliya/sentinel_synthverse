import random

def spread_infection(patients, network, prob=0.2):
    new_infected = []

    for pid, neighbors in network.items():
        if patients[pid]["infected"] == 1:
            for n in neighbors:
                if patients[n]["infected"] == 0:
                    if random.random() < prob:
                        new_infected.append(n)

    for n in new_infected:
        patients[n]["infected"] = 1

    return patients