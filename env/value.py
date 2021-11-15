import future_value
import present_value
import rate
import num
import time


class value:
    def __init__(self, FV, PV, Rate, Num, Time):
        self.FV = FV
        self.PV = PV
        self.Rate = Rate
        self.Num = Num
        self.Time = Time

    FV = eval(input('What is the future value that you would like your account to be?": '))
    PV = eval(input('How much money do you have to invest today?' ))
    Rate = eval(input('What rate do you need for your present vale to become your future value? '))
    Num = eval(input('How many time in the year do you want your investment to compund? '))
    Time = eval(input('How long do you want to hold your investment for? '))

    #Hi how are you???

    