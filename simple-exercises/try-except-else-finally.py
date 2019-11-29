message="What's the height of your wall?"
message2="What's the width of your wall?"

try:
    height = float(input(message))
    width = float(input(message2))
    area = height * width
    print ("The dimentions of your wall is {}x{} and the area is {}m²".format(height, width, area))
    ink = area / 2
    print("You will need {} liters of ink to paint the wall.".format(ink))
except ValueError as e:
    print('Please enter valid numbers only. {}'.format(e))
else:
    print('ELSE')
    #only execute this code when try doesn't failed
finally:
    print('FINALLY')
    #always execute this code
