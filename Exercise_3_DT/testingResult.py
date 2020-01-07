# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 11:43:23 2019

@author: Orin
"""

import math

entropy = - ((2/3) * math.log2(2/3)) - ((1/3) * math.log2(1/3));
print(entropy);

information_gain = 1 - ((3/4) * entropy);
print(information_gain);