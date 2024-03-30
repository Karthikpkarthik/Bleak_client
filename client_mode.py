from bleak import BleakClient
import time
import csv
import asyncio
import matplotlib.pyplot as plt
i=1
ADDRESS ="00:18:80:00:BD:02"
SER_UUID='e0262760-08c2-11e1-9073-0e8ac72e1001'
CHAR_UUID='e0262760-08c2-11e1-9073-0e8ac72e0001'
text_to_write=['uptime','temp','hrm','spo2']
cvs_list=[['uptime','temp','hrm','spo2']]
time=0
count=0
temp=0
spo2=0
hrm=0
x_data=list()
y1_data=list()
y2_data=list()
y3_data=list()
async def fn(address):
    global i,count
    async with BleakClient(address) as client:
        if client.is_connected:
            print("connected")
        # services =  client.services
        plt.ion()
        fig1, ax1 = plt.subplots()
        ax1.set_xlabel('Time')
        ax1.set_ylabel('temp')
        fig2, ax2 = plt.subplots()
        ax2.set_xlabel('Time')
        ax2.set_ylabel('hrm')
        fig3, ax3 = plt.subplots()
        ax3.set_xlabel('Time')
        ax3.set_ylabel('spo2')
        global x_data, y1_data,y2_data,y3_data
        await client.start_notify(CHAR_UUID,notify_handler)
        
        while count!=100:
            await asyncio.sleep(4)
            await client.write_gatt_char(CHAR_UUID, text_to_write[0].encode(), response=True)
            await client.write_gatt_char(CHAR_UUID, text_to_write[1].encode(), response=True)
            await client.write_gatt_char(CHAR_UUID, text_to_write[2].encode(), response=True)
            await client.write_gatt_char(CHAR_UUID, text_to_write[3].encode(), response=True)
            count+=1   
            ax1.clear()
            ax1.plot(x_data, y1_data,'bo-',label='Data 1')
            ax2.plot(x_data, y2_data,'go-',label='Data 2')
            ax3.plot(x_data, y3_data,'ro-',label='Data 3')
            ax1.relim()
            ax1.autoscale_view()
            fig1.canvas.draw()
            fig1.canvas.flush_events()
            ax2.relim()
            ax2.autoscale_view()
            fig2.canvas.draw()
            fig2.canvas.flush_events()
            ax3.relim()
            ax3.autoscale_view()
            fig3.canvas.draw()
            fig3.canvas.flush_events()
            
        await client.stop_notify(CHAR_UUID)
        # with open("data1.csv",'w')as file:
        #     write=csv.writer(file)
        #     write.writerows(cvs_list)

        # for service in services:
        #     print(f"Service UUID: {service.uuid}")
        #     for characteristic in service.characteristics:
        #         print(f"  Characteristic UUID: {characteristic.uuid}")   
        #         print(f"    properties:{characteristic.properties}")
        #         print(f"       Handle: {characteristic.handle}")
                
        await asyncio.sleep(100)
            
def notify_handler(sender,data):
    global i,cvs_list
    global hrm,temp,spo2,time
    data=data.hex()
    data=int(data,16)
    if(i==1):
        print(f"uptime:{data}m") 
        time=data
        x_data.append(time)
    elif(i==2):
        print(f"temp:{(data+200)/10}c")
        temp=(data+200)/10 
        y1_data.append(temp)  
    elif(i==3):
        print(f"hrm:{data}")
        hrm=data
        y2_data.append(hrm) 
    elif(i==4):
        print(f"spo2:{data}") 
        spo2=data
        y3_data.append(spo2)
        i=0 
        # cvs_list.append([time,temp,hrm,spo2])
        
    i+=1

if __name__ == "__main__":
    asyncio.run(fn(ADDRESS))
    