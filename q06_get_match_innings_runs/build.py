# %load q06_get_match_innings_runs/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df
import numpy as np
import pandas as pd
# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

def get_match_innings_runs():
    final_answer = ipl_df[['match_code','runs','inning']]
    return final_answer.groupby(['match_code','inning']).runs.sum()

