"""
This module provides classes and functions for managing a shoe inventory.
It allows reading inventory data from a text file, creating 'Shoe' objects,
searching for shoes by code, and displaying inventory details.
"""

# Imports for use in functions later.
import os
from tabulate import tabulate


class Shoe:
    """
    Represents a shoe item in the inventory.

    Attributes:
        country (str): The country where the shoe is manufactured.
        code (str): The unique product code for the shoe.
        product (str): The product name or model of the shoe.
        cost (int): The cost of the shoe in the store's currency.
        quantity (int): The number of shoes available in stock.

    Methods:
        __str__():
            Returns a formatted string representation of the shoe.
    """

    def __init__(self, country, code, product, cost, quantity):
        """
        Initialize a new Shoe instance.

        Args:
            country (str): Country of origin.
            code (str): Unique product code.
            product (str): Product name.
            cost (int): Price per shoe.
            quantity (int): Available quantity in stock.
        """
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        """
        Return the cost of the shoe.

        Returns:
            int: Cost of the shoe.
        """
        return self.cost

    def get_quantity(self):
        """
        Return the quantity of shoes in stock.

        Returns:
            int: Quantity available.
        """
        return self.quantity

    def __str__(self):
        """
        Return a formatted string representation of the shoe.

        Returns:
            str: Descriptive summary of the shoe object.
        """
        return (
            "-----------------------------------------------------\n"
            f"Country:   {self.country}\n"
            f"Code:      {self.code}\n"
            f"Product:   {self.product}\n"
            f"Cost:      {self.cost}\n"
            f"Quantity:  {self.quantity}\n"
            "-----------------------------------------------------\n"
            )


# Global list to store all Shoe objects
shoe_list = []


def read_shoes_data():
    """
    Read shoe data from the 'inventory.txt' file.

    For each valid line, create a Shoe object and add it to the shoe_list.
    Handles missing files and data format errors gracefully.
    """

    try:
        with open("inventory.txt", "r", encoding="utf-8") as f:

            next(f)  # This skips the header line.

            for line_num, line in enumerate(f, start=2):
                parts = line.strip().split(",")
                # Checks for 5 parts and prints a message if not.
                if len(parts) != 5:
                    print(
                        f"Skipped malformed line {line_num}:"
                        f" {line.strip()}"
                    )
                    # Runs remainder of code despite malformed line.
                    continue

                # Stores each line into corresponding variables.
                country, code, product, cost, quantity = parts

                # If there is a value error it will print a message.
                try:
                    shoe_temp = Shoe(
                        country, code, product,
                        int(cost), int(quantity)
                    )
                    shoe_list.append(shoe_temp)
                except ValueError:
                    print(
                        f"Invalid number format in line "
                        f"{line_num}: {line.strip()}"
                    )
                    continue

    except FileNotFoundError:
        print("Error: 'inventory.txt' file was not found.")


def capture_shoes():
    """
    Capture new shoe data from user input.

    Validates inputs, appends new entry to inventory.txt,
    and refreshes the global shoe_list.
    """

    country = input("\nPlease input the country: ").strip()

    # Checks that the user has entered a unique code.
    while True:
        code = input("\nPlease input the unique shoe code: ").strip()
        if any(item.code == code for item in shoe_list):
            print("This is not a unique code, please try again.")
            continue
        break

    product = input("\nPlease input the product name: ").strip()

    # Checks cost is an integer (all other costs were integers).
    while True:
        cost = input("\nPlease input the cost: ").strip()
        if cost.isdigit():
            cost = int(cost)
            break
        else:
            print("The cost must be an integer value. Try again.")

    # Checks quantity is an integer.
    while True:
        quantity = input("\nPlease input the quantity: ").strip()
        if quantity.isdigit():
            quantity = int(quantity)
            break
        else:
            print("The quantity must be an integer value. Try again.")

    # Appends new shoe to file, if doesn't exist adds header first.
    if os.path.exists("inventory.txt"):
        with open("inventory.txt", "a", encoding="utf-8") as f:
            f.write(f'{country},{code},{product},{cost},{quantity}\n')
    else:
        with open("inventory.txt", "a", encoding="utf-8") as f:
            f.write("Country,Code,Product,Cost,Quantity\n")
            f.write(f'{country},{code},{product},{cost},{quantity}\n')

    # Clears shoe_list prior to re-importing shoe data.
    shoe_list.clear()
    read_shoes_data()


