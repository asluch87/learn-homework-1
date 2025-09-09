"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
 
  while True:
   variable1 = input("Как дела:") 
   print(f"{variable1}") # мне для логов строку можно удалять.
   if variable1 != "Хорошо":
     print("Обрабатываем повторно") # для логов.
     continue
   elif variable1 == "Хорошо": 
    break
  pass
    
  

  


    
if __name__ == "__main__":
    hello_user()
