#Exercise 0

def github() -> str:
    """
    This function returns the link to my solution.
    """

    return "https://github.com/tsato081/supreme-couscous/blob/main/Problem_Set_4.py"

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LogisticRegression

#Exercise 1
def load_data() -> pd.DataFrame:
    """
    It accesses the file on Tesla stock price history on the course website.
    """
    url = "https://lukashager.netlify.app/econ-481/data/TSLA.csv"
    df = pd.read_csv(url, parse_dates=['Date'])

    return df

#Exercise 2
def plot_close(df: pd.DataFrame, start: str = '2010-06-29', end: str = '2024-04-15') -> None:
    """
    takes the output of load_data() and optional start and end date 'YYYY-MM-DD' str format.
    plots the closing price of the stock between those dates as a line graph.
    """
    
    range = (df['Date'] >= start) & (df['Date'] <= end)
    new_df = df.loc[range]
    plt.figure(figsize=(10,5))
    plt.plot(new_df['Date'], new_df['Close'])
    plt.xlabel('Date')
    plt.ylabel('Closing Price($)')
    plt.show()
    return None

#Exercise 3
def autoregress(df: pd.DataFrame) -> float:
    """
    takes the output of Exercise 1 and returns the t-statistic on the autoregression
    """
    df['Delta'] = df['Close'].diff()
    df['Delta2'] = df['Delta'].shift(1)
    df.dropna(inplace=True)
    X = df['Delta2']
    Y = df['Delta']
    auto_fit = sm.OLS(Y, X).fit(cov_type='HC1', use_t = True)
    t_stat = auto_fit.tvalues['Delta2']

    return t_stat

#Exercise 4
def autoregress_logit(df: pd.DataFrame) -> float:
    """
    takes single argument df and returns the t statistic on coefficient.
    """
    df['Delta'] = df['Close'].diff()
    df['Direction'] = (df['Delta'] > 0).astype(int)
    df['Delta2'] = df['Delta'].shift(1)
    df = df.dropna()
    X = df['Delta2']
    y = df['Direction']
    log_fit = sm.Logit(y, X).fit()
    t_stat2 = log_fit.tvalues['Delta2']

    return t_stat2

#Exercise 5
def plot_delta(df: pd.DataFrame) -> None:
    """
    Takes the output of Exercise 1 as an argument, returns a graph for deltaX_t
    """
    df['Delta'] = df['Close'].diff()
    df = df.dropna()
    plt.figure()
    plt.plot(df.index, df['Delta'], label='ΔClose')
    plt.xlabel('Date')
    plt.ylabel('Change in Close Price')
    plt.show()
    return None
