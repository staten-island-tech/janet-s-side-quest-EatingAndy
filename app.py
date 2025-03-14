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
print(data)

def sale_average():
    for row in data[1:]:
        name = row[0]
        sales = map(int, row[1:])
        Sum = sum(sales)
        for sale in row[1:]:
            average = Sum % sale
        print(name, average)
sale_average()

def listed():
    for row in data[1:]:
        name = row[0]
        sales = map(int, row[1:])
        Sum = sum(sales)
        for sale in row[1:]:
            average = Sum % sale
            something = [].sort(key=lambda x: x[1],reverse=True)
        something.append(average)
        print(name, something)
listed()

    

