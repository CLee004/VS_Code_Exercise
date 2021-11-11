def present_value(FV, Rate, Num, Time):
    PV = FV/((1+Rate/100)**(Num*Time))
    print(f'')