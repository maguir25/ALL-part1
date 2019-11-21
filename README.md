import csv

with open("google_fit_data.csv", mode='rb') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    x_sum = x_length = 0
    for row in csv_reader:
        try:
            x = int(row['Calories_(kcal)'])
            x_sum += int(x)
            x_length += 1
        except ValueError:
            print("Error converting: {0:s}".format(x))
    x_average = x_sum / x_length
    print(x_average)
        
            
        
    
