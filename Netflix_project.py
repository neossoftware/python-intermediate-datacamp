# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!

netflix_df = pd.read_csv('netflix_data.csv')
tv_shows = netflix_df['type'] == 'Movie'
netflix_subset = netflix_df[tv_shows]
print(netflix_subset.head())
