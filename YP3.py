print(f"Квадраты чисел от 1 до 10: {[x ** 2 for x in range(1,11)]}")

print(f"Чётные числа от 1 до 20: {[x for x in range(1,20) if x % 2 == 0]}")

print(f"Отфильтрованные слова: {[word.lower() for word in ['key', 'Andrey', 'apple', 'slovo', 'car'] if len(word) > 3]}")

class Countdown:
    def __init__(self, n):
        self.n = n
        self.current = n  # Текущее значение для отсчета
    
    def __iter__(self):   #Возвращаем объект как итератор
        return self
    
    def __next__(self): #возвращаем следующее значение
        if self.current < 1:
            raise StopIteration 
        value = self.current
        self.current -= 1
        return value


print("Countdown от 10:")
for x in Countdown(10):
    print(x, end=" ")
print()


def fibonacci(n): #генератор фибоначи
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Пример использования
print("Первые 10 чисел Фибоначчи:")
for num in fibonacci(10):
    print(num, end=" ")
print()


from decimal import Decimal, ROUND_HALF_UP #финансовый калькулятор

def deposit_calculator():
    # Ввод данных
    initial_amount = Decimal(input("Введите начальную сумму вклада (руб): ")) # P
    interest_rate = Decimal(input("Введите годовую процентную ставку (%): "))
    years = Decimal(input("Введите срок вклада (лет): "))
    
    # Расчет по формуле ежемесячной капитализации
    monthly_rate = interest_rate / Decimal('12') / Decimal('100') #r/12
    months = years * 12 #12*t
    
    # S = P × (1 + r/12)^(12×t)
    final_amount = initial_amount * (1 + monthly_rate) ** months
    final_amount = final_amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    # Расчет прибыли
    profit = final_amount - initial_amount
    
    # Вывод результатов
    print(f"\nРезультаты расчета вклада:")
    print(f"Начальная сумма: {initial_amount} руб.")
    print(f"Итоговая сумма: {final_amount} руб.")
    print(f"Общая прибыль: {profit} руб.")

# Запуск калькулятора
deposit_calculator()


from fractions import Fraction #Рациональные дроби

# Создание дробей
frac1 = Fraction(2, 7)
frac2 = Fraction(1, 86)

print(f"Дробь 1: {frac1}")
print(f"Дробь 2: {frac2}")

# Выполнение операций
addition = frac1 + frac2
subtraction = frac1 - frac2
multiplication = frac1 * frac2
division = frac1 / frac2

print(f"\nРезультаты операций:")
print(f"Сложение: {addition}")
print(f"Вычитание: {subtraction}")
print(f"Умножение: {multiplication}")
print(f"Деление: {division}")


from datetime import datetime # Текущая дата и время
now = datetime.now()

print("Текущая дата и время:", now)
print("Только текущая дата:", now.date())
print("Только текущее время:", now.time())


from datetime import datetime, date #разница дат                        
def calculate_birthday_info():
    # Ввод дня рождения
    birth_year = int(input("Введите год рождения: "))
    birth_month = int(input("Введите месяц рождения: "))
    birth_day = int(input("Введите день рождения: "))
    
    birth_date = date(birth_year, birth_month, birth_day)
    today = date.today()
    
    # Сколько дней прошло с момента рождения
    days_passed = (today - birth_date).days
    
    # Следующий день рождения
    next_birthday = date(today.year, birth_month, birth_day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_month, birth_day)
    
    days_to_next_birthday = (next_birthday - today).days
    
    print(f"\nДень рождения: {birth_date}")
    print(f"Дней прошло с рождения: {days_passed}")
    print(f"Дней до следующего дня рождения: {days_to_next_birthday}")

# Запуск расчета
calculate_birthday_info()



from datetime import datetime

def format_datetime_russian(dt):
    # Русские названия месяцев
    months = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля",
        5: "мая", 6: "июня", 7: "июля", 8: "августа",
        9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
    }
    
    day = dt.day
    month = months[dt.month]
    year = dt.year
    time = dt.strftime("%H:%M")
    
    return f"Сегодня {day} {month} {year} года, время: {time}"

# Пример использования
current_time = datetime.now()
formatted_string = format_datetime_russian(current_time)
print(formatted_string)