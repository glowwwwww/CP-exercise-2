import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

class randomwalk_generator():
    """
    randomwalk number generator with random numbers

    Attributes:
        n_particle (int): numbers of particle doing the random walk    
        n_jump (int): numbers of steps simulated    
    """
    def __init__(self, n_particle, n_jump):
        self.n_particle = n_particle
        self.n_jump = n_jump
    
    def __call__(self, seed):
        """
        generate the distance of each particle for random walk 
        after n steps as ndarray of n_particle*n_jump
        
        Attributes:
            seed(int): seed of the random generator
        Return:
            ndarray
        """
        rng = np.random.default_rng(seed)
        steps = rng.integers(2, size = (self.n_particle, self.n_jump))*2-1
        dist = np.zeros_like(steps)
        for i in range(self.n_jump):
            dist[:,i] = np.sum(steps[:,:i], axis = 1) 

        return dist
