import turtle
import builtins

turtle.up()
turtle.setpos(0, -(turtle.window_height() / 2 + -50))
turtle.down()
turtle.pencolor('green')
turtle.circle(min(turtle.window_height(), turtle.window_width()) / 2 - 50)

tornadoes = builtins.open('C:/Users/JRyleHD/Desktop/Projects/tornadoes.csv', 'r')
lines = tornadoes.readlines()

dictionary = {}
deaths = []

for string in lines[1:]:
    
    x = string.replace('\n', '')
    x = x.split(',')
    month = x[0]
    fatalities = int(x[1])
    
    if month in dictionary.keys():
         dictionary[month] += fatalities
    else:
        dictionary[month] = fatalities
        
for key in dictionary:
    deaths.append(dictionary[key])

angle = 0
for key in dictionary:
    if dictionary[key] > 0:
        turtle.pencolor('black')
        turtle.up()
        turtle.home()
        turtle.seth(angle + (float(dictionary[key] / sum(deaths) * 360))/2)
        angle += float(dictionary[key] / sum(deaths) * 360)
        turtle.forward(min(turtle.window_height(), turtle.window_width()) / 2 - 25)
        turtle.write(key)
        turtle.pencolor('red')
        turtle.up()
        turtle.home()
        turtle.down()
        turtle.seth(angle)
        turtle.forward(min(turtle.window_height(), turtle.window_width()) / 2 - 50)