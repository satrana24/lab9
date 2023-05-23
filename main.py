from PIL import Image, ImageFilter
from pathlib import Path
import csv
import os


def first3():
    correct_directory = r'C:\Users\sofia\Desktop\lab9'  # путь к исходным изображениям
    new_directory = r'C:\Users\sofia\Desktop\lab9\\new_images'  # путь для сохранения изображений с фильтром

    if not os.path.exists(new_directory):  # проверка на существование одноимённой папки
        os.makedirs(new_directory)  # создание папки для сохранения обработанных изображений
    for filename in os.listdir(correct_directory):  # проходимся по всем файлам в исходной папке
        if not filename.endswith('.jpg') and not filename.endswith('.png'):
            continue
        with Image.open(os.path.join(correct_directory, filename)) as image:
            new_image = image.filter(ImageFilter.CONTOUR)
        new_filename = os.path.join(new_directory, filename)  # сохраняем изображение с фильтром в новую папку
        new_image.save(new_filename)


def first_and_second():
    current_directory = ''
    filenames = Path(current_directory).glob('*')  # поиск файлов по шаблону, в нашем случае по любому имени?
    Path('new directory').mkdir(parents=True, exist_ok=True)  # создаёт новую папку

    for file in filenames:
        if file.suffix in ['.jpg', '.png']:  # проверка на расширение файла
            with Image.open(file) as img:  # открываем картинку
                img.load()  # загружаем
                new_img = img.filter(ImageFilter.CONTOUR)  # накладываем фильтр
                new_img.save(Path('new directory/new_image_' + str(file)))  # сохраняем


def third():
    file = open('food.csv', 'r')  # открываем файл, чтобы его прочитать?
    data = list(csv.reader(file, delimiter=','))  # разделяет информацию запятой
    print('Нужно купить: ')
    for i in data:
        print(f'{i[0]} - {i[1]} шт. за {i[2]} руб.')
    print(f'Итоговая сумма: {sum([int(i[1]) * int(i[2]) for i in data])} руб.')
    file.close()  # закрываем файл
