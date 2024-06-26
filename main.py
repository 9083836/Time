

# import datetime
# def week_number(date):
#     # Из строки в объект datetime
#     date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
#     # номер недели
#     week_number = date.isocalendar()[1]
#     return week_number

# date_str = "2015-06-16"
# num = week_number(date_str)
# print(f"Номер недели - {num}")







# from datetime import datetime, timedelta
# def first_monday(year, week):

#     first_day_of_year = datetime(year, 1, 1)#первый день года

#     days = (7 - first_day_of_year.weekday() % 7)

#     first_week_monday = first_day_of_year + timedelta(days)
    
#     target_monday = first_week_monday + timedelta(weeks=week-1)
#     return target_monday.strftime('%a %d %B %H:%M:%S %Y')


# year, week = map(int, input("Введите год и номер недели через запятую: ").split(','))
# monday = first_monday(year, week)
# print(monday)






# from datetime import datetime, timedelta
# def all_sundays(year):
#     first_date = datetime(year, 1, 1)
#     first_date += timedelta(days=(6 - first_date.weekday()))
#     sundays = []
    
#     # все воскресенья в году
#     while first_date.year == year:
#         sundays.append(first_date.strftime("%a %d %b %Y"))
#         first_date += timedelta(weeks=1)
#     return sundays


# year = int(input("Введите год: "))
# sundays = all_sundays(year)

# for sunday in sundays:
#     print(sunday)




# import datetime
# from dateutil.relativedelta import relativedelta

# def add_years(date, years):
#     date = datetime.datetime.strptime(date, '%Y,%m,%d')
#     new_date = date + relativedelta(years=years)
#     return new_date.date()


# date = str(input("Введите год, месяц и число: "))
# years_to_add = int(input("Введите число: "))
# new_date = add_years(date, years_to_add)
# print(f"Новая дата после добавления {years_to_add} лет к {date} - это {new_date}")







# import datetime

# local_time = datetime.datetime.now()
# print(f"Местное время: {local_time}")

# utc_time = datetime.datetime.utcnow()
# print(f"Время по Гринвичу (UTC): {utc_time}")




# import datetime

# date1 = datetime.datetime.now() 
# date2 = datetime.datetime(2030, 12, 29) 
# difference = date2 - date1  
# print('Разница в днях: ', difference.days)
# print('Разница в годах: ', difference.days // 365)




# from datetime import datetime

# def format_timedelta(delta):
#     delta = delta
#     days = delta.days
#     seconds = delta.seconds
#     hours = seconds // 3600
#     minutes = (seconds % 3600) // 60
#     seconds = seconds % 60
#     return days, hours, minutes, seconds

# def main():

#     date_str1 = input("Введите первую дату (ГГГГ-ММ-ДД ЧЧ:ММ:СС): ")
#     date_str2 = input("Введите вторую дату (ГГГГ-ММ-ДД ЧЧ:ММ:СС): ")
    
#     date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
#     date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")
    
#     delta = abs(date2 - date1)
#     days, hours, minutes, seconds = format_timedelta(delta)
#     return (f"Разность: {days} дней, {hours} часов, {minutes} минут, {seconds} секунд")


# a  = main()
# print(a)









# def remove_unacceptable_words(input_file_path, unacceptable_words_file_path, output_file_path):
#     # Чтение неприемлемых слов
#     with open(unacceptable_words_file_path, 'r') as file:
#         unacceptable_words = {line.strip().lower() for line in file}
    
#     # Чтение исходного текста
#     with open(input_file_path, 'r') as file:
#         original_text = file.read()
    
#     # Удаление неприемлемых слов
#     cleaned_words = [
#         word for word in original_text.split()
#         if word.lower().strip('.,!?:;"\'') not in unacceptable_words
#     ]
    
#     cleaned_text = ' '.join(cleaned_words)
    
#     # Запись очищенного текста в новый файл
#     with open(output_file_path, 'w') as file:
#         file.write(cleaned_text)

#     return (f"Очищенный текст сохранен в файл {output_file_path}")

# def main():
#     # Пути к файлам
#     input_file_path = 'input.txt'
#     unacceptable_words_file_path = 'unacceptable_words.txt'
#     output_file_path = 'output.txt'
    
#     # Удаление неприемлемых слов из файла
#     return remove_unacceptable_words(input_file_path, unacceptable_words_file_path, output_file_path)


# a = main()
# print(a)








# from transliterate import translit

# def read_text(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         return file.read()

# def write_text(file_path, text):
#     with open(file_path, 'w', encoding='utf-8') as file:
#         file.write(text)

# def main():
#     input_file = 'text_input1.txt'
#     output_file = 'text_output1.txt'
    
