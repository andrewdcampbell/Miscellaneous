# This program generates a linear least-squares regression of the form y = ax + b 
# for data points (x, y). It then calculates epsilon values for how much to adjust
# the y-values for any two data points in order to achieve desired a,b values from 
# linear least-squares regression on the modifed data points.

import matplotlib.pyplot as plt
import numpy as np

# Must be an integer greater than 1
NUM_DATA_POINTS = 40
# The indices of the data points to adjust to obtain the desired regression line
ADJUSTED_POINT_1_INDEX, ADJUSTED_POINT_2_INDEX = 4, NUM_DATA_POINTS - 8
# The desired a value (the slope)
DESIRED_A = np.pi
# The desired b value (the y-intercept)
DESIRED_B = np.e

def generate_data_points(num_points):
    """ 
    Returns random (but roughly linear) data points in the form (x_list, y_list) 
    """
    midpoint = num_points // 2
    x_list = np.array(list(range(-midpoint, num_points - midpoint)))
    random_a = np.random.randn()
    random_b = np.random.randn()
    y_list = [random_a * x + random_b + np.random.randn() for x in x_list]
    return x_list, y_list

def least_squares_line(x_list, y_list):
    """ 
    Returns (a, b) for the least squares line of the form y = ax + b for
    the data points stored as x_list, y_list
    """ 
    A = np.matrix([[x, 1] for x in x_list])
    b = np.array([y_list]).T
    x = np.linalg.solve(np.dot(A.T, A), np.dot(A.T, b))
    least_squares_a = x[0, 0]
    least_squares_b = x[1, 0]
    return least_squares_a, least_squares_b

def get_epsilon(desired_a, desired_b, x_list, y_list, index_1, index_2):
    """ 
    Returns the epsilon values (e1, e2) needed to adjust y_list[index_1] 
    and ylist[index_2], respectively, to obtain the desired_a and desired_b 
    values from linear regression on the data points stored as x_list, y_list 
    """
    desired_x = np.matrix([[desired_a], [desired_b]])
    A = np.matrix([[x, 1] for x in x_list])
    y = np.array([y_list]).T
    A_T_A = np.dot(A.T, A)
    A_T_y = np.dot(A.T, y)

    b = np.dot(A_T_A, desired_x) - A_T_y
    A = np.matrix([[x_list[index_1], x_list[index_2]], [1, 1]])
    epsilon = np.linalg.solve(A, b)
    return epsilon[0, 0], epsilon[1, 0]

x_list, y_list = generate_data_points(NUM_DATA_POINTS)
least_squares_a, least_squares_b = least_squares_line(x_list, y_list)
print("Old A value:", least_squares_a)
print("Old B value:", least_squares_b)

# Plot the data and regression line y = ax + b
fig, ax = plt.subplots()
ax.plot(x_list, least_squares_a * x_list + least_squares_b, color='red')
ax.grid(True, which='both')
ax.scatter(x_list, y_list)

# Adjust data to achieve the desired a, b values for y = ax + b
e1, e2 = get_epsilon(DESIRED_A, DESIRED_B, x_list, y_list, 
    ADJUSTED_POINT_1_INDEX, ADJUSTED_POINT_2_INDEX)
print("Adjusting data point {} from {} to {}".format(ADJUSTED_POINT_1_INDEX, 
    y_list[ADJUSTED_POINT_1_INDEX], e1))
print("Adjusting data point {} from {} to {}".format(ADJUSTED_POINT_2_INDEX, 
    y_list[ADJUSTED_POINT_2_INDEX], e2))
y_list[ADJUSTED_POINT_1_INDEX] += e1
y_list[ADJUSTED_POINT_2_INDEX] += e2

least_squares_a, least_squares_b = least_squares_line(x_list, y_list)
print("New A value:", least_squares_a)
print("New B value:", least_squares_b)
ax.plot(x_list, least_squares_a * x_list + least_squares_b, color='orange')

plt.show()