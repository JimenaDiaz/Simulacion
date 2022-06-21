import pandas as pd
from datetime import datetime
import random
import threading
import time
import csv


in_index = 0
out_index = 0
reporte=[]
data=[]
num_simulacion=10


class Producer(threading.Thread):
  def run(self):
    global reporte, in_index,out_index,num_simulacion
    id_dispositivo=0
    id=1
    items_produced =0
    while items_produced < num_simulacion :
      id_dispositivo+=1
      metrica = random.randint(10, 100)  
      date = (str( datetime.now()))
      dic={"ID_Dispositivo": id_dispositivo, "Metrica": metrica, "Timestamp":date }
      reporte.insert(in_index,dic)
      print('Producer',reporte[in_index])
      in_index += 1
      items_produced += 1
      time.sleep(1.5)

class Crud:
  def __init__(self):
    header=['Metrica', 'Timestamp']
    data=[]
    with open ('data.csv','a') as csv_data:
      write_file = csv.writer(csv_data)
      write_file.writerow(header)

  def write(self,registro):
    df1 = pd.DataFrame(registro, index=[registro['ID_Dispositivo']],columns=['Metrica', 'Timestamp'])
    df1.to_csv('data.csv', mode='a', index=False, header=False)
         

class Consumer(threading.Thread):
  def run(self):
     global reporte, out_index,num_simulacion
     items_produced =0
     while items_produced < num_simulacion :
        crud.write(reporte[out_index])
        print('Consumer', reporte[out_index])
        out_index += 1
        items_produced += 1
        time.sleep(2.5)

p = Producer()
c = Consumer()
crud=Crud()

p.start()
c.start()

p.join()
c.join()