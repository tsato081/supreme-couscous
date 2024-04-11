import numpy as np
import scipy as sp

#Exercise 0
def github() -> str:
    """This function takes no arguments.

    Returns:
        str: Returns a link to my answer to my solution on GitHub.
    """
    return "https://github.com/tsato081/supreme-couscous/blob/main/Problem_Set_2.py"

#Exercise 2
def estimate_mle (y: np.array, X: np.array) -> np.array:
    """Estimates MLE parameters for a linear regression model using numerical optimization.
    
    Args:
        y (np.array): Dependent variable
        X (np.array): Independent Variables

    Returns:
        np.array: MLE estimates for the coefficients(beta_0 to beta_3)
    """
    X_intercept = np.hstack((np.ones((X.shape[0], 1)), X))
    def neg_ll(beta) -> float:
        
        residuals = y - X_intercept @ beta
        return 0.5 * np.sum(residuals ** 2)

    Initial_beta = np.zeros(4)
    
    result = sp.optimize.minimize(fun = neg_ll, x0= Initial_beta, method="Nelder-Mead")

    return result.x  


#Exercise 3

def estimate_ols(y: np.array, X: np.array) -> np.array:
    """Estimates the OLS coefficients for the simulated data

    Args:
        y (np.array): Dependent variable
        X (np.array): Independent Variables

    Returns:
        np.array: OLS estimates for the coefficients
    """
    X_with_intercept = np.hstack((np.ones((X.shape[0], 1)), X))
    def objective_function(beta):
        residuals = y - X_with_intercept @ beta
        return np.sum(residuals ** 2)
    
    Initial_beta2 = np.zeros(4)
    
    result = sp.optimize.minimize(fun=objective_function, x0 = Initial_beta2, method="Nelder-Mead")
    return result.x

