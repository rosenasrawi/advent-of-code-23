from datetime import date

today = date.today()
day = today.strftime('%d')

inpfile = 'input-' + day + '.txt'
i = open('input/' + inpfile, 'x')

exmfile = 'example-' + day + '.txt'
i = open('input/example/' + exmfile, 'x')

solfile = 'day-' + day + '.py'
f = open('solutions/' + solfile, 'x')
f.write('from _getinput import *')