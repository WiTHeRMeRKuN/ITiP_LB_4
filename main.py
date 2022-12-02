import datetime as dt


class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.today = dt.date.today()
        self.week_ago = self.today - dt.timedelta(7)

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        day_stats = []
        for record in self.records:
            if record.date == self.today:
                day_stats.append(record.amount)
        return sum(day_stats)

    def get_week_stats(self):
        week_stats = []
        for record in self.records:
            if self.week_ago <= record.date <= self.today:
                week_stats.append(record.amount)
        return sum(week_stats)

    def get_today_limit_balance(self):
        limit_balance = self.limit - self.get_today_stats()
        return limit_balance


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        calories_remained = self.get_today_limit_balance()
        if calories_remained > 0:
            message = (f'Ты можешь потребить '
                       f'ещё не более {calories_remained} калорий')
        else:
            message = 'Хватит есть!'
        return message


class CashCalculator(Calculator):
    USD_RATE = 62.0
    EURO_RATE = 64.0
    RUB_RATE = 1

    def get_today_cash_remained(self, currency):
        currencies = {'usd': ('USD', CashCalculator.USD_RATE),
                      'eur': ('Euro', CashCalculator.EURO_RATE),
                      'rub': ('руб', CashCalculator.RUB_RATE)}
        cash_remained = self.get_today_limit_balance()
        if cash_remained == 0:
            return 'Денег нет, но вы держитесь'
        if currency not in currencies:
            return f'Валюта {currency} не учитывается'
        name, rate = currencies[currency]
        cash_remained = round(cash_remained / rate, 2)
        if cash_remained > 0:
            message = f'Ты можешь потратить ещё {cash_remained} {name}'
        else:
            cash_remained = abs(cash_remained)
            message = (f'Денег нет, но вы держитесь! Твой долг - {cash_remained} 'f'{name}')
        return message


# для CashCalculator
r1 = Record(amount=160, comment='Чай чёрный', date='01.12.2022')
r2 = Record(amount=345,
            comment='Обед в столовой')
r3 = Record(amount=2000, comment='Поход в ночной клуб', date='02.12.2022')

# для CaloriesCalculator
r4 = Record(amount=200, comment='Хлеб', )
r5 = Record(amount=500, comment='Обед', date='02.12.2022')

# для CashCalculator
cash_calculator = CashCalculator(1000)
cash_calculator.add_record(r1)
cash_calculator.add_record(r2)
cash_calculator.add_record(r3)

# для CaloriesCalculator
calories_calculator = CaloriesCalculator(1000)
calories_calculator.add_record(r4)
calories_calculator.add_record(r5)
print()