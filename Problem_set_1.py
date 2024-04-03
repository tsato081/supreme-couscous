def github() -> str:
    """
    Returns a link to the solution on GitHub
    """
    return "https://github.com/tsato081/supreme-couscous/blob/main/Problem_set_1.py"

#Question 1
def evens_and_odds (n: int) -> dict:
    """_summary_
    
    Args:
        n (int): natural numbers

    Returns:
        dict: returns a dictionary consisting of evens, which is a sum of all even numbers less than n and odds, which is a sum of all odd numbers less than n
        
    """
    evens = 0
    for i in range(n):
        if i %2 == 0:
            evens += i
    odds = 0
    for j in range(n):
        if j % 2 == 1:
            odds += j
    return {'evens': evens, 'odds': odds}


#Question3
from typing import Union
from datetime import datetime

def time_diff(date_1: str, date_2: str, out: str) -> Union[str,float]:
    """

    Args:
        date_1 (str): YYYY-MM-DD
        date_2 (str): YYYY-MM-DD
        out (str): string or float

    Returns:
        Union[str,float]: if out is float it returns difference in the number of days, and if out is str it returns "There are {diff} days between the two dates"
    """
    date1 = datetime.strptime(date_1, "%Y-%M-%D")
    date2 = datetime.strptime(date_2, "%Y-%M-%D")
    
    diff = abs((date1 - date2).days)
    
    if out == 'string':
        return f"There are {diff} days between the two dates"
    else:
        return diff

#Exercise 4
def reverse(in_list: list) -> list:
    """
    Some docstrings.
    """
    reversed_list = []
    for i in range(len(in_list)-1, -1, -1):
        reversed_list.append(in_list[i])
    return reversed_list

#Exercise 5
def prob_k_heads(n: int, k: int) -> float:
    """
    Some docstrings.
    """
    if n < k:
        return f"Error: n has to be larger than k"
    else:
        binom_coef = 1
        for i in range(n, n-k, -1):
            binom_coef *= i
        for j in range(1, k+1):
            binom_coef /= j
        
        probability = binom_coef / 2 ** n

    return probability

