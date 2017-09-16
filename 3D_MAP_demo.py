from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def a_posteriori_probability(X, Y, W, sigma_2):
	N = X.shape[0]
	norm_error = np.linalg.norm(W)**2 / sigma_2
	pred_Y = X.dot(W)
	return - np.linalg.norm(pred_Y - Y)**2 + N * norm_error

for N in [5, 25, 125]:
	for SIGMA_2 in [1000, 100, 10, 1, 0.1]:
		W = np.array([5, 5])
		X_rows = []
		for i in range(N):
			X_row = [np.random.randint(-20, 20), np.random.randint(-20, 20)]
			X_rows.append(X_row)
		X = np.vstack(X_rows)
		Y = X.dot(W) + np.random.normal()

		x1_range = np.linspace(0, 10)
		x2_range = np.linspace(0, 10)

		x = []
		y = []
		z = []

		for x1 in x1_range:
			for x2 in x2_range:
				W = np.array([x1, x2])
				x.append(x1)
				y.append(x2)
				z.append(a_posteriori_probability(X, Y, W, SIGMA_2))

		fig = plt.figure()
		ax = fig.gca(projection='3d')

		plt.xlabel('W_1')
		plt.ylabel('W_2')
		plt.title('a-posteriori probability for N = {} with sigma = {}'.format(N, SIGMA_2))
		ax.plot_trisurf(x, y, z, linewidth=0.5, antialiased=True)
		plt.grid(True)
		plt.savefig('plot_{}_{}.png'.format(N, SIGMA_2))
