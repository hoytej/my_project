# Декоратор логирования
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")
        result = func(*args, **kwargs)
        print(f"Функция {func.__name__} вернула {result}")
        return result
    return wrapper

# Декоратор доступа
def require_role(allowed_roles):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get('role') in allowed_roles:
                return func(user, *args, **kwargs)
            else:
                print(f"Доступ запрещён пользователю {user['name']}")
                return None
        return wrapper
    return decorator

# Функции с декоратором логирования
@logger
def add(a, b):
    return a + b

@logger
def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

@logger
def greet(name):
    return f"Привет, {name}!"

# Функции с декоратором доступа
@require_role(['admin'])
def delete_database(user):
    print(f"База данных удалена пользователем {user['name']}")
    return "Успешно удалено"

@require_role(['admin', 'manager'])
def edit_settings(user):
    print(f"Настройки изменены пользователем {user['name']}")
    return "Настройки обновлены"

# Тестирование
if __name__ == "__main__":
    print("=== Тестирование декоратора логирования ===")
    add(5, 3)
    print()
    divide(10, 2)
    print()
    divide(10, 0)
    print()
    greet("Анна")
    
    print("\n=== Тестирование декоратора доступа ===")
    users = [
        {'name': 'Иван', 'role': 'admin'},
        {'name': 'Мария', 'role': 'manager'},
        {'name': 'Петр', 'role': 'user'},
        {'name': 'Анна', 'role': 'guest'}
    ]
    
    for user in users:
        print(f"\nПользователь: {user['name']} (роль: {user['role']})")
        delete_database(user)
        edit_settings(user)