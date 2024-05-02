# a program to create maps and adjust coordinates

import math

def calculate_distance(x1, x2, y1, y2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance

def main():
    x1 = float(input("Enter the value of X1: "))

    x2 = float(input("Enter the value of X2: "))

    y1 = float(input("Enter the value of Y1: "))
    
    y2 = float(input("Enter the value of Y2: "))

    distance = calculate_distance(x1, x2, y1, y2)
    print("The distance d is:", distance)

if __name__ == "__main__":
    main()
