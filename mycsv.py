import csv

def create_csv(file_name):
    with open(file_name,'w',newline='') as csv_file:
        writer = csv.writer(csv_file,delimiter=',')
        writer.writerow(['Name','Location'])
        writer.writerow(['Krishna','Bengaluru'])
        writer.writerow(['Rajani', 'Dhramavaram'])
        writer.writerow(['Cherry','Hyderabad'])
        writer.writerow(['Lucky','Hindupur'])

def read_csv(file_name):
    with open(file_name, 'r') as csv_file:
     reader = csv.reader(csv_file)
     for row in reader:
        print(row)

if __name__ == '__main__':
    create_csv('Myfamily.csv')
    read_csv('Myfamily.csv')




