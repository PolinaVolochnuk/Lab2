"""
Задача №1.
Напишіть програму, яка просить користувача ввести вік людини (ціле число).
Програма повинна вивести повідомлення про те, чи є особа немовлям, дитиною,
підлітком або дорослим за такими правилами: якщо людині 1 рік або менше, він
або вона є немовлям, якщо особа старше 1 року, але молодше 13 років, вона є
дитиною, якщо особа не молодше 13 років, але молодше 20 років, вона є підлітком
і якщо особа віком старше 20 років, вона є дорослою.

Автор: Волочнюк Поліна Іванівна
"""

age = int(input("Введіть вік людини: "))

if age <= 1:
  print("Немовля")
elif 1 < age < 13:
  print("Дитина")
elif 13 <= age < 20:  
  print("Підліток")
else:
  print("Дорослий")
