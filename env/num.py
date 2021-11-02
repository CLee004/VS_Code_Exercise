import math

def Num(FV, PV, Rate, Time):
    num = math.log(FV/PV)/(Time*math.log(1+Rate))
    print(f'')