import matplotlib.pyplot as plt
import numpy as np

def predict_y(x, w):
    """ 
    Find predicted y vector given x and w vectors for a polynomial evaluation
    """
    r = []
    n = len(w)
    for i in range(len(x)):
        temp = 0
        for j in range(n):
            temp = temp+w[n-j-1]*(x[i]**j)
        r = r+[temp]
    return r

def get_feature_matrix(N, Xtrain, D):
    """
    Construct X according to degree of polynomial
    """
    for i in range(D+1):
        if i == 0:
            X = [1] * N
        else:
            X = np.vstack([np.power(Xtrain, i), X])
    X = X.transpose()
    return X

def regression(x_train, y_train, D):
    """
    Fits polynomial regression to dataset
    Args:
        x_train: np array of shape (n,) containing x_i values for training
        y_train: np array of shape (n,) containing y_i values for training
        D: degree of polynomial
    Returns:
        Dictionary with weights and error information
    """
    Ntrain = len(x_train)
    Xtrain = np.asmatrix(x_train)
    Ytrain = np.asmatrix(y_train).transpose()
    
    X = get_feature_matrix(Ntrain, Xtrain, D)

    w = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, Ytrain))
    
    predicted_Y = X.dot(w)
    average_training_error = np.linalg.norm(predicted_Y - Ytrain)**2 / Ntrain
    
    return w, average_training_error

# Training error as a function of D
PLOT = False
N = 50
MAX_D = 25
degs = [d for d in range(1, MAX_D)]
x_train = []
y_train = []
true_y =  []

for i in range(N):
    x = np.random.uniform(-1, 1)
    W_i = np.random.normal()
    y = x + 1 + W_i
    x_train.append(x)
    y_train.append(y)
    true_y.append(y - W_i)

errors = []
for D in degs:
    w, average_training_error = regression(x_train, y_train, D)
    errors.append(average_training_error)

    if PLOT:
        print("Average training error for degree {}: {}"
            .format(D, average_training_error))

        w = w.reshape((w.shape[0],)).tolist()[0]
        x = np.linspace(-5, 5, 1000)
        y = predict_y(x, w)
        plt.scatter(x_train, y_train)
        plt.plot(x, y, color='red')
        plt.plot(x_train, true_y, color='orange')
        plt.title('Training samples and regression')
        plt.grid(True)

        x1,x2,y1,y2 = plt.axis()
        plt.axis((-1.5,1.5,-3,4))    
        plt.show()

plt.plot(degs, errors)
plt.title('Average error as a function of D for fixed n = {}'.format(N))
plt.xlabel('Degree of polynomial')
plt.ylabel('Average squared training error')
plt.grid(True)
plt.savefig('test1.png')
plt.show()


# Training error as a function of n
MAX_N = 200
D = 10
Ns = [n for n in range(D+1, MAX_N)]
errors  = []
for N in Ns:
    x_train = []
    y_train = []
    for i in range(N):
        x = np.random.uniform(-1, 1)
        W_i = np.random.normal()
        y = x + 1 + W_i
        x_train.append(x)
        y_train.append(y)
    w, average_training_error = regression(x_train, y_train, D)
    errors.append(average_training_error)

    if PLOT:
        print("Average training error for n {}: {}"
            .format(N, average_training_error))

        w = w.reshape((w.shape[0],)).tolist()[0]
        x = np.linspace(-5, 5, 1000)
        y = predict_y(x, w)
        plt.scatter(x_train, y_train)
        plt.plot(x, y, color='red')
        plt.title('Training samples and regression')
        plt.grid(True)

        x1,x2,y1,y2 = plt.axis()
        plt.axis((-1.5,1.5,-3,4)) 
        plt.show()    

plt.scatter(Ns, errors)
plt.title('Average error as a function of n for fixed D = {}'.format(D))
plt.xlabel('Number of samples')
plt.ylabel('Average squared training error')
plt.grid(True)
plt.savefig('test2.png')
plt.show()    

