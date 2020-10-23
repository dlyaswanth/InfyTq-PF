#PF-Tryout

def generate_next_date(day,month,year):
    #Start writing your code here
    monthday=[31,28,31,30,31,30,31,31,30,31,30,31];
    if month==12:
        if day==monthday[month-1]:
            day=1;month=1;year+=1;
    else:
        if day==monthday[month-1]:
            day=1;month+=1;
        else:
            day+=1;
    print(day,"-",month,"-",year)
generate_next_date(30,6,2015)