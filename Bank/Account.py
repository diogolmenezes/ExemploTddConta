class Account:

    def __init__(self, money = 0, limit = 50):
        self.money = money
        self.limit = limit

    def add(self, value):
        self.money += value

    def get(self, value):
        i_have_money = self.money - value >= -self.limit
        if i_have_money:
            self.money -= value