# Simple Product Inventory Management System

This is a straightforward, console-based Python project designed for managing product inventory.

## Features

* **Product Definition:** Defines products using a unique ID, name, category, price, and quantity.
* **Persistent Storage:** Automatically loads and saves inventory data to a CSV file named **`products.csv`** using the standard `csv` library.
* **Inventory Operations:** Includes core functionality to add, view, and remove products.
* **Console Interface:** Provides a simple, interactive command-line menu for ease of use.

## Project Structure

The project is organized into the following main files:

* **`product.py`**: Contains the `Product` class definition.
* **`inventory.py`**: Contains the `Inventory` class, which handles the collection of products, business logic, and CSV file interaction.
* **`main.py`**: The entry point of the application, running the main menu loop and handling user input.
* **`products.csv`**: The file used for persistent data storage (it will be created automatically upon first save).

## Getting Started

### Prerequisites

This project requires **Python 3.x**. No external libraries are needed beyond the Python standard library.

### Installation and Execution

1.  **Clone the repository (or download the files):**
    ```bash
    git clone [Your Repository URL]
    cd [project-folder-name]
    ```

2.  **Run the application:**
    Execute the main file to start the inventory management system:
    ```bash
    python main.py
    ```

### Usage

Upon execution, you will be presented with the main menu:

=== INVENTORY MENU ===

Add product

List product

Remove product

Exit Choose option:


1.  **Add product:** Prompts for ID, Name, Category, Price, and Quantity for a new item.
2.  **List product:** Displays all items currently in the inventory.
3.  **Remove product:** Asks for the ID of the product to be removed.
4.  **Exit:** Closes the application.

All changes made (adding or removing products) are automatically saved to the `products.csv` file.

## Class Overview

### `Product` (in `product.py`)

Represents a single stock keeping unit (SKU) or item.

| Attribute | Description | Type |
| :--- | :--- | :--- |
| `id` | Unique identifier | `str` |
| `name` | Product name | `str` |
| `category` | Product category | `str` |
| `price` | Unit price | `float` |
| `quantity` | Stock quantity | `int` |

### `Inventory` (in `inventory.py`)

Manages the collection of `Product` objects and handles file input/output.

| Method | Description |
| :--- | :--- |
| `__init__` | Initializes the inventory and loads existing data from CSV. |
| `add_product(product)` | Adds a new product to the list and saves changes to CSV. |
| `list_products()` | Prints the entire inventory list to the console. |
| `find_product(id)` | Searches for and returns a `Product` object by its ID, or `None`. |
| `remove_product(id)` | Removes a product by ID and saves changes to CSV. |
| `save_to_csv()` | Persists the current inventory state to `products.csv`. |
| `load_from_csv()` | Reads and loads product data from `products.csv`. |

## What this project demonstrates
- Object-Oriented Programming (classes, encapsulation)
- File persistence using CSV
- Separation of concerns (data model, business logic, UI)
- Basic error handling and input validation

## Tech Stack
- Python 3
- Standard Library (`csv`)
