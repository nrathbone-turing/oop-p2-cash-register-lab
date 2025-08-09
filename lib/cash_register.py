#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0, total = 0, items = None, previous_transactions = None):
    self.discount = discount
    self.total = total
    self.items = items if items is not None else []
    self.previous_transactions = previous_transactions if previous_transactions is not None else []

  # discount property
  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, value):
    if isinstance(value, int) and 0 <= value <= 100:
      self._discount = value
    else:
        print("Not valid discount")

  def add_item(self, item, price, quantity = 1):
    # update the running total
    self.total += price * quantity
    
    #add items to the array
    self.items.extend([item] * quantity)

    # record the transaction as an object to append into previous_transactions array
    self.previous_transactions.append({
        "item": item,
        "price": price,
        "quantity": quantity,
        "subtotal": price * quantity
    })