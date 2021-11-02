import math

def Time(FV, PV, Rate, Num):
    num = math.log(FV/PV)/(Num*math.log(1+Rate))
    print(f'')