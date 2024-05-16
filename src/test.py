from biobeam import SimLSM_Cylindrical
import numpy as np
from pdb import set_trace as st
import tifffile as tf 
import matplotlib.pyplot as plt
from tqdm import tqdm
from utils import Ellipsoid

# dn = np.zeros((512, 512, 512))

# signal = np.zeros_like(dn)

# # some point sources
# np.random.seed(0)
# for _ in range(8000):
#     k, j, i = np.random.randint(dn.shape[0]), np.random.randint(dn.shape[1]), np.random.randint(dn.shape[2])
#     signal[k, j, i] = 1.33
#     dn[k, j, i] = 1.59

# st()

ellipsoid = Ellipsoid(num_spheres=500, 
                      elli_axis=(105, 200, 105), 
                      spheres_radius=5, 
                      grid_size=512, 
                      sample_reIndex=1.5, 
                      medium_reIndex=1.33,
                      seed=42)
dn, signal = ellipsoid.get_sample()
# signal = np.ones_like(dn) * 1.33


# st()
# tf.imshow(np.asanyarray(dn))
# plt.show()

if not "m" in locals():
    pass
    m = SimLSM_Cylindrical(dn=dn,
                            signal=signal,
                            NA_illum=.4,
                            NA_detect=.8,
                            units=(.1,)*3,
                            n0=1.33,
                            # simul_xy_detect=(512,512),
                            # simul_xy_illum=(512,512),
                            )
 

image = m.simulate_image_z(cz=5, zslice = 100)

# tf.imshow(np.asanyarray(image))
# plt.show()
# st()
tf.imwrite('./lightsheet_test.tiff',np.asanyarray(image))
 
# #simulate the image at relative  axial position 20um
# img_stack = []
# for i in tqdm(np.arange(0,5.6,0.1)):
#     image = m.simulate_image_z(cz=i, zslice = 1)
#     img_stack.append(image[0])
    
# st()
# tf.imshow(np.asanyarray(img_stack))
# plt.show()

# tf.imwrite('./lightsheet_test.tiff',np.asanyarray(img_stack))
# st()