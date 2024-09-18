n = int(input())
forcast_list = []

for _ in range(n):
    forcast_list.append(list(input().split("-")))

forcast_list2 = []
for i in forcast_list:
    for j in range(len(i)):
        forcast_list2.append(i[j].split(" "))


# print(forcast_list2)

earliest_years = None
earliest_month = None
earliest_day = None
earliest_data = None
earliest_weather = None

for i in range(0,len(forcast_list2),3):
    # print(i)
    years_ind = i
    month_ind = i+1
    day_ind = [i+2,0]
    data_ind = [i+2,1]
    weather_ind = [i+2,2]
    if forcast_list2[weather_ind[0]][weather_ind[1]] == 'Rain':
        if earliest_years == None:
            earliest_years = forcast_list2[years_ind]
            earliest_month = forcast_list2[month_ind]
            earliest_day = forcast_list2[day_ind[0]][day_ind[1]] 
            earliest_data = forcast_list2[data_ind[0]][data_ind[1]] 
            earliest_weather = forcast_list2[weather_ind[0]][weather_ind[1]]
        else:
            if forcast_list2[years_ind] < earliest_years:
                earliest_years = forcast_list2[years_ind]
                earliest_month = forcast_list2[month_ind]
                earliest_day = forcast_list2[day_ind[0]][day_ind[1]] 
                earliest_data = forcast_list2[data_ind[0]][data_ind[1]]  
                earliest_weather = forcast_list2[weather_ind[0]][weather_ind[1]]
            elif forcast_list2[years_ind] == earliest_years:
                if forcast_list2[month_ind] < earliest_month:
                    earliest_years = forcast_list2[years_ind]
                    earliest_month = forcast_list2[month_ind]
                    earliest_day = forcast_list2[day_ind[0]][day_ind[1]] 
                    earliest_data = forcast_list2[data_ind[0]][data_ind[1]] 
                    earliest_weather = forcast_list2[weather_ind[0]][weather_ind[1]]
                elif forcast_list2[month_ind] == earliest_month:
                    if forcast_list2[day_ind[0]][day_ind[1]]  < earliest_day:
                        earliest_years = forcast_list2[years_ind]
                        earliest_month = forcast_list2[month_ind]
                        earliest_day = forcast_list2[day_ind[0]][day_ind[1]] 
                        earliest_data = forcast_list2[data_ind[0]][data_ind[1]]  
                        earliest_weather = forcast_list2[weather_ind[0]][weather_ind[1]]
                    elif forcast_list2[day_ind[0]][day_ind[1]]  == earliest_day:
                        if forcast_list2[data_ind[0]][data_ind[1]]  < earliest_data:
                            earliest_years = forcast_list2[years_ind]
                            earliest_month = forcast_list2[month_ind]
                            earliest_day = forcast_list2[day_ind[0]][day_ind[1]] 
                            earliest_data = forcast_list2[data_ind[0]][data_ind[1]] 
                            earliest_weather = forcast_list2[weather_ind[0]][weather_ind[1]]
                        else:
                            pass

                    
                    else:
                        pass

                else:
                    pass
            else:
                pass
    else:
        pass

data = earliest_years[0]+"-"+earliest_month[0]+"-"+earliest_day

print(data,earliest_data,earliest_weather)