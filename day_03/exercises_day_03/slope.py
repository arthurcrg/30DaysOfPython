m = int(input("Enter the slope of the line: "))
b = (int(input("Enter the independent variable: ")))

x_intercept = -b / m
y_intercept = b

print("The slope is:", m)
print("The x-intercept is:", x_intercept)
print("The y-intercept is:", y_intercept)

x1 = int(input("Enter the x-coordinate of the first point: "))
y1 = int(input("Enter the y-coordinate of the first point: "))
x2 = int(input("Enter the x-coordinate of the second point: "))
y2 = int(input("Enter the y-coordinate of the second point: "))

slope = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("The slope between the two points is:", slope)
print("The Euclidean distance between the two points is:", euclidean_distance)
