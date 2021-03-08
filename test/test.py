import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd



def f(x):
    y = np.exp(-1 * (x ** 2) / 2) / (2 * math.pi) ** 0.5
    #y = np.exp(x)
    return y

x = np.arange(-2, 2, 0.01)
y = f(x)

plt.plot(x, y, ls="-")
plt.show()



list1 = ["abc", 'def', 'xyz']

df1 = pd.DataFrame(np.random.randn(3, 3), index=list1, columns=list('ABC'))
#print(df1)

print(3>2>2)



x1 = []
print(range(5) + 1)