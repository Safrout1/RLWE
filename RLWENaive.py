import sys
import random
q = 12289
M = 512
Pmat = [[0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,1,1,1,1,1,0,1,1,1,1,0,0,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,0,1,0,1,1,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,1,1], [0,0,1,0,1,0,0,1,0,0,1,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,1,1,0,0,0,1,0,1,1,1,1,1,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,1,0,0,1,1,0,0,0,1,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1], [0,0,1,0,0,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,1,1,1,1,1,0,1,1,1,1,0,1,0,1,1,0,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,0,1,1,0,0,0,1,0,0,0,1,1,0,1,1,1,1,1,1,1,1,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1], [0,0,1,0,0,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,1,1,0,1,1,1,0,1,1,1,0,0,1,0,0,1,1,0,1,0,1,1,1,0,1,1,0,1,0,1,0,0,0,1,0,1,1,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1], [0,0,0,1,1,1,0,1,1,1,1,1,0,1,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,1,0,1,1,0,1,0,0,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,0,0,0,1,1,0,0,1,1,0,1,1,0,1,0,0,0,0,0,1,1,1,0,1,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,1,1,0,1,0,0,1,0,0,1], [0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,1,1,1,0,1,0,1,1,0,0,1,1,1,1,0,1,0,1,0,1,1,0,1,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,1,1,1,1,1,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1,1,0,0,1,1,1,0,1,1,1,1,1,1,0], [0,0,0,1,0,0,1,1,1,0,0,1,1,1,0,0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,1,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,1,0,1,1,0,0,1,0,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,0,1,0,1,1,0,1,1,1,1,0,1,1,1], [0,0,0,0,1,1,1,0,1,1,1,0,0,1,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,1,0,0,0,1,0,0,1,0,0,1,0,1,1,1,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,0,0,0,1,1,0,0,0,0,1,1,1,0,0,1,0,1,0,1,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,0], [0,0,0,0,1,0,1,0,1,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,0,1,1,0,1,1,0,0,0,0,1,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,1,0,0,0,0,0,0,1,0,1,1,1,0,1,0,0,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0], [0,0,0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,1,0,1,0,0,0,0,1,1,1,1,1,0,1,0,0,0,1,0,1,0,1,1,0,1,1,1,0,0,0,0,1,1,0,0,0,1,0,1,0,0,1,0,1,0,1,1,0,0,1,0,1,1,0,1,0,0,1,1,1,1,1,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1,1,0], [0,0,0,0,0,1,0,1,0,0,0,0,1,1,1,0,1,0,1,1,1,0,0,0,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,1,1,0,1,1,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0,1,1,0,0,1,0,1,0,0,1,1,1,1,0], [0,0,0,0,0,0,1,1,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,0,0,1,0,1,0,1,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,0,0,1,1,0,0,1,0,1,0,0,1,1,0,0,0,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,0,1,1,1,1,1,0,0,0,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,1,1,0,1], [0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,1,1,1,1,0,0,0,1,0,1,1,0,0,1,0,0,1,1,1,0,0,1,0,1,0,1,1,0,1,1,0,0,0,0,1,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,1,0], [0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,1,1,0,0,1,0,1,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,1,1,1,1,1,0,0,1,1,0,1,0,1,0,1,1,1,1,0,1,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1], [0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,1,0,0,0,1,0,1,0,1,1,0,1,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,0,0,1,0,0,1,0,0,1,1,0,0,0,1,1,0,1,0,1,0,1,0,0,1,0,0,0,0,1,1,1,0,1,0,1,1,0,1,0,0,0,1,1,1,0,1,0,0,0,0,0,1,0,1,1,1,1,1,0,1,0,1,0], [0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0,0,0,0,1,0,0,0,0,0,1,0,1,1,1,1,1,0,0,0,1,0,0,1,1,1,0,0,0], [0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,0,0,1,0,1,0,1,1,0,1,0,0,1,1,1,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,0,0,1,1,0,1,0,1,1,1,1,0,0,1,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,1,1,0,1,1,1,1,1], [0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,1,1,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,1,0,0,1,1,0,0,0,0,0,1,1,0,1,0,0,0,0,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,1,1,0,0,0,1,0,0,1,1,1,1,1,0,1,0,1,1,0,1,0,0,1,1,0,1,1,0,1,1,1,0,0,1,0,1,0,0,0,0,0,1,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,1,0,1,1,0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,1,1,0,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,1,0,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,0,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,0,0,0,1,0,1,1,1,0,0,0,0,1,1,1,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,1,1,1,1,0,0,0,0,1,0,1,1,1,0,1,1,0,1,0,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,0,1,0,1,1,1,1,0,0,0,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1,1,1,0,1,0,1,0,0,1,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0,1,0,0,0,0,1,1,0,1,0,1,0,0,1,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,0,0,1,0,1,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,1,1,1,0,0,0,0,1,1,1,1,0,0,1,0,0,1,1,1,1,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,1,1,1,0,1,0,1,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,1,1,1,0,0,1,0,0,0,1,0,1,1,1,0,0,1,1,1,0,1,1,1,0,1,0,0,0,1,0,1,0,1,1,0,0,1,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,1,0,1,0,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,1,1,1,0,0,0,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,1,1,0,0,1,0,0,0,1,0,0,1,0,1,1,1,1,1,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,1,1,0,0,1,1,0,1,0,0,1,1,1,0,0,1,0,1,0,1,0,1,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,1,0,1,1,0,0,1,0,0,1,0,0,1,1,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,1,0,1,1,1,1,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,1,0,1,0,0,0,0,1,1,1,0,0,1,1,0,1,0,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,1,1,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,1,1,1,0,1,0,0,1,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,1,0,0,1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,1,1,0,0,1,0,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,1,0,0,0,0,1,0,1,1,1,1,0,0,1,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,0,0,1,1,1,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,1,1,1,0,0,0,1,1,0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,0,0,0,1,1,1,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,0,1,1,0,0,0,1,0,0,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,1,1,0,0,1,0,1,1,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,1,0,0,1,0,1,0,0,1,0,0,0,1,1,0,0,0,0,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,0,0,1,1,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,1,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,1,0,1,1,0,1,1,1,0,1,0,1,1,0,0,1,1,1,0,1,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1,0,0,1,1,0,0,0,1,1,1,1,0,1,1,0,0,0,0,1,0,0,0,1,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,1,1,1,0,0,1,1,0,0,1,1,1,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,0,1,0,0,0,1,0,1,1,1,1,0,1,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,1,1,1,0,0,1,0,0,1,0,0,1,1,0,0,1,0,1,1,0,1,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,0,1,1,1,1,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,1,0,1,0,1,0,1,1,0,0,0,1,0,0,1,0,0,1,1,0,0,1,0,0,0,0,1,1,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1,1,1,0,0,1,0,0,1,0,0,1,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,0,1,1,1,0,1,0,1,0,0,0,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,1,0,0,1,0,1,0,0,1,1,0,1,0,1,1,0,0,0,1,1,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,1,1,0,0,1,0,0,1,0,0,1,1,1,0,1,1,0,0,1,1,1,0,1,0,0,1,0,0,0,1,0,0,0,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,1,0,1,0,0,1,1,0,0,1,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,0,0,1,1,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,1,0,0,0,1,1,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,1,0,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,0,0,1,1,0,1,1,0,1,0,1,1,1,1,0,1,0,0,1,1,1,0,0,1,0,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,0,0,1,0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,1,1,1,1,0,1,1,1,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,0,0,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0,0,0,1,1,0,0,0,0,1,1,1,1,1,0,0,1,1,0,1,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,1,0,1,0,0,1,0,0,0,0,0,0,1,0,1,1,1,1,0,0,1,0,0,1,0,1,0,0,0,0,1,1,0,1,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1,1,1,0,1,1,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,0,1,1,0,1,0,0,0,1,1,1,1,1,1,0,1,1,0,0,0,0,0,1,0,1,1,0,0,0,0,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,1,0,1,1,0,0,0,1,0,0,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,1,1,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,1,1,1,1,1,0,0,0,1,0,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0,1,1,0,0,1,1,1,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1], [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]]
MaxCol = 106
MaxRow = 59
QBY2 = 6144
QBY4 = 3072
QBY4_TIMES3 = 9216
f = [0] * M
f[0] = 1
f[-1] = 1


