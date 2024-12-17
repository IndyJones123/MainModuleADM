from MainModuleADM.Utils.distance import i_distance

#Paris
long1 = 2.3522
lat1 = 48.8566

#Krakow
long2 = 19.9450
lat2 = 50.0647

#Mt. Evereset
lat3 = 27.9881
long3 = 86.9250

#Empire State Building
lat4 = 40.7484
long4 = -73.9857

#Jarak Paris & Krakow
asd = i_distance(long1,lat1,long2,lat2)
print(f'Jarak Paris dan Krakow = {asd}')

#Jarak Mt.Everest & Empire State Building
dsa = i_distance(long3,lat3,long4,lat4)
print(f'Jarak Evereset dan Empire State = {dsa}')

#Source Example Data Distance In https://www.omnicalculator.com/other/latitude-longitude-distance

