###############################12
def average(line):
  """Вычисляет среднее значение чисел из строки.

  Args:
    line: Строка, содержащая целые числа, разделенные пробелами.

  Returns:
    Среднее значение чисел в строке или None, если строка пуста.
  """
  numbers = [int(x) for x in line.split()]
  return sum(numbers) / len(numbers) if numbers else None

# Основной цикл программы
while True:
  line = input()
  result = average(line)
  if result is not None:
    print(round(result, 2))  # Округляем до 2 знаков после запятой
  else:
    break
###############################13
def process_string(line):
  """Обрабатывает строку, преобразуя регистр и удаляя специальные символы.

  Args:
    line: Входная строка.

  Returns:
    Обработанная строка.
  """
  if line.startswith('!'):
    line = line.upper()  # Верхний регистр, если начинается с '!'
  else:
    line = line.lower()  # Нижний регистр в противном случае
  
  # Удаляем символы '!', '@', '#', '%'
  for char in '!@#%':
    line = line.replace(char, '') 
  
  return line

# Основной цикл программы
while True:
  line = input()
  if not line:
    break
  processed_line = process_string(line)
  print(processed_line)
###############################14
start, end, step = map(int, input().split())
result = map(lambda x: x**2 if x % 2 else -x, range(start, end, step))  # Убрали + 1
for num in result:
  print(num)
###############################15
fib_cache = {}  # Глобальный словарь для кэширования результатов

def fibonacci(n):
  """Вычисляет n-е число Фибоначчи с помощью рекурсии и кэширования."""
  if n in fib_cache:
    return fib_cache[n]  # Если результат уже вычислен, возвращаем его из кэша
  if n == 1 or n == 2:
    result = 1
  else:
    result = fibonacci(n-1) + fibonacci(n-2)
  fib_cache[n] = result  # Сохраняем результат в кэше
  return result

# Считываем порядковый номер n
n = int(input())

# Выводим n-е число Фибоначчи
print(fibonacci(n))
###############################16
def map(func, seq):
  """Генератор, применяющий функцию к каждому элементу последовательности."""
  for item in seq:
    yield func(item)  # Применяем функцию и возвращаем результат с помощью yield

# Считываем функцию и последовательность из входных данных
func_in, seq_in = eval(input()), eval(input())

# Применяем функцию к последовательности и выводим результаты
for x in map(func_in, seq_in):
  print(x)
###############################17
def filter(func, seq):
  """Генератор, фильтрующий последовательность по условию функции."""
  for item in seq:
    if func(item):
      yield item

# Считываем функцию и последовательность из входных данных
func_in, seq_in = eval(input()), eval(input())

# Применяем фильтр и выводим результаты
for x in filter(func_in, seq_in):
  print(x)
###############################18
def cache_deco(func):
  cache = {}

  def wrapper(*args):
    if args not in cache:
      cache[args] = func(*args)
    return cache[args]

  return wrapper

code = []
while data := input():
  code.append(data)
code = "\n".join(code)
exec(code)
###############################19
def repeat_deco(n=1):
  """Декоратор для повторения вызова функции n раз."""
  def decorator(func):
    def wrapper(*args, **kwargs):
      result = None
      for _ in range(n):
        result = func(*args, **kwargs)
      return result
    return wrapper
  return decorator

code = []
while data := input():
  code.append(data)
code = "\n".join(code)
exec(code)
###############################20
a = int(input())

def f():
  global a  # Указываем, что мы хотим изменить глобальную переменную 'a'
  a += 10  # Увеличиваем значение 'a' на 10
  
f()

print(a)
###############################21
def g():
  b = int(input())
  def h():
    nonlocal b  # Указываем, что мы хотим изменить 'b' из объемлющей области
    b += 10
  h()
  print(b)
g()
###############################22
from typing import List, Dict

def make_most_common_keys(d: Dict[int, int]) -> List[int]:
  return sorted(d, key=d.get, reverse=True)

code = []
while data := input():
  code.append(data)
code = "\n".join(code)
exec(code)
###############################23
from typing import List

def get_indexes(nums1: List[int], nums2: List[int]) -> List[int]:
  return [i for i, (a, b) in enumerate(zip(nums1, nums2)) if a < b]

code = []
while data := input():
  code.append(data)
code = "\n".join(code)
exec(code)
###############################24 в конце модуля 2
def cache_deco(func):
  """Декоратор для кэширования результатов функции."""
  cache = {}

  def wrapper(*args):
    if args not in cache:
      cache[args] = func(*args)
    return cache[args]

  return wrapper

def solution(func_map, func_filter, data):
  """Генератор, фильтрующий, преобразующий и возвращающий каждый второй элемент."""
  filtered_data = filter(func_filter, data)
  mapped_data = map(func_map, filtered_data)
  for i, item in enumerate(mapped_data):
    if i % 2 == 0:  # Возвращаем каждый второй элемент (начиная с первого)
      yield item

code = []
while data := input():
  code.append(data)
