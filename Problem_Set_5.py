#Exercise 0
def github() -> str:
    """
    takes no arguments and returns the link to the assignment.
    """

    return "https://github.com/tsato081/supreme-couscous/blob/main/Problem_Set_5.py"

import requests
from bs4 import BeautifulSoup
import re

#Exercise1
def scrape_code(url: str) -> str:
    """
    takes a URL to a lecture page and scrapes all the Python code snippets,
    cleaning them for direct use in a Python interpreter.

    Args:
    url (str): The URL of the lecture page.

    Returns:
    str: A string containing all Python code snippets from the lecture, cleaned and concatenated.
    """
    
    req_obj = requests.get(url)
    soup = BeautifulSoup(req_obj.text)
    code_block = soup.find_all('code')
    
    code_snippets = []
    for code in code_block:
        raw_code = code.get_text()
        cleaned_code = re.sub(r"=\s*'.*?'", "", raw_code) 
        code_snippets.append(cleaned_code)  
    extracted_code = [item for item in code_snippets if "'" in item ]
    cleaned_code2 = []
    for i in extracted_code:
        cleaned_entry = i.strip('"')
        cleaned_code2.append(cleaned_entry)
    for line in cleaned_code2:
        print(line)
    return None