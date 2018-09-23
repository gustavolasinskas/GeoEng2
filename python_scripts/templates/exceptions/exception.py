

car = {'make':'Toyota', 'model':'Prius', 'year':2002}

print(car['make'])

try:
    print(car['color'])
except:
    print("No key 'Color'")
finally:
    print("next key ->")

print(car['year'])
