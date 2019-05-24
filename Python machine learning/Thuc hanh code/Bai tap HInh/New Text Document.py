import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as img
from numpy import random


img_dir = 'img.png'

image = img.imread(img_dir)

plt.subplot(231)
plt.imshow(image)
plt.axis('off')
plt.show()