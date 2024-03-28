import numpy as np
import matplotlib.pyplot as plt

Many =50000

x = np.random.rand(Many)
r = np.linspace(0,4.0, num= Many)

for i in range(1, 54):
    x_a = 1-x
    Data= np.multiply(x,r)
    Data= np.multiply(Data, x_a)
    x = Data

    plt.title(r'Logistic map: $x_{n+1} = r x_{n} (1-x_{n}).$  n = '+ str(i) )
    plt.ylabel('x-Random number')
    plt.xlabel('r-Rate')
    
    plt.scatter(r, Data, s=0.1, c='k')
    plt.show()
    plt.savefig(str(i) + " Logistic Map.png", dpi = 300)
    plt.clf()
    