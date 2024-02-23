import pandas as pd
import json
import requests
import os
from PIL import Image
from IPython.display import IFrame
import openpyxl
from openpyxl import Workbook

""" 1- HTTP and Requests """

# making response object
url='https://www.ibm.com/'
r = requests.get(url)
# checking the status code
status = r.status_code
if status.ok:
    print("Imported Successfully!")
else:
    print("There is definitely error.")
# view the request headers:
print("request headers:", r.headers)
# view the request body
print("request body:", r.request.body)  # You can view the request body, in the following line, as there is no body for a get request we get a None
# view the date the request was sent using the key Date
print(r.headers['date'])
# view Content-Type indicates the type of data
print(r.headers['Content-Type'])
# view the encoding
print(r.encoding)

url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
rec=requests.get(url)
print(rec.status_code)
print(rec.headers)
path=os.path.join(os.getcwd(),'D:/Other/1-IBM Data Analysis/(7) Data Analysis with Python/W1 - Importing Data sets/codes/Imported image.png')

""" 2- Collecting Job Data Using APIs """


api_url = "http://api.open-notify.org/astros.json" # this url gives use the astronaut data
response = requests.get(api_url) # Call the API using the get method and store the
                                # output of the API call in a variable called response.

if response.ok:             # if all is well() no errors, no network timeouts)
    data = response.json()  # store the result in json format in a variable called data
                            # the variable data is of type dictionary.
print(data)   # print the data just to check the output or for debugging
print(data.get('number'))

astronauts = data.get('people')
print("There are {} astronauts on ISS".format(len(astronauts)))
print("And their names are :")
for astronaut in astronauts:
    print(astronaut.get('name'))
# another solution
df = pd.DataFrame(astronauts)
print(len(df['name']))


### Lab: Collect Jobs Data using Jobs API
api_url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"
r = requests.get(api_url)
data = r.json()
df = pd.DataFrame(data)

def get_number_of_jobs_T(technology):
    df_filterd = df[df['Key Skills'].str.contains(technology, case=False)]
    number_of_jobs = len(df_filterd)
    #your code goes here
    return technology,number_of_jobs

#print(get_number_of_jobs_T('Python'))

Locations = df['Location'].unique().tolist()
def get_number_of_jobs_L(location):
    df_filtered = df[df['Location'].str.contains(location, case=False)]
    number_of_jobs = len(df_filtered)
    #your coe goes here
    return location,number_of_jobs

wb=Workbook()
ws=wb.active

for loco in Locations:
    ws.append(get_number_of_jobs_L(loco))
wb.save("output.xlsx")

df_ex = pd.read_excel("output.xlsx")
df_ex.columns = ['Location', 'Num_Jobs']

max_index = df_ex['Num_Jobs'].idxmax()
location = df_ex.loc[max_index, 'Location']
print(location)