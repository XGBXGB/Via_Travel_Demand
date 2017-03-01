from model.fourstep.TripDistribution import *

productions = [98, 106, 122]
attractions = [102, 118, 106]

td = TripDistribution(productions, attractions)

distributions = td.getTripDistribution()
print(distributions)
p = [0, 0, 0]
a = [0, 0, 0]
for x in range(len(productions)):
    for y in range(len(attractions)):
        p[x] += distributions[x][y]
        a[y] += distributions[x][y]
print("productions: " + str(p))
print(a)