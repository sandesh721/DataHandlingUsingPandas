# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 13:33:47 2023

@author: Sandesh
"""

import pandas as pd
from pathlib import Path
import os
class pandasProgram:
    def show_data(data):
        try:
            n = int(input("Enter the number of rows to be printed: "))
            print(data.head(n))
        except:
            print("\nInvalid input")
            pandasProgram.show_data(data)
    def droping(data,col):
        
        try:
            choice = int(input("Do you want to:-\n1.Drop the column\n2.Try Another Operation\nEnter the choice(Enter 0 to go back): "))
            if choice==0:
                return -1
        except:
                print("Invalid choice")
                pandasProgram.droping(data,col)
        if choice == 1:
            data.drop(col,axis=1,inplace=True)
            print(f"Successfylly Dleted the column {col}")
            ch = input("Do you want continue with null opration(y/n): ")
            if ch.lower()=='y':
                try:
                    pandasProgram.nul(data)
                except:
                    print("Column name not found. Retry with Correct Name")
            else:
                pandasProgram.operation(data)
        elif choice==2:
            pandasProgram.nul(data)
        else:
            print("Enter valid input")
            pandasProgram.droping(data, col)
        return  
    def Desc(data):
        print("\n1.Describe specific column\n2.Show properties of each column\n3.Show dataset")
        try:
            ch=int(input("Enter the Choice(Enter 0 to go to MAIN MENU):"))
            if ch==0:
                return -1
            elif ch==1:
                col_name = data.columns
                for c in col_name:
                    print(c, end=" ")
                try:
                    col = input("\n\nEnter the column name: ")
                    data[col]
                except:
                    print("Enter valid column name")
                    pandasProgram.Desc(data)
                # mean_val = data[col].mean()
                count_val = data[col].count()
                # std_val = data[col].std()
                min_val = data[col].min()
                # percentile_val = data[col].quantile(0.25)
                max_val = data[col].max()
                
                # print("Mean  :%0.2f"%mean_val)
                print("Count :",count_val)
                # print("Std   :%0.2f"%std_val)
                print("Min   :",min_val)
                # print("0.25  :%0.2f"%percentile_val)
                print("Max   :",max_val)
                
            elif ch==2:
                 print(data.info())
                
            elif ch==3:
                pandasProgram.show_data(data)
            
            else:
                print("Invalid")
        except:
                print("Invalid choice")
                pandasProgram.Desc(data)
        
        pandasProgram.Desc(data)
    def nul(data):
        print("\nCount of null values:\n\n")
        print(data.isna().sum())
        col_name = data.columns
        for c in col_name:
            print(c, end=" ")
        print("\n1. Replace Null with Zero\n2. Fill Null (with Mean)\n3. Fill Null (with Median)\n4. Fill Null (with Mode)\n")
        try:
            ch = int(input("Enter the choice(Enter 0 to go back): "))
            if ch==0:
                return -1
        except:
                print("Invalid choice")
                pandasProgram.nul(data)
        try:
            col = input("\n\nEnter the column name: ")
            data[col]
        except:
            print("Enter valid column name")
            pandasProgram.nul(data)
        
    
        
    
        # def handle_operation(fill_value, operation):
        #     try:
        #         print("Hiii")
        #         fill_value = eval(f"{fill_value.operation}")   # Evaluate the operation to get the method or function
        #         data[col].fillna(fill_value, inplace=True)
        #     except Exception as e:
        #         print(f"Operation cannot be performed: {e}")
        #         choice = input("Do you want to drop the column? (y/n): ")
        #         if choice.lower() == 'y':
        #             droping(col)
        #         else:
        #             return 0
    
        if ch == 1:
            # handle_operation(0, '')
            data[col].fillna(0, inplace=True)
        elif ch == 2:
            # handle_operation(data[col], 'mean()')
            try:
                data[col].fillna(data[col].mean(), inplace=True)
            except Exception as e:
                print(f"Operation cannot be performed: {e}")
                pandasProgram.droping(data,col)
        elif ch == 3:
            # handle_operation(data[col], 'median()')
            try:
                data[col].fillna(data[col].median(), inplace=True)
            except Exception as e:
                print(f"Operation cannot be performed: {e}")
                pandasProgram.droping(data,col)
        elif ch == 4:
            # handle_operation(data[col], 'mode()')
            try:
                data[col].fillna(data[col].mode().iloc[0], inplace=True)
            except Exception as e:
                print(f"Operation cannot be performed: {e}")
                pandasProgram.droping(data,col)
       
    
        pandasProgram.nul(data)
        
    def encod(data):
        print("\n1.Show Categorical Columns\n2.Performing on hot encoding\n ")
        try:    
            ch=int(input("Enter the Choice(Enter 0 to go back):"))
        except:
            print("\nIvalid input")
            pandasProgram.encod(data)
        if ch==1:
            print(data.nunique())
        elif ch==2:
            hot_encode = pd.get_dummies(data, columns = ['Sex', 'Pclass'])
            data = hot_encode
            print(hot_encode)
        elif ch==0:
            return -1
        pandasProgram.encod(data)
    # def feature(data):
    #     print("\n1.Performing normalization\n2.Performing Standardization\n ")
    #     try:    
    #         ch=int(input("Enter the Choice(Enter 0 to go back):"))
    #     except:
    #         print("\nIvalid input")
    #         pandasProgram.feature(data)
    #     if ch==1:
    #         print()
    #     elif ch==2:
            
    #         print()
    #     elif ch==0:
    #         return -1
    #     pandasProgram.feature(data)
    def down(data):
        data.to_csv("PandasCLI.csv")
        loc=os.getcwd()
        print(f"File is successfully saved at {loc}")
        
    def operation(data):
        condition=True
        while(condition):
            print("\n\nOperations:\n1.Data Description\n2.Handling Null values\n3.Encoding categorial data\n4.Download modfied data\n5.Show Data")
            try:    
                ch=int(input("Enter the Choice(Enter 0 to exit):"))
            except:
                 print('\nEnter valid inputing') 
                 pandasProgram.operation(data)    
            if ch==1:
                pandasProgram.Desc(data)
                
            elif ch==2:
                pandasProgram.nul(data)
                
            elif ch==3:
                pandasProgram.encod(data)
            
            # elif ch==4:
            #     pandasProgram.feature(data)
                
            elif ch==4:
                pandasProgram.down(data)
            elif ch==5:
                pandasProgram.show_data(data)
                
            elif ch==0:
                condition=False
                    
           
    def main():
        print("\n*****Welcome to Pandas*****")
        
        print("Enter the name of the file mentioned below to do the operations")
        # folder path
        cwd = os.getcwd()
        
        # list file and directories
        # res = os.listdir(cwd)
        for file in Path(cwd).rglob('*.csv'):
            print(file.name,end=" ") 
        
        tit = input("\nEnter the file name: ")
        try: 
            data = pd.read_csv(tit)
        except:
            print("\nEnter valid file name")
            pandasProgram.main()
        pandasProgram.show_data(data)
        pandasProgram.operation(data)
        
if __name__=='__main__':
     pandasProgram.main()   
                    
    