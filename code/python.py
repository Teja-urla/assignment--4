import numpy as np
from numpy import random as RN

#Total number of outcomes(HH,HT,TH,TT)
N = 4
#Number of outcomes in which we get atleast one head(HH,HT,TH)
n_0 = 3
#Number of outcomes in which we get no heads (TT)
n_1 = 1

# So Theoretical probabilities
pr_0 = (n_0)/N
pr_1 = (n_1)/N


x = RN.randint(0, 4, size=N)

#Finding the number of numbers which are greater than or equal to 3.
x_0 = np.count_nonzero(x>=1)

#So ,number of numbers such that x=0 is
x_1 = N - x_0


print("Theoretical Probabilities (i.e caculated):", pr_0, pr_1)
print("Practical Probabilities:", x_0/N, x_1/N)
