from datetime import datetime

prev_date = datetime.now()  # переменная для предыдущей даты
c = 0  # счетчик кол-ва NOK
result = {}  # переменная для сохранения результата

with open("events.log") as file:
    for line in file:
        if not line.isspace() and line.split()[-1] == 'NOK':  # обрабатываем строку только если она не пустая и содержит 'NOK' в конце
            date_str = ' '.join(line.split()[0:2])  # парсим дату из строки
            date = datetime.strptime(date_str, '[%Y-%m-%d %H:%M:%S]')  # и переводим в класс datetime
            if prev_date.replace(second=0) != date.replace(
                    second=0):  # если предыдущая дата (без секунд) и текущая не совпадают, счетчик побнуляется
                c = 0
            c += 1  # счетчик событий NOK увеличивается на один
            result[date.strftime('%Y-%m-%d %H:%M')] = c  # записываем результат для текущей минуты
            prev_date = date  # текущую дату из строки объявляем предыдущей

for k, v in result.items():  # выводим подсчитанный результат
    print(k, '=', v)
