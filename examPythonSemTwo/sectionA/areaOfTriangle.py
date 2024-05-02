# A program to calculate the area of a triangle 

def calculate_triangle_area(base, height): # creating a function 
    area = 0.5 * base * height
    return area

def main():
    base = 2
    height = 3
    area = calculate_triangle_area(base, height)
    print(f"The area of the triangle with base {base} and height {height} is: {area}")

if __name__ == "__main__": 
    main()
