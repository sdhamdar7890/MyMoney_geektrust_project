from constant import Constants


class Account:
    """
    This class creates an object to track the investment of a investor it store data of equity, debt, gold.
    
    """
    def __init__(self, equity, debt, gold):

        total = equity + debt + gold
        self.amount = {"allocated": Constants(equity, debt, gold), "initial_percentage": Constants(equity / total,
                                                                                                   debt / total,
                                                                                                   gold / total)}
        self.last_month = "allocated"
        self.rebalance_month = ""

    def sip(self, equity, debt, gold):
        self.amount["sip"] = Constants(equity, debt, gold)

    def change(self, equity, debt, gold, month):
        if month[:7] == 'january':
            self.amount[month] = self.amount[self.last_month].change(equity / 100, debt / 100, gold / 100)
        else:
            sip = self.amount["sip"]
            spam = self.amount[self.last_month].change(sip.equity(), sip.debt(), sip.gold())
            self.amount[month] = spam.change(equity/100, debt/100, gold/100)
        self.last_month = month
        if month[:4] == "june" or month[:8] == "december":
            self.rebalance(month)

    def rebalance(self, month):
        month_balance = self.amount[month]
        percent = self.amount["initial_percentage"]
        total = sum([month_balance.equity(), month_balance.debt(), month_balance.gold()])
        self.amount[month] = Constants(int(total * percent.equity()), int(total * percent.debt()),
                                       int(total * percent.gold()))
        self.rebalance_month = month

    def balance(self, month):
        if month == "":
            print("CANNOT REBALANCE")
        else:
            month1 = self.amount[month]
            print(month1.equity(), month1.debt(), month1.gold())
