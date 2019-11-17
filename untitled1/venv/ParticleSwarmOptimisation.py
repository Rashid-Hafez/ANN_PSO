
# apply the position formulae to the whole vector containing the weights, its just adding stuff
# PSO calls function with particle parameters, the PSO calls the function with the Paricle vector
# PSO gives an array
# the function gives the answer

# position are the weights

# the answer is contained in the particle

# the global best particle contains the right answer but not the weights,
# we dont know the weight/position of the particle

# returns the best vector which it could find
from __future__ import division
import random
import math


# --- COST FUNCTION
# function we are attempting to optimize (minimize)
from base64 import main


def func1(x):
    total = 0
    for i in range(len(x)):
        total += x[i] ** 2
    return total


# --- MAIN
class Particle:
    def __init__(self, x0):
        self.position_i = []  # particle position/weight
        self.velocity_i = []  # particle velocity
        self.pos_best_i = []  # best position individual
        self.err_best_i = -1  # best error individual
        self.err_i = -1  # error individual

        for i in range(0, num_dimensions):
            self.velocity_i.append(random.uniform(-1, 1))
            self.position_i.append(x0[i])

    # evaluate current fitness
    def evaluate(self, costFunc):
        self.err_i = costFunc(self.position_i)

        # check to see if the current position is an individual best
        if self.err_i < self.err_best_i or self.err_best_i == -1:
            self.pos_best_i = self.position_i
            self.err_best_i = self.err_i

    # update new particle velocity
    def update_velocity(self, pos_best_g):
        w = 0.5  # constant inertia weight (how much to weigh the previous velocity)
        c1 = 1  # cognative constant
        c2 = 2  # social constant

        for i in range(0, num_dimensions):
            r1 = random.random()
            r2 = random.random()

            vel_cognitive = c1 * r1 * (self.pos_best_i[i] - self.position_i[i])
            vel_social = c2 * r2 * (pos_best_g[i] - self.position_i[i])
            self.velocity_i[i] = w * self.velocity_i[i] + vel_cognitive + vel_social

    # update the particle position based off new velocity updates
    def update_position(self, bounds1):
        for i in range(0, num_dimensions):
            self.position_i[i] = self.position_i[i] + self.velocity_i[i]

            # adjust maximum position if necessary
            if self.position_i[i] > bounds1[i][1]:
                self.position_i[i] = bounds1[i][1]

            # adjust minimum position if neseccary
            if self.position_i[i] < bounds1[i][0]:
                self.position_i[i] = bounds1[i][0]


class PSO:
    def __init__(self, costFunc, x0, bounds, num_particles, maxiter):
        global num_dimensions

        num_dimensions = len(x0)
        err_best_g = -1  # best error for group
        pos_best_g = []  # best position for group

        # establish the swarm
        swarm = []
        for i in range(0, num_particles):
            swarm.append(Particle(x0))

        # begin optimization loop
        i = 0
        while i < maxiter:
            # print i,err_best_g
            # cycle through particles in swarm and evaluate fitness
            for j in range(0, num_particles):
                swarm[j].evaluate(costFunc)

                # determine if current particle is the best (globally)
                if swarm[j].err_i < err_best_g or err_best_g == -1:
                    pos_best_g = list(swarm[j].position_i)
                    err_best_g = float(swarm[j].err_i)

            # cycle through swarm and update velocities and position
            for j in range(0, num_particles):
                swarm[j].update_velocity(pos_best_g)
                swarm[j].update_position(bounds)
            i += 1

        # print final results
        print('FINAL:')
        print (pos_best_g)
        print (err_best_g)

    main()

# --- EXECUTE

initial = [1, 1]  # initial starting location [x1,x2...]
bounds = [(-2, 2), (-2, 2)]  # input bounds [(x1_min,x1_max),(x2_min,x2_max)...]
PSO(func1, initial, bounds, num_particles=1, maxiter=10)