from unittest import TestCase
from account import Account

class TestAccount(TestCase):

    def test_init(self):
        test_account = Account("187529", 7898, 500, "john", "public")
        self.assertEqual(test_account.account_num, "187529")
        self.assertEqual(test_account.pin, 7898)
        self.assertEqual(test_account.balance, 500)
        self.assertEqual(test_account.first_name, "john")
        self.assertEqual(test_account.last_name, "public")

    def test_account_in_data(self):
        true_test = Account.account_in_data("513287")
        false_test = Account.account_in_data("123123")
        self.assertEqual(true_test, True)
        self.assertEqual(false_test, False)

    def test_validate(self):
        real_account = Account("513287", 5378)
        fake_account = Account("123123", 7291)
        self.assertTrue(real_account.validate())
        self.assertFalse(fake_account.validate())

    def test_load(self):
        test_account = Account("513287", 5378)
        test_account.load()
        self.assertEqual(test_account.first_name, "john")
        self.assertEqual(test_account.last_name, "doe")
        self.assertEqual(test_account.balance, 756004.46)