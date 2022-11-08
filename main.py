def esBiciesto():
  year = int(input('Ingrese un año para saber si es bisiesto: '))
  if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
    print('el año: ' + str(year) + ' es biciesto')
  else: 
    print('el año: ' + str(year) + ' no es biciesto')
  
  esBiciesto() 
    
esBiciesto()