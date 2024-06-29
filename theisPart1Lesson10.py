"""
I certify, that this computer program submitted by me is all of my own work.
Signed: Dylan Theis 6/7/2024

Author: Dylan Theis
Date: Summer 2024
Class: CSC330
Project: Writing a DSL
Description: Creating specification tests for the DSL, using test_add, test_get_quantity, and test_remove
"""

# Main class
class Inventory:
  # Constructor for class
  def __init__(self):
    # items dictionary will hold each item and their quantity
      self.items = {}

  # add to the items, can either be new or adds it to dictionary
  def add_item(self, name, quantity):
      if name in self.items:
          self.items[name] += quantity
      else:
          self.items[name] = quantity

  # returns quantity if none return 0
  def get_quantity(self, name):
      return self.items.get(name, 0)

  # remove item from dictionary, if 0 or less remove from dictionary
  def remove_item(self, name, quantity):
      if name in self.items:
          self.items[name] -= quantity
          if self.items[name] <= 0:
              del self.items[name]

# Testing each function
if __name__ == "__main__":
  inventory = Inventory()

  # Testing add
  inventory.add_item("apple", 10)
  print("After adding 10 apples: ", inventory.items)

  # Testing quantity
  print("Quantity of apples: ", inventory.get_quantity("apple"))

  # Testing remove
  inventory.remove_item("apple", 5)
  print("After removing 5 apples: ", inventory.items)
