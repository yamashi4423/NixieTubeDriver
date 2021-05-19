import RPi.GPIO as GPIO
import datetime
from time import sleep

# ニキシー管のピンの設定
nixie1 = 22
nixie2 = 10
nixie3 = 9
nixie4 = 11

# ドライバのピンの設定
driverA = 23
driverB = 25
driverC = 8
driverD = 24

# ディレイの時間の設定
delaytime = 2
breaktime = 1


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

# 10進数から2進数へ
def dec2bin(num):
    bin = [0, 0, 0, 0]
    i = 0
    while int(num) != 0:
        bin[i] = int(num%2)
        num = num/2
        i = i+1
    bin.reverse()
    return bin

# 指定したピンに指定した数字を表示
def numPrint(num, pin):
    dec2bin(num)
    GPIO.output(driverA, dec2bin(num)[3])
    # print("driverA is", dec2bin(num)[3])
    GPIO.output(driverB, dec2bin(num)[2])
    # print("driverB is", dec2bin(num)[2])
    GPIO.output(driverC, dec2bin(num)[1])
    # print("driverC is", dec2bin(num)[1])
    GPIO.output(driverD, dec2bin(num)[0])
    # print("driverD is", dec2bin(num)[0])
    GPIO.output(pin, GPIO.HIGH)
    # print("HIGH is ", pin)
    sleep(delaytime)
    GPIO.output(pin, GPIO.LOW)
    # print("LOW is", pin)
    sleep(breaktime)

# main
try:
    while True:
        # 現在時刻を取得
        now = datetime.datetime.now()
        hour = now.hour
        hour1 = int(hour/10)
        hour2 = hour%10
        minute = now.minute
        minute1 = int(minute/10)
        minute2 = minute%10

        # ニキシー管を点灯
        numPrint(hour1, nixie1)
        # print("hour1 is " , hour1)
        # print("\n")
        numPrint(hour2, nixie2)
        # print("hour2 is " , hour2)
        # print("\n")
        numPrint(minute1, nixie3)
        # print("hour3 is " , minute1)
        # print("\n")
        numPrint(minute2, nixie4)
        # print("hour4 is " , minute2)
        # print("\n")

finally:
    GPIO.cleanup()