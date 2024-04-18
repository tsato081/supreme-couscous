#Exercise 0

def github() -> str:
    """The link to my solution.

    Returns:
        str: link for github.
    """
    return "https://github.com/tsato081/supreme-couscous/blob/main/Problem_Set_3.py"



#Exercise 1
import pandas as pd

def import_yearly_data(years: list) -> pd.DataFrame:
    """
     takes as its argument a list of years,
     returns a concatenated DataFrame of the Direct Emitters tab of each of those years EPA excel sheet.
    """
    
    data = []
    
    for year in years:
        url = f"https://lukashager.netlify.app/econ-481/data/ghgp_data_{year}.xlsx"
        df = pd.read_excel(url, sheet_name= "Direct Emitters", header=3)
        df['year'] = year
        data.append(df)
        
    concat_df = pd.concat(data, ignore_index = True)
    
    return concat_df



#Exercise 2
def import_parent_companies(years: list) -> pd.DataFrame:
    """
    takes a list of years as an argument.
    returns concatenated DataFrame of the corresponding tabs in the parents' companies excel sheet
    """
    data2 = []
    url2 = "https://lukashager.netlify.app/econ-481/data/ghgp_data_parent_company_09_2023.xlsb"
    for year in years:
        df2 = pd.read_excel(url2, sheet_name = f"{year}", engine='pyxlsb')
        df2 = df2.dropna(how='all')
        df2['year'] = year
        data2.append(df2)
    concat_df2 = pd.concat(data2, ignore_index = True)
    
    return concat_df2



#Exercise 3
def n_null(df: pd.DataFrame, col: str) -> int:
    """
    takes as its argument a DataFrame and a column name.
    returns an integer corresponding to the number of null values in that column.
    """
    null_amount = df[col].isna().sum()

    return null_amount



#Exercise 4
def clean_data(emissions_data: pd.DataFrame, parent_data: pd.DataFrame) -> pd.DataFrame:
    """
    takes as its arguments 2 outputs from exercise 1 and 2.
    outputs a dataframe.
    """
    parent_data = parent_data.rename(columns={'GHGRP FACILITY ID': 'Facility Id'}) 
    merged_df = pd.merge(emissions_data, parent_data, left_on=['year', 'Facility Id'], right_on = ['year', 'Facility Id'], how='left')
    column_sub = ['Facility Id', 
        'year', 
        'State', 
        'Industry Type (sectors)', 
        'Total reported direct emissions', 
        'PARENT CO. STATE', 
        'PARENT CO. PERCENT OWNERSHIP'
    ]
    subset_df = merged_df[column_sub]
    merged_df.columns = merged_df.columns.str.lower()

    return merged_df


#Exercise 5
def aggregate_emissions(df: pd.DataFrame, group_vars: list) -> pd.DataFrame:
    """
    that takes as input a DataFrame with the schema of the output of Exercise 4 and a list of variables and produces the minimum, median, mean, and maximum values
    return the the data sorted by highest to lowest mean total reported direct emissions.
    """
    
    aggregate_vars = {'total reported direct emissions':['min', 'median', 'mean', 'max'],
                      'parent co. percent ownership':['min', 'median', 'mean', 'max']}
    aggregated_df = df.groupby(group_vars, as_index=True).agg(aggregate_vars)
    aggregated_df.columns = ['_'.join(col).strip() for col in aggregated_df.columns.values]
    aggregated_df = aggregated_df.sort_values('total reported direct emissions_mean', ascending=False)
    

    return aggregated_df
