import unittest

from main import CaloriesCalculator, CashCalculator, r1, r2, r3, r4, r5


class ITiP_TEST_FOR_LAB_3(unittest.TestCase):

    def test_CaloriesCalculator(self):
        calories_calculator = CaloriesCalculator(1000)
        calories_calculator.add_record(r4)
        calories_calculator.add_record(r5)
        self.assertEqual(calories_calculator.get_calories_remained(),
                         'Ты можешь потребить ещё не более 300 калорий')

    def test_CashCalculator(self):
        cash_calculator = CashCalculator(1000)
        cash_calculator.add_record(r1)
        cash_calculator.add_record(r2)
        cash_calculator.add_record(r3)
        self.assertEqual(cash_calculator.get_today_cash_remained('rub'), 'Денег нет, но вы держитесь! Твой долг - 1345.0 руб')

    def test_extra(self):
        calories_calculator = CaloriesCalculator(1000)
        calories_calculator.add_record(r4)
        self.assertEqual(calories_calculator.get_today_limit_balance(), 800)

if __name__ == '__main__':
    unittest.main()