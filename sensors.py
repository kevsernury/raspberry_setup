import time
from datetime import datetime

print("Sensor verileri dosyaya yaziliyor")

raspName = "raspberry3"
sensor1_name = raspName + 'sensor1.txt' 
sensor2_name = raspName + 'sensor2.txt' 

sensor1 = 10
sensor2 = 30

while True:
    now = datetime.now()
    current_time = now.strftime("%d/%m/%Y %H:%M:%S")
    
    with open(sensor1_name, 'a') as f:
        f.write(str(sensor1) + ' ' + current_time + '\n')
    f.close()

    with open(sensor2_name, 'a') as f:
        f.write(str(sensor2) + ' ' + current_time + '\n')
    f.close()
    
    sensor1 += 1
    sensor2 += 2
    
    print("yaziliyor")
    time.sleep(10)
    

