import os
import csv
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#建立record目錄
#directory = os.path.abspath("./record")

#if not os.path.isdir(directory):  # 取得絕對路徑，尚未建立前狀態為false ( not false = true )
    #os.makedirs(directory)  # 建立record目錄，true才會執行
    # 一旦執行完第一次後，布林值就變成false，所以第二次後就永遠是false，不會再建立。

full_path_csvFile = None
db = None

def recordData(distance,lightValue,absolute_Path):
    global full_path_csvFile
    global db
    current = datetime.now()   #抓取現在的時間
    current_date = current.date()   #抓取現在時間中的日期
    filename = current_date.strftime("%Y-%m-%d.csv")  #將抓到的日期轉為文字str
    relative_Path = "record/"
    full_path_record = os.path.join(absolute_Path,relative_Path)

    if not os.path.isdir(full_path_record):  # 取得絕對路徑，尚未建立前狀態為false ( not false = true )
        os.makedirs(full_path_record)  # 建立record目錄，true才會執行
        # 一旦執行完第一次後，布林值就變成false，所以第二次後就永遠是false，不會再建立。

    currentFiles = os.listdir(full_path_record)  #使用listdir()顯示目錄內容
    full_path_csvFile = os.path.join(full_path_record,filename)
    print(full_path_csvFile)

    if filename not in currentFiles:
        #建立檔案
        file = open(full_path_csvFile,'w',encoding='utf-8',newline='')
        header_writer = csv.writer(file)
        header_writer.writerow(["日期","距離","光線"])
        file.close()
    #加入資料
    with open(full_path_csvFile,"a",newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([current.strftime("%Y-%m-%d %H:%M:%S"),distance,lightValue])
    
    #將資料加入至firestore
    #print("要加入的資料")
    #print('日期',current.strftime("%Y-%m-%d %H:%M:%S"))
    #print('距離',distance)
    #print('亮度',lightValue)
    relative_path_key = "private/raspberry1-47370-firebase-adminsdk-9eb4u-92da494d53.json"
    full_path_key = os.path.join(absolute_Path,relative_path_key)
    print("key:",full_path_key)
    if db is None:
        cred = credentials.Certificate(full_path_key)
        app = firebase_admin.initialize_app(cred)
        db = firestore.client()

#讀取資料
def getData():
    with open(full_path_csvFile,"r",newline='') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
    return data