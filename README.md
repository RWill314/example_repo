# Inventory Management System

A simple Python program for managing a shoe inventory from the command line.
It lets you read and update inventory data, search for shoes, and calculate values.

---

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Example](#example)
5. [Credits](#credits)
6. [License](#license)

---

## Features
- Read inventory from `inventory.txt`
- Add new shoes with unique codes
- View all shoes in a tabular format
- Restock the shoe with the lowest quantity
- Calculate total value of each shoe item (cost × quantity)
- Search for shoes by product code
- Identify the shoe with the highest quantity ("for sale")

---

## Installation

Clone the repository and install dependencies:

```powershell
git clone https://github.com/RWill314/example_repo.git
cd example_repo
pip install tabulate
```

> **Note:** Requires Python 3.x.

---

## Usage

1. **Prepare the data file (optional)**
   If `inventory.txt` doesn’t exist, the program will create it.
   Example format if you want to start with data:

   ```powershell
   Country,Code,Product,Cost,Quantity
   USA,SKU123,Nike Air,120,50
   UK,SKU456,Adidas Run,95,30
   ```

2. **Run the program**

   ```powershell
   python inventory.py
   ```

3. **Follow the interactive menu**
   - `1` View all shoes (displayed in a table)
   - `2` Add a new shoe (validates unique code and numeric fields)
   - `3` Restock the lowest-quantity shoe (updates `inventory.txt`)
   - `4` View total value for each item (cost × quantity)
   - `5` Search by shoe code (case-insensitive)
   - `6` Show the shoe with the highest quantity
   - `7` Exit

4. **Where data is stored**
   All changes are saved to `inventory.txt` in the same directory as `inventory.py`.

---

## Example

```powershell
Here are the options:
1: View all shoes
2: Add a new shoe
3: Check shoe with lowest quantity and re-stock
4: View total value for each item
5: Search for a shoe using the shoe code
6: Find shoe with highest quantity
7: Exit

Enter the option number you would like to perform: 1
```

---

## Credits

Created by **Rhys Williams** for the **AI Bootcamp**.

---

