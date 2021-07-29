'''
進行資料處理，
將組員整理好資料
整理成標準格式存入firestore
'''
import os
import json
from google.cloud import firestore

arr = os.listdir("./json")
# print(arr)

# 建立客戶端
db = firestore.Client()
items_ref = db.collection(u'items')
# 存入資料庫
for j in range(1, 5, 1):
    for i in range(1, 11, 1):
        with open(f'./json/style{j}-{i}.json', "r") as a_file:
                data=json.load(a_file)

        items_ref.add(document_data=data, document_id=f'style{j}-{i}')

# 進行資料處理
# for i in range(1, 11, 1):
#     with open(f'./json/style4-{i}.json', "r") as a_file:
#         data=json.load(a_file)
#     data["style"]="nature"
#     with open(f'./json/style4-{i}.json', "w") as a_file:
#         json.dump(data, a_file)


# with open(f'./json/style2-1.json', "r") as a_file:
#     data=json.load(a_file)
#     print(f"風格2",data["style"])

# with open(f'./json/style3-1.json', "r") as a_file:
#     data=json.load(a_file)
#     print(f"風格3",data["style"])

# with open(f'./json/style4-1.json', "r") as a_file:
#     data=json.load(a_file)
#     print(f"風格4",data["style"])