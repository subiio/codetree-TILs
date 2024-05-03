n = int(input())

class Weather:
    def __init__(self,y,m,w):
        self.date =y
        self.dwo =m
        self.weather =w
weather_cast = []

for _ in range(n):
    date,dwo,weather = tuple(input().split())
    weather_cast.append(Weather(date,dwo,weather))

min_idx =0
list2 = []
for i in range(n):
    if weather_cast[i].weather =="Rain":
        list2.append(weather_cast[i])

(''.join(list2[0].date.split('-')))
min_idx =  0
for j in range(len(list2)):
    if (''.join(list2[min_idx].date.split('-')))> (''.join(list2[j].date.split('-'))):
        min_idx = j

print(list2[min_idx].date,list2[min_idx].dwo,list2[min_idx].weather)