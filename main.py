# main.py

from calculator import (
    calculate_rectangle_area,
    calculate_rectangle_perimeter,
    calculate_square_area,
    calculate_square_perimeter,
    calculate_triangle_area,
    calculate_triangle_perimeter,
)
from utils import get_float
from exceptions import NegativeValueError

def main():
    print("Welcome to the Multi-Shape Calculator!")
    print("Choose a shape to calculate:")
    print("1. Rectangle")
    print("2. Square")
    print("3. Triangle")

    choice = input("Enter your choice (1-3): ")

    try:
        if choice == '1':
            length = get_float("Enter the length: ")
            width = get_float("Enter the width: ")
            if length < 0 or width < 0:
                raise NegativeValueError("Length and width must be positive.")
            area = calculate_rectangle_area(length, width)
            perimeter = calculate_rectangle_perimeter(length, width)
            print(f"Rectangle Area: {area}")
            print(f"Rectangle Perimeter: {perimeter}")

        elif choice == '2':
            side = get_float("Enter the side length: ")
            if side < 0:
                raise NegativeValueError("Side length must be positive.")
            area = calculate_square_area(side)
            perimeter = calculate_square_perimeter(side)
            print(f"Square Area: {area}")
            print(f"Square Perimeter: {perimeter}")

        elif choice == '3':
            base = get_float("Enter the base: ")
            height = get_float("Enter the height: ")
            side1 = get_float("Enter side 1: ")
            side2 = get_float("Enter side 2: ")
            side3 = get_float("Enter side 3: ")
            if base < 0 or height < 0 or side1 < 0 or side2 < 0 or side3 < 0:
                raise NegativeValueError("All sides must be positive.")
            area = calculate_triangle_area(base, height)
            perimeter = calculate_triangle_perimeter(side1, side2, side3)
            print(f"Triangle Area: {area}")
            print(f"Triangle Perimeter: {perimeter}")

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    except NegativeValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
