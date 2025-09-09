"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцЧто делаешьию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {}

def ask_user(answers_dict):
   
   answers_dict = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"}
   while True:
         questions_and_answers = input("Чем занят:")
         if questions_and_answers in answers_dict:
             Answer = answers_dict[questions_and_answers]
             print(f"{Answer}")
             break
         else:
             print("такого запроса нет")  
       
       

      
    
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
