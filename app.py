## This function opens the CSV for You!
def csv_to_list(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [int(value) if value.isdigit() else value for value in row]
            data_list.append(row)

    return data_list

file_path = "SalesData.csv"  
data = csv_to_list(file_path)
print(data)  # Output the list

def sale_total():
        x = {row[0]: sum([int(x) for x in row[1:]]) for row in data[1:]}
        return x
sale_total()

""" def location():

    
average_sales = map() """




    

