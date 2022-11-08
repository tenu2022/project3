import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tools import data,record


class CustomView(ttk.Treeview):   #建立ttk裡的treeview
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.heading('#1',text="日期")
        self.heading('#2',text="距離")
        self.heading('#3',text="光線")


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.label = tk.Label(self,text="",font=("arial",30))
        self.label.pack(padx=50,pady=30)
        self.customView = CustomView(self,column=('#1','#2','#3'),show='headings')
        self.customView.pack()

        self.change_time()
        self.window_time()
        
      
    def change_time(self):
        now = datetime.now()
        now_str = now.strftime("%Y-%m-%d %H:%M:%S")
        self.label.config(text=now_str)
        self.after_id = self.label.after(1000,self.change_time)

    def window_time(self):
        distance = data.getDistance()
        print(distance)
        if distance < 100.0: 
            print(f"距離:{distance:.2f}公分")
        else:
            print(f"距離:大於100公分")
            distance = 100

        lightValue = data.getLightValue()
        print(f"光線:{lightValue:.1f}")

        #紀錄資料
        record.recordData(distance=distance,lightValue=lightValue)

        #取得資料
        all_data = record.getData()
        print(all_data)
        self.window_id = self.after(1000 * 30,self.window_time)

    def delete_delay(self):
        self.label.after_cancel(self.after_id)
        self.after_cancel(self.window_id)
        self.destroy()
        
        
        


def main():
    window =  Window()
    window.title("數位時鐘")
    window.protocol("WM_DELETE_WINDOW",window.delete_delay)
    window.mainloop()

if __name__ == "__main__":
    main()