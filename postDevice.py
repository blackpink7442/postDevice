import requests
import json
import time
import threading
import keyboard 
value = 135.0
stopthread = 0
url = 'http://tsukumonet.ddns.net:21090/device/blackpink'
session_requests = requests.Session()
headers = {
    'content-type': 'application/json'
}

class MyThread(threading.Thread):
    def __init__(self,thread_id, name, delay):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.delay = delay
                  
    def run(self):
        print('開始執行緒:'+self.name)
        postdevice(self.name,self.delay,6)        
       
class MyThread2(threading.Thread):
    def __init__(self,thread_id, name):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name

    def run(self):
        print('開始執行緒'+self.name)
        changevalue(self.name,1)

def changevalue(thread_name,counter):
    while counter<2:
        global value , stopthread
        print('-------------Enter new value-------------')
        order = input()
        if order == "777":
            stopthread = 1
            time.sleep(5)
            order = 0
            stopthread = input()
            if stopthread == "0":
                event.set()
                event.clear()
        else:
            value = order
   

def postdevice(thread_name,delay,counter):
    global stopthread
    while counter >= 1:
        data1 = {
            "setData":{
                "deviceName": "blackpink",
                "value": value,
                "unit": "cm"
            }
        }
        time.sleep(delay)
        response = session_requests.post(url, data =json.dumps(data1),headers = headers)
        if response.ok == True:
            print(thread_name+' [Success]')
            print(response.text)

        else:
            print(thread_name+'Error')

        if stopthread == 1:
            print('Stop PostThread')
            event.wait(600)
       
event = threading.Event()            
PostThreda1 = MyThread(1, 'PostThreda-1', 5)
changevalue1 = MyThread2(2,'ChangeValue-1')
PostThreda1.start()
changevalue1.start()
PostThreda1.join()
changevalue1.join()






