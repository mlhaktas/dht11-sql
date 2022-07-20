import serial
import datetime
from time import sleep
import sys
import mysql.connector


COM = 'COM5'# Control Arduino connected port and change port name
BAUD = 9600

ser = serial.Serial(COM, BAUD, timeout = .5)

mydb = mysql.connector.connect(
  host="Your Host",
  user="User Name",
  database="Database Name",
  password="Password"
)
mycursor = mydb.cursor()
sql = "INSERT INTO temphumd (date, temp, humd) VALUES (%s, %s, %s)"

print('Sicaklik, Nem Izleme - Kayit');
print('Cikis icin CTRL+C');
sleep(2)

if("-m" in sys.argv or "--monitor" in sys.argv):
	monitor = True
else:
	monitor= False

while True:
        val = str(ser.readline().decode().strip('\r\n'))
        if(monitor == True):
                if (val == "nem"):
                        print("nem")
                        sleep(5)
                        val = str(ser.readline().decode().strip('\r\n'))
                        nem = val
                        print(nem)
                if (val == "sicaklik"):
                        print("sicaklik")
                        sleep(5)
                        val = str(ser.readline().decode().strip('\r\n'))
                        sicaklik = val
                        print(sicaklik)
                        tarih = datetime.datetime.now()
                        tarih = tarih.strftime("%Y-%m-%d %H:%M:%S")
                        print(tarih)
                        print ("")
                        kyt = (tarih, nem, sicaklik)
                        print(kyt)
                        valtsn = (tarih, sicaklik, nem)
                        mycursor.execute(sql, valtsn)
                        mydb.commit()
