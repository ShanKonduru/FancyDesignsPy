import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class ComplexLogisticMap3DPlotter:
    def __init__(self, Many=500, iterations=100):
        self.Many = Many
        self.iterations = iterations
        self.r = np.linspace(-2, 2, self.Many)
        self.c = np.linspace(-2, 2, self.Many)
        self.R, self.C = np.meshgrid(self.r, self.c)

    def logistic_map(self, z, r):
        return r * z * (1 - z)

    def plot(self):
        Z = np.zeros_like(self.R, dtype=complex)
        for i in range(self.iterations):
            Z = self.logistic_map(Z, self.R + 1j * self.C)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(self.R, self.C, np.real(Z), cmap='viridis')
        ax.set_xlabel('r')
        ax.set_ylabel('Imaginary part')
        ax.set_zlabel('Real part')
        ax.set_title('3D Bifurcation Map with Complex Numbers')
        plt.show()

# Example usage:
if __name__ == "__main__":
    plotter = ComplexLogisticMap3DPlotter()
    plotter.plot()
