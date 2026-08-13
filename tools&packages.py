

import os
current_dir = os.getcwd()
print(current_dir)

import math
result = math.sqrt(16)
print(result)

from math import sqrt, pi
result = sqrt(25)
radius = 5
circle_area = pi * radius ** 2
print(result)
print(circle_area)

# can also import everything from a module using *
from math import *

# can import using an alias
import math as m
import numpy as np
import pandas as pd