def view_all():
    """
    Display all shoes in the inventory in tabular format.

    Outputs data from the shoe_list using the tabulate module.
    """
    # Creates a 2D list of shoe details.
    table = [
        [s.country, s.code, s.product, s.cost, s.quantity]
        for s in shoe_list
    ]

    # Prints in a tabulated form.
    print(tabulate(table, headers=["Country", "Code",
                                   "Product", "Cost", "Quantity"]))


def re_stock():
    """
    Restock the shoe with the lowest quantity.

    Prompts the user for a quantity to add, updates the shoe's quantity,
    and saves changes back to 'inventory.txt'.
    """
    # Identifies the shoe with the lowest quantity.
    lowest_quantity_shoe = min(shoe_list, key=lambda s: s.quantity)
    print("Shoe with lowest quantity:")
    # Prints shoe details.
    print(lowest_quantity_shoe)

    # User inputs how much to re-stock by, verifies value inputted.
    while True:
        restock_number = input(
            "How much would you like to restock these by? "
                        ).strip()
        if restock_number.isdigit():
            # Is an integer so now saves it as such.
            restock_number = int(restock_number)
            break
        else:
            print("The cost must be an integer value. Try again.")

    # Increases quantity.
    lowest_quantity_shoe.quantity += restock_number

    # Clears the txt file and replaces with updated data.
    with open("inventory.txt", "w", encoding="utf-8") as f:
        # Adds header first.
        f.write("Country,Code,Product,Cost,Quantity\n")
        for item in shoe_list:
            f.write(
                f"{item.country},{item.code},{item.product},"
                f"{item.cost},{item.quantity}\n"
            )

    print(f'The new quantity is now {lowest_quantity_shoe.quantity}.')


def value_per_item():
    """
    Calculate and display the total value for each shoe item.

    Total value is computed as: cost × quantity.
    """
    for item in shoe_list:
        total_value = item.quantity * item.cost
        print(f'The total value for shoe code {item.code} is {total_value}')


def search_shoe():
    """
    Search for a shoe by its code.

    Prompts the user for a shoe code and displays the matching shoe if found.

    Returns:
        Shoe | None: The matching Shoe object, or None if not found.
    """
    search_code = input("Enter the shoe code you want to search: ").strip()

    for item in shoe_list:
        if search_code.lower() == item.code.lower():
            # Once found returns item.
            return item
    # If nothing found, prints a message.
    print("No shoe with the code exists.")


def highest_qty():
    """
    Identify and display the shoe with the highest quantity in stock.

    This shoe is considered the one marked "for sale".
    """
    # Identifies the shoe with the highest quantity.
    highest_quantity_shoe = max(shoe_list, key=lambda s: s.quantity)

    print("Shoe with highest quantity for sale:")
    # Prints shoe details.
    print(highest_quantity_shoe)


# Imports data from txt file.
read_shoes_data()

# Displays the options.
while True:
    print("\nHere are the options:")

    opts_list = [
        "1: View all shoes",
        "2: Add a new shoe",
        "3: Check shoe with lowest quantity and re-stock",
        "4: View total value for each item",
        "5: Search for a shoe using the shoe code",
        "6: Find shoe with highest quantity",
        "7: Exit"
    ]

    for opt in opts_list:
        print(opt)

    # Asks user for option number.
    while True:

        input_opt = input("\nEnter the option number you "
                          "would like to perform: ")

        # Checks it is numerical and between 1 and 7.
        if input_opt.isdigit():
            if 1 <= int(input_opt) <= 7:
                input_opt = int(input_opt)
                break
            else:
                print("You have entered an incorrect value.")
        else:
            print("You have entered an incorrect value.")

    # Calls relevent function.
    if input_opt == 1:
        view_all()
    elif input_opt == 2:
        capture_shoes()
    elif input_opt == 3:
        re_stock()
    elif input_opt == 4:
        value_per_item()
    elif input_opt == 5:
        shoe_found = search_shoe()
        if shoe_found:
            print(shoe_found)
    elif input_opt == 6:
        highest_qty()
    elif input_opt == 7:
        # Ends the program.
        break
