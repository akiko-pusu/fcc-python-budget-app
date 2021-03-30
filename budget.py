class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, budget, type=''):
        ledger = {"amount": budget, "description": type}
        self.ledger.append(ledger)

    def withdraw(self, price, items=''):

        fundable = self.check_funds(price)
        if (fundable):
            ledger = {"amount": price * -1, "description": items}
            self.ledger.append(ledger)
            return True

        return False

    def get_balance(self):
        budget = self.ledger[0]["amount"]
        expense = self.ledger[1]["amount"]
        return budget + expense

    def transfer(self, amount, other_category):
        fundable = self.check_funds(amount)
        if (fundable):
            description = "Transfer to " + other_category.category
            ledger = {"amount": amount * -1, "description": description}
            self.ledger.append(ledger)
            other_category.deposit(amount, "Transfer from " + self.category)
            return True

        return False

    def check_funds(self, amount):
        budget = self.ledger[0]["amount"]

        return budget >= amount

    def __str__(self):
      deposit = self.ledger[0]
      transfar = self.ledger[2]
      rest = deposit["amount"] + transfar["amount"]

      result = (
        "*************"
        + self.category
        + "*************\n"
        + "deposit                 "
        + '{:.2f}'.format(deposit["amount"])
        + "\n"
        + deposit["description"]
        + ' '
        + str(deposit["amount"])
        + "\n"
        + "Total: "
        + str(rest)
      )
      return result

def create_spend_chart(categories):
    print('create_spend_chart called!')
