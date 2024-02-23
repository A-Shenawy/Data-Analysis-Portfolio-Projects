import pandas as pd
import json
import requests
import os
from PIL import Image
from IPython.display import IFrame
import openpyxl
from openpyxl import Workbook
from bs4 import BeautifulSoup

# Lab : Web Scraping
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"

data = requests.get(url).text

soup = BeautifulSoup(data, "html.parser")

# 1st Solution using pd.read_html(url)
read_html_pandas_data = pd.read_html(url)
first_table = read_html_pandas_data[0]
first_table.columns = first_table.iloc[0]
first_table = first_table.drop(first_table.index[0])
first_table = first_table.reset_index(drop=True)
print(first_table[['Language','Average Annual Salary']])

# 2nd Solution using the tags of table

for row in soup.find_all('tr'):
    cols = row.find_all('td')
    Language = cols[1].getText()
    annual_average_salary = cols[3].getText()
    print("{} -->{}".format(Language,annual_average_salary))


first_table.to_csv("popular-languages.csv")

# To get the max salary
sorted_df = first_table.sort_values(by= 'Average Annual Salary', axis=0, ascending=False)

print(sorted_df)