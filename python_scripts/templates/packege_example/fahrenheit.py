def fahrenheit(T):
	return (9.0/5)*T + 32

temp = [-40, -20, 0, 32, 50, 70, 100]



f_temps = map(fahrenheit, temp)

print f_temps