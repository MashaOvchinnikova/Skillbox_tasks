shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500],
        ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
part_name = input('Название детали: ')
count = 0
total_sum = 0

for part in shop:
    if part[0] == part_name:
        count += 1
        total_sum += part[1]

if count != 0:
    print(f'Кол-во деталей — {count}')
    print(f'Общая стоимость — {total_sum}')
else:
    print('Такой детали нет в магазине')
