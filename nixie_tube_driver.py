import RPi.GPIO as GPIO
import datetime
from time import sleep

# ニキシー管のピン
nixie1 = 22
nixie2 = 10
nixie3 = 9
nixie4 = 11

# ドライバのピン
driverA = 18
driverB = 25
driverC = 24
driverD = 23

# ディレイ時間設定
delaytime = 0.001
breaktime = 0.001

# ピンの準備
GPIO.setmode(GPIO.BCM)
GPIO.setup(nixie1, GPIO.OUT)
GPIO.setup(nixie2, GPIO.OUT)
GPIO.setup(nixie3, GPIO.OUT)
GPIO.setup(nixie4, GPIO.OUT)
GPIO.setup(driverA, GPIO.OUT)
GPIO.setup(driverB, GPIO.OUT)
GPIO.setup(driverC, GPIO.OUT)
GPIO.setup(driverD, GPIO.OUT)

# 10進数→2進数
def dec2bin(num):
    bin = [0, 0, 0, 0]
    i = 0
    while int(num) != 0:
        bin[i] = int(num%2)
        num = num/2
        i = i+1
    bin.reverse()
    return bin

# 指定した数字を指定したニキシー管のピンに表示
def numPrint(num, pin):
    GPIO.output(driverA, dec2bin(num)[3])
    GPIO.output(driverB, dec2bin(num)[2])
    GPIO.output(driverC, dec2bin(num)[1])
    GPIO.output(driverD, dec2bin(num)[0])
    GPIO.output(pin, GPIO.HIGH)
    sleep(delaytime)
    GPIO.output(pin, GPIO.LOW)
    sleep(breaktime)

# main
try:
    while True:
        # 時間の取得
        now = datetime.datetime.now()
        hour = now.hour
        hour1 = int(hour/10)
        hour2 = hour%10
        minute = now.minute
        minute1 = int(minute/10)
        minute2 = minute%10
        
        # 点灯
        numPrint(hour1, nixie1)
        numPrint(hour2, nixie2)
        numPrint(minute1, nixie3)
        numPrint(minute2, nixie4)

finally:
    GPIO.cleanup()