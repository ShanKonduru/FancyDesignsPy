import numpy as np
import matplotlib.pyplot as plt

class LogisticMapPlotter:
    def __init__(self, Many=50000):
        self.Many = Many
        self.x = np.random.rand(self.Many)
        self.r = np.linspace(0, 4.0, num=self.Many)

    def plot(self, iterations=100):
        for i in range(1, iterations + 1):
            output_filename = "./output/" +  str(i) + "_Logistic_Map.png"
            x_a = 1 - self.x
            Data = np.multiply(self.x, self.r)
            Data = np.multiply(Data, x_a)
            self.x = Data

            plt.title(r'Logistic map: $x_{n+1} = r x_{n} (1-x_{n}).$  n = ' + str(i))
            plt.ylabel('x-Random number')
            plt.xlabel('r-Rate')

            plt.scatter(self.r, Data, s=0.1, c='k')
            plt.savefig(output_filename, dpi=300)
            plt.clf()

# Example usage:
if __name__ == "__main__":
    plotter = LogisticMapPlotter()
    plotter.plot()
