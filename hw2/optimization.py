import numpy as np
from scipy import optimize

def rosenbrock_func(x):
    """
    calculate value of rosenbrock function with n=3
    :param x: a list of independent variables
    :return: the value of the rosenbrock function at point x
    """
    return 100 * (x[1] - x[0] **2) **2 + (1 - x[0]) ** 2 + 100 * (x[2] - x[1] ** 2) ** 2 + (1 - x[1]) ** 2

def rosenbrock_grad(x):
    """
    calculate value of the gradient of rosenbrock function with n=3
    :param x: a list of independent variables
    :return: the value of the gradient of rosenbrock function at point x
    """
    return np.array([-400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0]), 
                     200*(x[1]-x[0]**2) - 400*x[1]*(x[2]-x[1]**2) - 2*(1-x[1]), 
                     200*(x[2]-x[1]**2)])

if __name__ == "__main__":
    x1 = [1, 3, 5]
    x2 = [-4, 5, 99]
    x3 = [66, 91, 20000]
    x4 = [34, 1, -5]
    x5 = [-7, 20, -82]
    x = [x1, x2, x3, x4, x5]
    res = []
    for x0 in x:
        res.append(optimize.minimize(rosenbrock_func, x0, method='BFGS', jac=rosenbrock_grad).fun)
    print(min(res))