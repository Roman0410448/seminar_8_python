# Задача 38: 
# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

# Показывает информацию в файле

def show_data(filename):
    loading()
    print("\nПП | Имя | Фамилия | Телефон")
    with open(filename, "r", encoding="utf-8") as data:
        print(data.read())
    print("")
    
# Записывает информацию в файл
def export_data(filename):
    with open(filename, "r", encoding="utf-8") as data:
        tel_file = data.read()
    num = len(tel_file.split("\n"))
    with open(filename, "a", encoding="utf-8") as data:
        loading() 
        name = input("Введите Имя: ")
        secondname = input('Введите Фамилию: ')
        phone_number = input("Введите номер телефона: ")
        data.write(f"{num} | {name} |{secondname}| {phone_number}\n")
        loading()
        print(f"Добавлена запись : {num} | {name} |{secondname}| {phone_number}\n")
    
# Изменяет информацию из файла
def edit_data(filename):
    loading()
    print("\nПП | Имя | Фамилия | Телефон")
    with open(filename, "r", encoding='utf-8') as data:
        tel_book = data.read()    
    print(tel_book)
    print("")
    index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
    tel_book_lines = tel_book.split("\n")
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(" | ")
    loading()
   
    name = input("Введите Имя: ")
    secondname = input('Введите Фамилию: ')
    phone = input("Введите номер телефона: ")
    num = elements[0]
    if len(name) == 0:
        name = elements[1]
    if len(secondname) == 0:
        secondname = elements[2]      
    if len(phone) == 0:
        phone = elements[3]
    edited_line = f"{num} | {name} |{secondname} | {phone}"
    tel_book_lines[index_delete_data] = edited_line
    loading()
    print(f"Запись - {edit_tel_book_lines}, изменена на - {edited_line}\n")
    with open(filename, "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))
    
# Удаляет информацию из файла
def delete_data(filename):
    loading()
    print("\nПП | Имя | Фамилия | Телефон")
    with open(filename, "r", encoding="utf-8") as data:
        tel_book = data.read()
        print(tel_book) 
    print("")
    index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
    tel_book_lines = tel_book.split("\n")
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    loading()
    print('______________________\n'
          f'Запись {del_tel_book_lines} успешно удалена')
    print("")
    with open(filename, "w", encoding='utf-8') as data:
        data.write("\n".join(tel_book_lines))
    
def main():
    my_choice = -1
    file_tel = "tel.txt"

    # Создает файл если его нет в папке
    with open(file_tel, "a", encoding="utf-8") as file:
         file.write("")

    while my_choice != 0:
        print("Выберите одно из действий:")
        print("1 - Добавить запись")
        print("2 - Вывести информацию на экран")
        print("3 - Произвести изменение данных")
        print("4 - Произвести удаление данных")
        print("0 - Выход из программы")
        action = int(input("Действие: "))
        if action == 2:
            show_data(file_tel)
        elif action == 1:
            export_data(file_tel)
        elif action == 3:
            edit_data(file_tel)
        elif action == 4:
            delete_data(file_tel)
        else:
            my_choice = 0
    loading()    
    print("До свидания")
def loading():
    import time
    import sys

    animationproc = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
    animation = ["■□□□□□□□□□", "■■□□□□□□□□", "■■■□□□□□□□", "■■■■□□□□□□", "■■■■■□□□□□",
                 "■■■■■■□□□□",
                 "■■■■■■■□□□", "■■■■■■■■□□", "■■■■■■■■■□", "■■■■■■■■■■"]

    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r" + animation[i % len(animation)] + f" {animationproc[i]}")
        sys.stdout.flush()

    print("\n")    

if __name__ == "__main__":
    main()