"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
  def compare_strings(str1, str2):
  
    if type(str1) != str or type(str2) != str:
        return 0
    
   
    if str1 == str2:
        return 1
 
    if len(str1) > len(str2):
        return 2
    
    if str2 == "learn":
        return 3
    
  print(compare_strings(123, "привет"))     # 0 (не строки)
  print(compare_strings("hello", "hello"))  # 1 (одинаковые)
  print(compare_strings("python", "java"))  # 2 (первая длиннее)
  print(compare_strings("hi", "learn"))     # 3 (вторая = "learn")
  print(compare_strings("learn", "java"))   # None (ни одно условие)
if __name__ == "__main__":
    main()
