import numpy as np;
import random;
import matplotlib
import pylab


def getData(n, p):

    n = 1000; # number of observations
    p = 2; # number of explanatory variables

    velocityMeans = np.array([70, 1000])
    accelerationMeans = np.array([70, 1000])

    data = np.empty([n, p + 1])

    for x in range(0, n):
        Type =  np.random.binomial(1,0.5)
        velocity = random.gauss(velocityMeans[Type], 10)
        acceleration = random.gauss(accelerationMeans[Type], 10)
        data[x, :] = [Type, velocity, acceleration] 
    return data;
  
def leastSquaresSoln(X, p):
    y = X[:, 0]
    x = X[:, 1:p + 1]
    pinv = np.linalg.pinv(x)
    return np.dot(pinv, y)

def fishersLinearDiscriminant(data):
    



if __name__ == "__main__":

    n = 1000; # number of observations
    p = 2; # number of explanatory variables
    data = getData(n, p)
    
    betaLS = leastSquaresSoln(data, p)
    
    x = np.sort(data[:,1])
    y = (0.5 - x*betaLS[1])/betaLS[0]

    matplotlib.pyplot.scatter(data[:, 1], data[:, 2], c = data[:, 0])
    matplotlib.pyplot.plot(x, y)
    matplotlib.pyplot.show()

