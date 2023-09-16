import math

# Accept the radius from the user as input
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = math.pi * (radius ** 2)

# Display the result
print("The area of the circle with radius {0} is {1}".format(radius,area))
