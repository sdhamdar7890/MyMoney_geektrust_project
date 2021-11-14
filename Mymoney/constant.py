class Constants:

    def __init__(self, equity, debt, gold):
        self.value = {"equity": equity, "debt": debt, "gold": gold}

    def __str__(self):
        return f'{self.value.get("equity")}, {self.value.get("debt")}, {self.value.get("gold")}'

    def change(self, equity, debt, gold):
        if equity <= 1:
            return Constants(int(self.equity() * (1 + equity)), int(self.debt() * (1 + debt)),
                             int(self.gold() * (1 + gold)))
        else:
            return Constants(int(self.equity() + equity), int(self.debt() + debt), int(self.gold() + gold))

    def equity(self):
        return self.value.get("equity")

    def debt(self):
        return self.value.get("debt")

    def gold(self):
        return self.value.get("gold")

