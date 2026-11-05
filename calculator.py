"""Interactive Calculator & Unit Converter (InternCircle Project 1).

A menu-driven command-line program that does basic arithmetic and unit
conversions, validates all input, and keeps running until the user quits.
"""

import math

# All conversion factors live here, so they can be changed in one place.
CONVERSION_FACTORS = {
    "km_to_miles": 0.621371,
    "kg_to_pounds": 2.20462,
}

MAIN_MENU = """
===== Calculator & Unit Converter =====
1) Add
2) Subtract
3) Multiply
4) Divide
5) Convert units
6) Quit"""

CONVERT_MENU = """
--- Unit Conversions ---
1) Kilometres to miles
2) Miles to kilometres
3) Celsius to Fahrenheit
4) Fahrenheit to Celsius
5) Kilograms to pounds
6) Pounds to kilograms
7) Back to main menu"""


# ---------- Input helpers ----------

def read_number(prompt):
    """Keep asking until the user types a valid, finite number."""
    while True:
        text = input(prompt).strip()
        if text == "":
            print("Input cannot be empty. Please enter a number, e.g. 12 or 3.5.")
            continue
        try:
            value = float(text)
        except ValueError:
            print("That is not a number. Please enter one, e.g. 12 or 3.5.")
            continue
        if not math.isfinite(value):
            print("Please enter a normal number (not 'nan' or 'inf').")
            continue
        return value


def read_choice(prompt, valid_options):
    """Keep asking until the user types one of the valid menu options."""
    while True:
        choice = input(prompt).strip()
        if choice in valid_options:
            return choice
        print(f"Invalid choice. Please pick one of: {', '.join(valid_options)}.")


# ---------- Arithmetic functions ----------

def add(a, b):
    """Return a + b."""
    return a + b


def subtract(a, b):
    """Return a - b."""
    return a - b


def multiply(a, b):
    """Return a * b."""
    return a * b


def divide(a, b):
    """Return a / b, or a clear message if b is zero."""
    if b == 0:
        return "Error: cannot divide by zero."
    return a / b


# ---------- Conversion functions ----------

def km_to_miles(km):
    """Convert kilometres to miles."""
    return km * CONVERSION_FACTORS["km_to_miles"]


def miles_to_km(miles):
    """Convert miles to kilometres."""
    return miles / CONVERSION_FACTORS["km_to_miles"]


def celsius_to_fahrenheit(celsius):
    """Convert degrees Celsius to degrees Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert degrees Fahrenheit to degrees Celsius."""
    return (fahrenheit - 32) * 5 / 9


def kg_to_pounds(kg):
    """Convert kilograms to pounds."""
    return kg * CONVERSION_FACTORS["kg_to_pounds"]


def pounds_to_kg(pounds):
    """Convert pounds to kilograms."""
    return pounds / CONVERSION_FACTORS["kg_to_pounds"]


# Maps each conversion menu option to (prompt, function, unit label).
CONVERSIONS = {
    "1": ("Kilometres: ", km_to_miles, "miles"),
    "2": ("Miles: ", miles_to_km, "km"),
    "3": ("Celsius: ", celsius_to_fahrenheit, "°F"),
    "4": ("Fahrenheit: ", fahrenheit_to_celsius, "°C"),
    "5": ("Kilograms: ", kg_to_pounds, "pounds"),
    "6": ("Pounds: ", pounds_to_kg, "kg"),
}

OPERATIONS = {"1": add, "2": subtract, "3": multiply, "4": divide}


# ---------- Menu handling ----------

def format_result(value):
    """Return numbers rounded to 4 decimals; pass messages through as-is."""
    if isinstance(value, str):
        return value
    return round(value, 4)


def run_arithmetic(choice):
    """Ask for two numbers and apply the chosen operation."""
    a = read_number("First number: ")
    b = read_number("Second number: ")
    result = OPERATIONS[choice](a, b)
    print("Result:", format_result(result))


def run_conversion_menu():
    """Show the conversion submenu and perform one conversion."""
    print(CONVERT_MENU)
    choice = read_choice("Choose a conversion: ", ["1", "2", "3", "4", "5", "6", "7"])
    if choice == "7":
        return
    prompt, function, unit = CONVERSIONS[choice]
    value = read_number(prompt)
    print("Result:", format_result(function(value)), unit)


def main():
    """Run the main menu loop until the user chooses Quit."""
    while True:
        print(MAIN_MENU)
        choice = read_choice("Choose an option (1-6): ", ["1", "2", "3", "4", "5", "6"])
        if choice == "6":
            print("Goodbye!")
            break
        if choice == "5":
            run_conversion_menu()
        else:
            run_arithmetic(choice)


if __name__ == "__main__":
    main()
