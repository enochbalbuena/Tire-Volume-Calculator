'''This program calculates the volume of a tire from three arguments: width, aspect ratio, and diameter, and stores the in a text file.'''

import math
import datetime

def calculate_tire_volume(width, aspect_ratio, diameter):
    # Calculate the tire volume using the formula provided
    volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
    return volume

def main():
    # Get user input for tire dimensions with specific prompt formatting
    print("Enter the width of the tire in mm (ex 205): ", end="")
    width = int(input())
    print("Enter the aspect ratio of the tire (ex 60): ", end="")
    aspect_ratio = int(input())
    print("Enter the diameter of the wheel in inches (ex 15): ", end="")
    diameter = int(input())

    # Calculate the volume of the tire
    volume = calculate_tire_volume(width, aspect_ratio, diameter)

    # Output the calculated volume with a specific format
    print(f"The approximate volume is {volume:.2f} liters.")

    # Ask if the user wants to buy the tires
    buy_tires = input("Do you want to buy tires with the dimensions you entered? (yes/no): ").strip().lower()
    
    # Get the current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Prepare data to write
    data_to_write = f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}"

    if buy_tires == "yes":
        # If user wants to buy, ask for phone number
        phone_number = input("Please enter your phone number: ")
        data_to_write += f", {phone_number}\n"
    else:
        data_to_write += "\n"

    # Open a text file for appending and write the data
    with open("volumes.txt", "a") as file:
        file.write(data_to_write)

if __name__ == "__main__":
    main()