def modulus(n, m):
	return ((n % m) + m) % m;

#print(mod(-1, 5))

def multiplyNaive(a, b, mod):
	m = len(a)
	n = len(b)
	prod = [0] * (m + n - 1)
	for i in range(0, m):
		for j in range(0, n):
			prod[i + j] += modulus(a[i] * b[j], mod)
			prod[i + j] = modulus(prod[i + j], mod)
	return prod

def PolyToString(a):
	n = len(a)
	s = ""
	for i in range(0, n):
		s += str(a[i])
		if (i != 0):
			s += 'X^' + str(i)
		if (i != n - 1):
			s += '+'
	return s

from itertools import izip
from math import fabs

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def degree(poly):
    while poly and poly[-1] == 0:
        poly.pop()   # normalize
    return len(poly)-1
 
def poly_div(N, D, mod):
    dD = degree(D)
    dN = degree(N)
    if dD < 0: raise ZeroDivisionError
    if dN >= dD:
        q = [0] * dN
        while dN >= dD:
            d = [0]*(dN - dD) + D
            mult = q[dN - dD] = N[-1] // d[-1]
            d = [coeff * mult for coeff in d]
            N = [ ( coeffN - coeffd ) for coeffN, coeffd in izip(N, d)]
            dN = degree(N)
        r = N
    else:
        q = [0]
        r = N
    for i in range(0, len(q)):
    	q[i] = modulus(int(q[i]), mod)
    for i in range(0, len(r)):
    	r[i] = modulus(int(r[i]), mod)
    return [q, r]

# print "POLYNOMIAL LONG DIVISION"
# N = [17, 13, 0, 6, 7, 12]
# D = [1, 1, 0, 0, 0, 6]
# x = poly_div(N, D, q)
# print(x)


# a = [5, 0, 10, 6]
# b = [1, 2, 4]
# print(PolyToString(a))
# print(PolyToString(b))
# c = multiplyNaive(a, b)
# print(PolyToString(c))

