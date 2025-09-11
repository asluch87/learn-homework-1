"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""




price = 100
discount = 95
def discounted(price,discount,max_discount = 20):
    try:
        price = float(price)
    except(ValueError,TypeError):
        return  ('Должно быть числом')   
    try:
       discount = float(discount)
    except(ValueError,TypeError):
       return  ('Должно быть числом')     
    try:
        max_discount = int(max_discount)
    except(ValueError,TypeError):  
         return  ('Должно быть числом')   
## Если сделать проверку ввиде как ниже, то он не отработал.Поэтому сделал блок if-ов
#    try:
        # Приведение типов с обработкой исключений
  #      price = float(price)
   #     discount = float(discount)
    #    max_discount = int(max_discount)
    #except (ValueError, TypeError)



    if max_discount >= 100:
        return ValueError ('Скидка не может быть больше 100')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price*discount/100
    return price_with_discount
 








      
      

if __name__ == "__main__":
    print(discounted(103, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
