import pandas as pd 

allcountry = {
    'country':['brazil','india','bangladesh','south-africa'],
    'capital':['brasilia','new delhi','dhaka',' pretoria'],
    'area' : [200.4,100.10,10.47,60.58]
}

#print(type(allcountry))
#print(allcountry['country'][0])

df = pd.DataFrame(allcountry)
print(df)