#     original_text = read_text(input_file)
    
#     print("Выберите направление транслитерации:")
#     print("1. С русского на английский")
#     print("2. С английского на русский")
#     choice = input("Введите номер: ")
    
#     if choice == '1':
#         transliterated_text = translit(original_text, 'ru', reversed=True)
#     elif choice == '2':
#         transliterated_text = translit(original_text, 'ru')
#     else:
#         print("Неверный выбор. Программа завершена.")
#         return
    
#     write_text(output_file, transliterated_text)
    
#     return (f"Текст успешно транслитерирован и сохранен в файл {output_file}")

# r = main()
# print(r)





# def merge_files(input_files, output_file):
#     with open(output_file, 'w', encoding='utf-8') as out_file:
#         for file_name in input_files:
#             with open(file_name, 'r', encoding='utf-8') as in_file:
#                 out_file.write(in_file.read())
#                 out_file.write('\n')  

# def main():
#     input_files = []
    
#     while True:
#         file_name = input("Введите название файла (или 'quit' для завершения): ")
        
#         if file_name.lower() == 'quit':
#             break
        
#         input_files.append(file_name)
    
#     output_file = 'merged_output.txt'
#     merge_files(input_files, output_file)
    
#     return (f"Содержимое файлов объединено в файл {output_file}")

# d = main()
# print








# def read_file(file_name):
#     with open(file_name, 'r') as file:
#         return set(file.read().strip())

# def find_common_characters(files):
#     if not files:
#         return set()
    
#     common_chars = read_file(files[0])
    
#     for file_name in files[1:]:
#         common_chars.intersection_update(read_file(file_name))
    
#     return common_chars

# def main():
#     input_files = []
    
#     while True:
#         file_name = input("Введите название файла (или 'quit' для завершения): ")
        
#         if file_name.lower() == 'quit':
#             break
        
#         input_files.append(file_name)
    
#     if not input_files:
#         return ("Не было введено ни одного файла. Программа завершена.")
    
#     common_chars = find_common_characters(input_files)
    
#     if common_chars:
#         output_file = 'common_characters.txt'
#         with open(output_file, 'w', encoding='utf-8') as file:
#             file.write(''.join(common_chars))
        
#         return (f"Символы, присутствующие в каждом файле, записаны в файл {output_file}")
#     else:
#         return ("Ни один из введенных файлов не содержит символов. Программа завершена.")

# result = main()
# print(result)






# import os
# import shutil

# def create_and_move_files(src_dirs, dest):

#     if not os.path.exists(dest):
#         os.makedirs(dest)

#     for src_dir in src_dirs:
#         if not os.path.exists(src_dir):
#             print(f"Папка {src_dir} не существует")
#             continue

#         for item in os.listdir(src_dir):
#             src_item = os.path.join(src_dir, item)
#             dest_item = os.path.join(dest, item)

#             shutil.move(src_item, dest_item)
#             print(f"{src_item} перемещен в {dest_item}")

# def main():
#     src_dirs = ['video', 'sub']
#     dest = 'watch_me'

#     create_and_move_files(src_dirs, dest)

# result = main()
# print(result)










# import os

# files = os.listdir('.')

# for file_name in files:

#     if file_name.endswith('.jpg'):
#         parts = file_name[:-4].split('_')
#         if len(parts) == 2:
#             new_file_name = f"{parts[1]}_{parts[0]}.jpg"
#             os.rename(file_name, new_file_name)
#             print(f"Файл {file_name} переименован в {new_file_name}")





# import os
# import shutil

# list_file = 'list.tsv'
# dest_dir = 'list'

# if not os.path.exists(dest_dir):
#     os.makedirs(dest_dir)

# with open(list_file, 'r', encoding='utf-8') as file:
#     files_to_move = [line.strip() for line in file]

# for file_name in files_to_move:
#     if os.path.exists(file_name):
#         shutil.move(file_name, os.path.join(dest_dir, file_name))
#         print(f"Файл {file_name} перемещен в папку {dest_dir}")
#     else:
#         print(f"Файл {file_name} не найден")

# print("Перемещение файлов завершено.") #файл Nina_Stoletova.jpg переместил в list







# def last_line(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as file:
#         lines = file.readlines()
    
#     if lines:
#         lines = lines[:-1]  # Удаляем последнюю строку
    
#     with open(output_file, 'w', encoding='utf-8') as file:
#         file.writelines(lines)

# # Задаем имена входного и выходного файлов
# input_file = 'text_fail.txt'
# output_file = 'result_fail.txt'

# last_line(input_file, output_file)
# print(f"Последняя строка удалена из файла {input_file} и результат записан в файл {output_file}")