def coefficientAdd(b, c, mod): # a = b * c
	m = len(b)
	a = [0] * m
	for i in range (0, m):
		a[i] = modulus(b[i] + c[i], mod)
	return a

#print(coefficientAdd([2, 3, 5], [3, 2, 10], q))

def coefficientSub(b, c, mod): # a = b * c
	m = len(b)
	a = [0] * m
	for i in range (0, m):
		a[i] = modulus(b[i] - c[i], mod)
	return a

#print(coefficientSub([2, 3, 5], [3, 2, 10], q))

def knuthYaoSingleNumber(r, mod):
	d = 0
	col = 0
	while (col < MaxCol):
		d = 2 * d + (r & 1) # I don't know what the distance actually is
		r >>= 1
		row = MaxRow - 1
		while (row >= 0):
			d = d - Pmat[row][col]
			if (d == -1):
				if ((r & 1) == 1):
					return modulus(mod - row, mod)
				else:
					return modulus(row, mod)
			row -= 1
		col += 1
	return 0

def plot():
	a = [0] * (12289)
	for idx in range(1, (1 << 16) - 1):
		a[knuthYaoSingleNumber(idx, q)] += 1
	print(a)

# plot()

def knuthYao(a, mod):
	n = len(a)
	r = random.randint(0, 10000000000)
	i = 0
	while (i < n / 2):
		a[i << 1] = knuthYaoSingleNumber(r, mod)
		if ((i << 1) + 1 < n):
			a[(i << 1) + 1] = knuthYaoSingleNumber(r, mod)
		i+= 1
	return a

def aGen(a, mod):
	i = 0
	n = len(a)
	while (i < n / 2):
		r = random.randint(0, 1000000000000)
		a[i << 1] = modulus((r & 0xffff), mod)
		if ((i << 1) + 1 < n):
			a[(i << 1) + 1] = modulus(((r >> 16) & 0xffff) , mod)
		i += 1
	return a

def r1Gen(r1, mod):
	knuthYao(r1, mod)
	return r1

def r2Gen(r2, mod):
	n = len(r2)
	i = 0
	while (i < n):
		r = random.randint(0, 1000000000)
		j = 0
		while (j < 16):
			bit = r & 1
			sign = (r >> 1) & 1
			if (sign == 1 and bit == 1):
				bit = mod - 1
			if (i < n):
				r2[i] = bit
			i += 1
			r = r >> 2
			j += 1
	return r2

def keyGeneration():
	a = [0] * M
	r1 = [0] * M
	r2 = [0] * M
	aGen(a, q)
	r1Gen(r1, q)
	r2Gen(r2, q)
	tmp = poly_div(multiplyNaive(a, r2, q), f, q)[1] # tmp = a * r2
	tmp = tmp + ([0] * (M - len(tmp)))
	p = coefficientSub(r1, tmp, q) # p = r1 - tmp -> p = r1 - a * r2
	r2 = r2 + ([0] * (M - len(r2)))
	a = a + ([0] * (M - len(a)))
	p = p + ([0] * (M - len(p)))
	return [r2, a, p]

def encryption(a, p, m):
	e1 = [0] * M
	e2 = [0] * M
	e3 = [0] * M
	mEncoded = [0] * M
	for i in range(0, M): # m'
		mEncoded[i] = m[i] * QBY2
	knuthYao(e1, q)
	knuthYao(e2, q)
	knuthYao(e3, q)
	e3Plusm = coefficientAdd(e3, mEncoded, q) # e3 + m'
	c1 = poly_div(multiplyNaive(a, e1, q), f, q)[1]
	c1 = c1 + ([0] * (M - len(c1)))
	c1 = coefficientAdd(c1, e2, q)
	c2 = poly_div(multiplyNaive(p, e1, q), f, q)[1]
	c2 = c2 + ([0] * (M - len(c2)))
	c2 = coefficientAdd(c2, e3Plusm, q)
	c1 = c1 + ([0] * (M - len(c1)))
	c2 = c2 + ([0] * (M - len(c2)))
	return [c1, c2]

def decryption(c1, c2, r2):
	mEncoded = poly_div(multiplyNaive(c1, r2, q), f, q)[1]
	mEncoded = mEncoded + ([0] * (M - len(mEncoded)))
	mEncoded = coefficientAdd(mEncoded, c2, q)
	i = 0
	origM = [0] * len(mEncoded)
	while (i < len(origM)):
		if (mEncoded[i] > QBY4 and mEncoded[i] < QBY4_TIMES3):
			origM[i] = 1
		else:
			origM[i] = 0
		i += 1
	return origM

key = keyGeneration()
r2 = key[0]
a = key[1]
p = key[2]
m = [1, 0, 1, 0, 1] + ([0] * (M - 5))
print("Message:")
print(m)
c = encryption(a, p, m)
c1 = c[0]
c2 = c[1]
print("Cypher Text 1:")
print(c1)
print("Cypher Text 2:")
print(c2)
ans = decryption(c1, c2, r2)
print("Original Message Encoded: ")
print(ans)