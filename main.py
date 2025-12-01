# This is a data cleaning application

# importing dependencies
import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random

#data_path = 'day19_sales.csv'
#data_name = 'Jan_sales'

def data_cleaning_master(data_path , data_name):

    print("Thank you for giving the details!")

    sec = random.randint(1,4)
    print(f"Please wait for {sec}seconds! Checking file path")
    time.sleep(sec)

    # checking if the path exists
    if not os.path.exists(data_path):
        print("Incorrect path! Try again with correct path")
        return
    else:
        #checking the data type
        if data_path.endswith('.csv'):
            print('Dataset is csv!')
            data = pd.read_csv(data_path , encoding_errors='ignore')

        elif data_path.endswith('.xlsx'):
            print('Dataset is xlsx!')
            data = pd.read_excel(data_path)

        else:
            print("Unknown file type")
            return
        
    #print dealy msg
    sec = random.randint(1,4)
    print(f"Please wait for {sec}seconds! Checking total columns and rows")
    time.sleep(sec)
    

    # showing number of records
    print(f"Dataset contain total rows : {data.shape[0]} \n total columns : {data.shape[1]}")

    #start cleaning

    #print dealy msg
    sec = random.randint(1,4)
    print(f"Please wait for {sec}seconds! Checking total duplicates")
    time.sleep(sec)
    
    # checking duplicates
    duplicates = data.duplicated()
    Total_duplicates = data.duplicated().sum()

    print(f"Datasets has total duplicates records : {Total_duplicates}")

    #print dealy msg
    sec = random.randint(1,4)
    print(f"Please wait for {sec}seconds! Saving total duplicates rows")
    time.sleep(sec)
    

    # saving the duplicates 
    if Total_duplicates > 0:
        duplicate_records = data[duplicates]
        duplicate_records.to_csv(f'{data_name}_duplicates.csv', index = None)

    #deleting duplicates

    df = data.drop_duplicates()

    #print dealy msg
    sec = random.randint(1,10)
    print(f"Please wait for {sec}seconds! Checking for missing values")
    time.sleep(sec)
    

    #find missing values
    total_missing_values = df.isnull().sum().sum()
    missing_value_columns = df.isnull().sum()

    print(f"Dataset has total missing values : {total_missing_values}")
    print(f"Dataset contain missing value by columns \n {missing_value_columns}")

    # Dealing with missing values
    #fillna --int and float
    #dropna -- any object

    #print dealy msg
    sec = random.randint(1,6)
    print(f"Please wait for {sec}seconds! Checking Datasets")
    time.sleep(sec)
    

    columns = df.columns

    for col in columns:
        #fiiling mean for numeric columns all rows
        if df[col].dtype in (float,int):
            df[col] = df[col].fillna(df[col].mean())

        else:
            # dropping all rows with missing records for number column
            df.dropna(subset=col , inplace=True)

    #print dealy msg
    sec = random.randint(1,5)
    print(f"Please wait for {sec}seconds! Exporting datasets")
    time.sleep(sec)
    

    # data is cleaned
    print(f"Congratualtions dataset is cleaned! \n Number of Rows : {df.shape[0]} Numbeer of Columns : {df.shape[1]}")

    #saving the clean dataset
    df.to_csv(f'{data_name}_clean_data.csv',index=None)
    print("Dataset is saved!")


if __name__ == "__main__":

    print("Welcoming to Data Cleaning Master!")
    
    # ask path and file and name
    data_path = input("Please enter dataset path :")
    data_name = input("Please enter dataset name :")

    #calling the function
    data_cleaning_master(data_path , data_name)


