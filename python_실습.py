import csv

with open('차량관리.csv','r', newline = '') as file:
    csv_reader = csv.reader(file, delimiter = ',', quotechar = '"') # 읽기 객체 생성
    # quotechar은 묶어야하는 string을 처리할 때 사용된다. 무엇으로 묶을지.
    for line in csv_reader:
        print(line)
