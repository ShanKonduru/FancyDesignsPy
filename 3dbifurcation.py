import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class LogisticMap3DPlotter:
    def __init__(self, Many=50000, iterations=100):
        self.Many = Many
        self.iterations = iterations
        self.r = np.linspace(0, 4.0, self.Many)
        self.x = np.linspace(0, 1.0, self.Many)
        self.R, self.X = np.meshgrid(self.r, self.x)

    def logistic_map(self, x, r):
        return r * x * (1 - x)

    def plot(self):
        output_filename = "./output/3d_Logistic_Map.png"
        Z = np.zeros_like(self.R)
        for i in range(self.iterations):
            self.x = self.logistic_map(self.x, self.r)
            Z += self.x

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.R, self.X, Z, cmap='viridis')
        ax.set_xlabel('r')
        ax.set_ylabel('x')
        ax.set_zlabel('Value')
        ax.set_title('3D Bifurcation Map')
        plt.show()
        plt.savefig(output_filename, dpi=300)

# Example usage:
if __name__ == "__main__":
    plotter = LogisticMap3DPlotter()
    plotter.plot()
