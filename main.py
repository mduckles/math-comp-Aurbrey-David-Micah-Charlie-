from model import SlingShot as S
import csv

feilds = ['Spring','Size','Angle','Force']

def range_value(low,high):
    arr = []
    for i in range(low,high):
        arr.append(i)
    return arr

def main():
    with open('test.csv','w') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(feilds) 
        for i,l in enumerate(range_value(-100,100)):
            Test = S((82*l)/240,l,70)
            row=[(82*l)/240,l,70,Test.EnergyOutcome()]
            csvwriter.writerow(row)
            


if __name__ == '__main__':
    main()