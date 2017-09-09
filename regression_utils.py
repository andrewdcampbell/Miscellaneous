import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
import itertools

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

def regression(x_train, y_train, x_test=[], y_test=[], D=2, plot=False):
    """
    Fits polynomial regression or ridge regression to dataset, plot the results, 
    and calculates training errors.
    Args:
        x_train: np array of shape (n,) containing x_i values for training
        y_train: np array of shape (n,) containing y_i values for training
        x_train: np array of shape (k,) containing x_i values for testing
        y_train: np array of shape (k,) containing y_i values for testing   
        D: degree of polynomial
        plot: if true, plot the data and best fit polynomial
    Returns:
        Dictionary with weights and error information
    """
    Ntrain = len(x_train)
    Ntest  = len(x_test)
    Xtrain = np.asmatrix(x_train)
    Ytrain = np.asmatrix(y_train).transpose()
    Xtest = np.asmatrix(x_test)
    Ytest = np.asmatrix(y_test).transpose()    
    
    X = get_feature_matrix(Ntrain, Xtrain, D)
    X_test = get_feature_matrix(Ntest, Xtest, D)

    w = np.linalg.solve(np.dot(X.T, X), np.dot(X.T, Ytrain))
    w = w.reshape((w.shape[0],)).tolist()[0]
    
    predicted_Y = X.dot(w).T
    Rtrain = np.linalg.norm(predicted_Y - Ytrain) #training error

    predicted_Y_test = X_test.dot(w).T
    Rtest = np.linalg.norm(predicted_Y_test - Ytest) #test error    

    average_training_error = (Rtrain**2) / Ntrain
    average_test_error = (Rtest**2) / Ntest

    if plot:
        # plots
        x = np.linspace(-5, 5, 1000)
        y = predict_y(x, w)
        plt.subplot(211)
        plt.scatter(x_train, y_train)
        plt.plot(x, y)
        plt.title('Training samples and regression')
        plt.grid(True)

        x = np.linspace(-5, 5, 1000)
        y = predict_y(x, w)
        plt.subplot(212)
        plt.scatter(x_test, y_test)
        plt.plot(x,y)
        plt.title('Test samples and regression')
        plt.grid(True)   

        plt.show()
    
    return {'weights': w, 
            'average_training_error': average_training_error,
            'average_test_error': average_test_error,
           }


def get_polynomial(vars, degree):
    vars.append("c") # add dummy variable
    terms = []
    for x in itertools.combinations_with_replacement(vars, degree):
        terms.append(x)
    
    # get rid of "c" terms
    terms = list(map(list, terms))
    for i in range(len(terms)):
        while "c" in terms[i]:
            terms[i].remove("c")

    return terms


def get_multivariate_matrix(x_data, D):
    """
    Construct multivariate feature matrix for polynomial of degree D
    """
    rows = []
    terms = get_polynomial(['x1', 'x2', 'x3', 'x4', 'x5'], D)
    for row in range(len(x_data)):
        row_data = {}
        row_data['x1'] = x_data[row, 0]
        row_data['x2'] = x_data[row, 1]
        row_data['x3'] = x_data[row, 2]
        row_data['x4'] = x_data[row, 3]
        row_data['x5'] = x_data[row, 4]
        
        row_entry = []
        for t in terms:
            prod = 1
            for var in t:
                prod *= row_data[var]
            row_entry.append(prod)
            
        row_entry = np.array(row_entry)    
        rows.append(row_entry)
    return np.vstack(rows)  
