# importing
import csv
import pandas as pd
import sys
# csv file name
file2 = "Attendance\Attendance_24-05-2021.csv"
file1 = "StudentDetails\StudentDetails.csv"

# initializing the titles and rows list
fields1 = []
rows1 = []
fields2=[]
rows2=[]

# reading csv file

with open(file1, 'r') as csvfile1:
    # creating a csv reader object
    csvreader1 = csv.reader(csvfile1)
      
    # extracting field names through first row
    fields1 = next(csvreader1)
  
    # extracting each data row one by one
    for row in csvreader1:
        rows1.append(row)
        

with open(file2, 'r') as csvfile2:
    # creating a csv reader object
    csvreader2 = csv.reader(csvfile2)
      
    # extracting field names through first row
    fields2 = next(csvreader2)
  
    # extracting each data row one by one
    for row in csvreader2:
        rows2.append(row)
  
  
with open('Report.txt','w') as f:
    sys.stdout=f
    print("Total no. of Registrations: %d"%(csvreader1.line_num))
    print(" ")
    print("List of Registered Students are:")
    print(" ")
    for i in rows1:
        print(i)
    print(" ")
    print("Total no. of Attendance Records: %d"%(csvreader2.line_num))
    print(" ")
    for i in rows2:
        print(i)

