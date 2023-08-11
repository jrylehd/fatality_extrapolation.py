with open('2005-2007_torn.csv', 'r') as tornado:
    lines = tornado.readlines()

dictionary = {}
DATA = []
NEWDATA = ['Months,Fatalities']

for string in lines[1:]:
    
    x = string.split(',')
    month = x[2]
    fatalities = int(x[12])
    
    if month in dictionary.keys():
         dictionary[month] += fatalities
    else:
        dictionary[month] = fatalities

for key in dictionary:
    DATA.append((key, str(dictionary[key])))

for n in DATA:
    n = ','.join(list(n))
    NEWDATA.append(n)

with open('tornadoes.csv', 'w') as tornadoes:
    for y in NEWDATA:
        tornadoes.write(y + '\n')