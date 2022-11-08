import os
from datetime import datetime

#建立record目錄
directory = os.path.abspath("./record")
if not os.path.isdir(directory):  # 取得絕對路徑，尚未建立前狀態為false ( not false = true )
    os.makedirs(directory)  # 建立record目錄，true才會執行
    # 一旦執行完第一次後，布林值就變成false，所以第二次後就永遠是false，不會再建立。


def recordData(distance,lightValue):
    current = datetime.now()   #抓取現在的時間
    current_date = current.date()   #抓取現在時間中的日期
    filename = current_date.strftime("%Y-%m-%d.csv")  #將抓到的日期轉為文字str
    currentFiles = os.listdir(directory)  #使用listdir()顯示目錄內容
    if filename not in currentFiles:
        #建立檔案
        file = open(f"{directory}/{filename}",'w',encoding='utf-8')
        file.close()
    