from art import logo, vs
from game_data import data
from random import randint
from replit import clear
  
DATA_LEN = len(data)-1

def message(a, b):
  print(f"Compare A: {a['name']}, {a['description']}, {a['country']}")
  print(vs)
  print(f"Compare B: {b['name']}, {b['description']}, {b['country']}")

#Генерация начальных значений на a и b
def choice_generation(a=None, b=None, right_choice=None):
  if not a and not b:
    a = data[randint(0, DATA_LEN)]
    b = data[randint(0, DATA_LEN)]
  else:
    if right_choice == a:
      b = values_check(a, b)
    elif right_choice == b:
      a = b
      b = values_check(a, b)
  return a, b
  
#Проверка значений
def values_check(a, b):
  b = data[randint(0, DATA_LEN)]
  if b == a:
    values_check(a, b)
  return b
  
def compare_choices(a, b, score, choice):
  if a["follower_count"] >= b["follower_count"] and choice == "a":
    clear()
    score += 1
    print(f"You're right! Current score: {score}")
    return score, False, a
  elif a["follower_count"] <= b["follower_count"] and choice == "b":
    clear()
    score += 1
    print(f"You're right! Current score: {score}")
    return score, False, b
  else:
    clear()
    print(logo)
    print(f"You're lose! Current score: {score}")
    return score, True, None

def game():
  is_end = False
  a, b, score = (0,) * 3
  right_choice = None
  while not is_end:
    print(logo)
    #Вывод вариантов для сравнения
    a, b = choice_generation(a, b, right_choice)
    message(a, b)
    #Ввод пользователем а или б
    choice = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
    #Результаты
    score, is_end, right_choice = compare_choices(a, b, score, choice)
    
game()