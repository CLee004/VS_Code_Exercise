import math

def rate(FV, PV, Num, Time):
    rate = math.exp(math.log(FV/PV)/(Num*Time))-1
    print(f'')