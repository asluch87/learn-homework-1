"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():

 
 while True:
  try:
    variable1 = input("Как дела:") 
    print(f"{variable1}") # мне для логов строку можно удалять.
    if variable1 != "Хорошо":
     print("Обрабатываем повторно") # для логов.
     continue
    else: 
     print("Хорошо") # для логов.
  except KeyboardInterrupt:  
     print("Пока!") # для логов.
     break
if __name__ == "__main__":
    hello_user()
