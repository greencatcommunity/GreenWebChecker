import os
import requests
import sys

os.system("figlet GreenWebCheck")
try:
        data = sys.argv[1]
except:
        print("syntax: python main.py text-file-name.txt")
        exit(0)

if data not in os.listdir():
        print("File is not present in CWD")
        exit(0)

with open(data,'r') as var:
        data = var.readlines()


for i in data:
        requesting = requests.get(i[:-1])
        if requesting.status_code == 200:
                print(i[:-1], "is Up")
        else:
                print(i[:-1],"is Down")
