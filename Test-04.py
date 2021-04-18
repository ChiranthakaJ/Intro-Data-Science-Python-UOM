import re
string = 'bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot'
result = re.findall('b[ao]t', string)
print(result)

import numpy as np

old = np.array([[1, 1, 1], [1, 1, 1]])
new = old
new[0, :2] = 0
print(old)