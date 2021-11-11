def future_value(PV, Rate, Num, Time):
    FV = PV*(1.0+Rate/100.0)**(Num*Time)
    print(f'The future value of your investment is {FV}.')