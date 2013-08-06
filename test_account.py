import unittest
from lib.Account import *

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account()
    
    def test_can_create_account(self):
        self.assertIsNotNone(self.account)

    def test_can_create_account_with_value(self):
        new_account = Account(50)
        self.assertEqual(50, new_account.money)

    def test_when_create_total_money_is_zero(self):
        self.assertEqual(0, self.account.money)

    def test_when_get_one_money_is_minus_one(self):
        self.account.get(1)
        self.assertEqual(-1, self.account.money)

    def test_when_have_five_and_get_one_money_is_four(self):
        self.account.add(5)
        self.account.get(1)
        self.assertEqual(4, self.account.money)

    def test_when_add_one_money_is_one(self):
        self.account.add(1)
        self.assertEqual(1, self.account.money)

    def test_when_add_five_money_is_five(self):
        self.account.add(5)
        self.assertEqual(5, self.account.money)

    def test_when_add_five_and_seven_money_is_twelve(self):
        self.account.add(5)
        self.account.add(7)
        self.assertEqual(12, self.account.money)

    def test_if_i_try_use_more_than_my_limit_i_cant_get(self):
        self.account.add(100)
        self.account.get(200)
        self.assertEqual(100, self.account.money)

    def test_if_i_try_use_until_my_limit_i_can_get(self):
        self.account.add(100)
        self.account.get(150)
        self.assertEqual(-50, self.account.money)

if __name__ == '__main__':
    unittest.main()