"""
Задача №2.
Задані дві клітини шахової дошки. Якщо вони пофарбовані в один колір, то введіть
слово Так, а якщо в різних кольорах - Ні. Програма отримує на вхід чотири числа
від 1 до 8 шкіри, що спочатку дає номер стовпця і номер рядка першої клітинки,
потім для другої клітинки.

Автор: Волочнюк Поліна Іванівна
"""

a = int(input("Введіть номер рядка 1 клітинки (1-8): "))
b = int(input("Введіть номер стовпця 1 клітинки (1-8): "))
c = int(input("Введіть номер рядка 2 клітинки (1-8): "))
d = int(input("Введіть номер стовпця 2 клітинки (1-8): "))

if (a + b) % 2 == (c + d) % 2:
    print("Yes")
else:
    print("No")