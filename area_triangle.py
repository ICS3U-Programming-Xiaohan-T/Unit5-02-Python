#!/usr/bin/env python3
# Created by: Xiaohan
# Created on: May 5, 2025
# This program calculates the area of a triangle


# This function calculates the area of a triangle
# Call the function
def cal_area(height, base):
    # The formula used to calculate the area of a triangle
    area = (base * height) / 2
    # Display the area of the triangle
    print("The area of the triangle is {} cm².".format(area))


# This function is the main function
def main():
    # Casting the base and height from into float
    base_str = input("Enter the base of the triangle (cm): ")
    height_str = input("Enter the height of the triangle (cm): ")
    try:
        # Casing the base and height from into float
        base = float(base_str)
        height = float(height_str)
        # Check if the base and height are positive numbers
        # If they are, call the function cal_area
        if base > 0 and height > 0:
            cal_area(base, height)
        # If they are not, display an error message
        else:
            print("Invalid input. Please enter a positive number.")
    # If the input is not a number, display an error message.
    except Exception:
        # Display an error message
        print("Invalid input.")


if __name__ == "__main__":
    main()
