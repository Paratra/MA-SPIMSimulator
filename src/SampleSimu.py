import numpy as np
from pdb import set_trace as st


class Beads:

    def __init__(self, num_beads, grid_size, sample_reIndex=1.5, medium_reIndex=1.33, seed=42):
        self.num_beads = num_beads # Number of beads to generate
        # self.radius = beads_radius  # Radius of spheres in pixels
        self.grid_size = grid_size  # Size of the ndarray
        self.seed = seed # random seed for reproducibility
        # Initialize the grid
        self.grid = np.zeros((grid_size, grid_size, grid_size))
        self.signal = np.copy(self.grid)
        self.sample_reIndex = sample_reIndex
        self.medium_reIndex = medium_reIndex



    def get_sample(self):
        # Generate sphere centers randomly inside the ellipsoid
        if self.seed == 'None':
            pass
        else:
            np.random.seed(self.seed)  # for reproducibility
            
            
        for _ in range(self.num_beads):
            k, j, i = np.random.randint(dn.shape[0]), np.random.randint(dn.shape[1]), np.random.randint(dn.shape[2])
            self.signal[k, j, i] = self.medium_reIndex
            self.dn[k, j, i] = self.sample_reIndex

        return self.grid, self.signal

class Ellipsoid:
    '''
    example: 
        ellipsoid = Ellipsoid(num_spheres=500, elli_axis=(200, 105, 105), spheres_radius=5, grid_size=512, seed=42)
        grid = ellipsoid.get_sample()
    '''

    def __init__(self, num_spheres, elli_axis, spheres_radius, grid_size, sample_reIndex=1.5, medium_reIndex=1.33, seed=42):

        self.num_spheres = num_spheres # Number of spheres to generate
        (self.a, self.b, self.c) = elli_axis  # Semi-axes of the ellipsoid within the 512 grid
        self.radius = spheres_radius  # Radius of spheres in pixels
        self.grid_size = grid_size  # Size of the ndarray
        self.seed = seed # random seed for reproducibility
        # Initialize the grid
        self.grid = np.zeros((grid_size, grid_size, grid_size))
        self.signal = np.copy(self.grid)
        self.sample_reIndex = sample_reIndex
        self.medium_reIndex = medium_reIndex

    def in_ellipsoid(self, x, y, z):
        """Check if a point (x, y, z) is inside the ellipsoid defined by semi-axes (a, b, c)."""
        return (x/self.a)**2 + (y/self.b)**2 + (z/self.c)**2 <= 1

    def draw_sphere(self, center):
        """Draw a sphere in a 3D grid at specified center with given radius."""
        x0, y0, z0 = center
        for x in range(max(0, x0-self.radius), min(self.grid_size, x0+self.radius+1)):
            for y in range(max(0, y0-self.radius), min(self.grid_size, y0+self.radius+1)):
                for z in range(max(0, z0-self.radius), min(self.grid_size, z0+self.radius+1)):
                    if (x-x0)**2 + (y-y0)**2 + (z-z0)**2 <= self.radius**2:
                        self.grid[x, y, z] = self.sample_reIndex
                        self.signal[x, y, z] = self.medium_reIndex

    def get_sample(self):
        # Generate sphere centers randomly inside the ellipsoid
        if self.seed == 'None':
            pass
        else:
            np.random.seed(self.seed)  # for reproducibility
            
        for ind in range(self.num_spheres):
            while True:
                # print(ind)
                # Generate random center within the grid
                x = np.random.randint(0, self.grid_size)
                y = np.random.randint(0, self.grid_size)
                z = np.random.randint(0, self.grid_size)
                # Adjust centers to be relative to the center of the grid
                if self.in_ellipsoid(x - self.grid_size//2, y - self.grid_size//2, z - self.grid_size//2):
                    self.draw_sphere((x, y, z))
                    break

        return self.grid, self.signal

