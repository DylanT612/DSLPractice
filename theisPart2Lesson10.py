"""
I certify, that this computer program submitted by me is all of my own work.
Signed: Dylan Theis 6/7/2024

Author: Dylan Theis
Date: Summer 2024
Class: CSC330
Project: Writing a DSL
Description: Creating specification tests for the DSL, using test_add, test_get_quantity, and test_remove
"""

from inventory import Inventory

# DSL Interface
class InventoryDSL:
  # Constructor initializes Inventory instance
  def __init__(self):
      self.inventory = Inventory()

  # add calls add_item using inventory
  def add(self, name, quantity):
      self.inventory.add_item(name, quantity)

  # quantity_of calls get_quantity using inventory
  def quantity_of(self, name):
      return self.inventory.get_quantity(name)

  # remove calls remove_item using inventory
  def remove(self, name, quantity):
      self.inventory.remove_item(name, quantity)

# Test if add works then checks that quantity is the same that was added
def test_add_item():
  dsl = InventoryDSL()
  dsl.add('widget', 10)
  assert dsl.quantity_of('widget') == 10, "Test failed: Expected quantity 10"

# Test if get_quantity works then checks that quantity is the same that was added
def test_get_quantity():
  dsl = InventoryDSL()
  dsl.add('gadget', 5)
  assert dsl.quantity_of('gadget') == 5, "Test failed: Expected quantity 5"

# Test if remove_items works then checks that quantity is the same that was removed
def test_remove_item():
  dsl = InventoryDSL()
  dsl.add('widget', 10)
  dsl.remove('widget', 5)
  assert dsl.quantity_of('widget') == 5, "Test failed: Expected quantity 5"
  dsl.remove('widget', 5)
  assert dsl.quantity_of('widget') == 0, "Test failed: Expected quantity 0"

# Run each DSL test then print pass or print the error
def run_tests():
  try:
      test_add_item()
      print("test_add_item passed")
  except AssertionError as e:
      print(e)

  try:
      test_get_quantity()
      print("test_get_quantity passed")
  except AssertionError as e:
      print(e)

  try:
      test_remove_item()
      print("test_remove_item passed")
  except AssertionError as e:
      print(e)

if __name__ == "__main__":
  run_tests()