code = "\n".join(code)
exec(code)
###############################24
class Counter:

    def __init__(self, initial_count):
        self.count = initial_count  # Инициализируем счётчик с начальным значением

    def increment(self):
        self.count += 1  # Увеличиваем счётчик на 1

    def get(self):
        return self.count  # Возвращаем текущее значение счётчика


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
###############################25
class Circle:
    pi = 3.14

    def calculate_area(self, radius):
        return self.pi * radius**2  # Вычисляем площадь круга и возвращаем результат

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
###############################26
class Person:
    def __init__(self, age):
        self._age = age  # Инициализируем внутренний атрибут _age

    @property
    def age(self):
        return self._age  # Возвращаем значение _age при доступе к age

    @age.setter
    def age(self, value):
        if value < 0:
            self._age = 0  # Если возраст меньше 0, устанавливаем его в 0
        else:
            self._age = value  # Иначе устанавливаем переданное значение

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
###############################27
class Pendulum:
    g = 10
    pi = 3.14

    @classmethod
    def calculate_period(cls, length):
        return 2 * cls.pi * (length / cls.g)**0.5  # Вычисляем период и возвращаем результат

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
###############################28
class Circle:
    _pi = 3.14

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def pi(self):
        return self._pi

    def calculate_area(self):
        return self._pi * self._radius ** 2


class SemiCircle(Circle):
    def calculate_area(self):
        return super().calculate_area() / 2  # Делим площадь круга на 2

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
###############################32 в конце 3
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        return self.a * self.b


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)  # Передаем одинаковую сторону и в a, и в b через родительский конструктор


class CalculatePerimeterMixin(Rectangle):
    def calculate_perimeter(self):
        return 2 * (self.a + self.b)


class SquareWithMixin(CalculatePerimeterMixin, Square):
    def __eq__(self, other):
        return self.a == other.a

    def __gt__(self, other):
        return self.calculate_area() > other.calculate_area()

    def __add__(self, other):
        return self.calculate_area() + other.calculate_area()

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
###############################33
import os

text = input()

def write_and_read(text):
    file_path = os.path.join(os.path.abspath('/tmp'), 'my_file')
    with open(file_path, 'w') as f:
        f.write(text)
    with open(file_path, 'r') as f:
        return f.read()

print(write_and_read(text))
###############################34 1 тест ток
numerator, denominator = int(input()), int(input())

def changed_div(numerator, denominator):
    try:
        return denominator / numerator
    except ZeroDivisionError:
        return denominator

print(changed_div(numerator, denominator))
###############################36
from itertools import zip_longest
from typing import List, Tuple


def fill_missing_values(values_list_1: List[int], values_list_2: List[int]) -> List[Tuple[int, int]]:
    return list(zip_longest(values_list_1, values_list_2, fillvalue=1))

###############################37
code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

import datetime

days, seconds = int(input()), int(input())

def shift_time(days: int, seconds: int):
    shifted_datetime = datetime.datetime(2023, 1, 1, 12, 30, 0) + datetime.timedelta(days=days) + datetime.timedelta(seconds=seconds)
    return (shifted_datetime.day, shifted_datetime.second)

print(shift_time(days, seconds))
###############################38
import datetime

string_datetime = input()


def parse_time(s):
    dt = datetime.datetime.strptime(s, "%Y %m %d %H %M %S")
    return dt + datetime.timedelta(days=1)

print((parse_time(string_datetime)).day)
###############################39
import datetime
from collections import Counter
from typing import List


def most_common_months(dates: List[str], n) -> List[int]:
    months = []
    for date in dates:
        months.append(int(date[5:7]))
    return [month for month, count in Counter(months).most_common(n)]


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
###############################40
from collections import deque
from typing import List


def rotate_list(nums: List[int], n: int):
    nums = deque(nums)
    nums.rotate(n)
    return list(nums)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
###############################итоговый проект
from typing import List


class Twitter:

    def __init__(self):
        self.tweets = {}  # {user_id: [tweet_id1, tweet_id2, ...]}
        self.followers = {}  # {follower_id: [followee_id1, followee_id2, ...]}
        self.time = 0  # счетчик времени

    def post_tweet(self, user_id, tweet_id):
        self.tweets.setdefault(user_id, []).append((self.time, tweet_id))
        self.time += 1

    def get_news_feed(self, user_id) -> List[int]:
        news_feed = []
        for followee_id in self.followers.get(user_id, []):
            for tweet_time, tweet_id in self.tweets.get(followee_id, []):
                news_feed.append((tweet_time, tweet_id))
        news_feed.sort(reverse=True)
        return [tweet_id for _, tweet_id in news_feed[:10]]

    def follow(self, follower_id, followee_id):
        self.followers.setdefault(follower_id, []).append(followee_id)

    def unfollow(self, follower_id, followee_id):
        if followee_id in self.followers.get(follower_id, []):
            self.followers[follower_id].remove(followee_id)

code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
