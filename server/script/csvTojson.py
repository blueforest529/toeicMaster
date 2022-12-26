import csv
import json

csvfile = open('file.csv', 'r', encoding='UTF-8')
jsonfile = open('file.json', 'w')

fieldnames = ("버전","위치","키 값","한국어","일어","영어","러시아어","우크라이나어")
reader = csv.DictReader( csvfile, fieldnames)

arr = {}
for idx, row in enumerate(reader):
    key = row['키 값'] 
    del(row['키 값'])
    arr[key] = row


print(arr)
# out = json.dumps( [ row for row in reader ] )


jsonfile.write(json.dumps(arr))

