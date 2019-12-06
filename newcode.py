#To create custom objects that are like tables
import csv

#To open the saved csv file from Google Takeout 
x = open("google_fit_data.csv", 'rt')
read = csv.reader(x)

#Define a function representing values of calories burned.
def calories(row):
    """This function will isolate a certain key and its value"""
    for row in read:
        del row[0]
    
    output = []
    with open( "google_fit_data.csv", 'rt', newline='') as f:
        reader = csv.reader(f)
        for counter, row in enumerate(reader):
            if counter > 1:
                # read only the header and first two rows
                break
            output.append(row[:0])
            print(row[2])

#Defining a function for distance values on the csv file
def distance(row):
    """This function will isolate a certain key and its value"""
    for row in read:
        del row[0]
    
    output = []
    with open( "google_fit_data.csv", 'rt', newline='') as f:
        reader = csv.reader(f)
        for counter, row in enumerate(reader):
            if counter > 0: 
                # read only the header and first two rows
                break
            output.append(row[:0])
            print(row[3])

#Creating variables as answers to the following question and instruction
answer1 = "calories"
answer2 = "distance"

#Creating strings to request the calories burned or distance done
input("Do you want to know this person's calories or distance? Please type answer in lowercase after pressing ENTER.....")
if input() in answer1:
    print(calories(1))
elif input() in answer2:
    print(distance(1))
else:
    print("The information you require does not exist")
