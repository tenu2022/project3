import os

#建立record目錄
directory = os.path.abspath("./record")
if not os.path.isdir(directory):  # 取得絕對路徑，尚未建立前狀態為false ( not false = true )
    os.makedirs(directory)  # true才會執行，建立record目錄
    # 一旦執行完第一次後，布林值就變成false，所以第二次後就永遠是false，不會再建立。


def recordData(distance,lightValue):
    print("紀錄")
    