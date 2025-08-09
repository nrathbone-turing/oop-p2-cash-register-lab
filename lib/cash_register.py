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
  if isinstance(discount, int) and 0 <= discount <= 100:
    self._discount = discount
  else:
      print("Not valid discount")
