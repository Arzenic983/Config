import sqlite3
from Main import *


def main_request(part_type_for_combobox):
    database = sqlite3.connect('eee.sqlite')
    cursor = database.cursor()
    return cursor.execute("""SELECT name FROM parts_main WHERE type=:eac""", {'eac': part_type_for_combobox}).fetchall()
    # вот эта вот функция должна быть универсальной, т.е. при привязке к типу железки должен он падать аргументом.
    # И вставляться а SQL запрос типа {part_type}


def get_type(name):
    database = sqlite3.connect('eee.sqlite')
    cursor = database.cursor()
    a = cursor.execute("""SELECT type FROM parts_main WHERE name=:nname""", {"nname": str(name)}).fetchall()
    return str(a)[3:-4]


def get_id(name):
    database = sqlite3.connect('eee.sqlite')
    cursor = database.cursor()
    b = cursor.execute("""SELECT ID FROM parts_main WHERE name=:nname""", {"nname": name}).fetchall()
    return str(b)[2:-3]


def get_info(name, typo, ID):
    database = sqlite3.connect('eee.sqlite')
    cursor = database.cursor()
    req_1 = cursor.execute(f"""SELECT price, manufacturer FROM parts_main WHERE name=:nname""",
                           {"nname": name}).fetchall()
    req_2 = cursor.execute(f"""SELECT * FROM {typo} WHERE ID =:idd """, {'idd': ID}).fetchall()
    req = req_1 + req_2
    result = list()
    for i in req:
        for j in i:
            result.append(j)
    return result

# крч сверни этот апулаз в одну функцию. Или не сворачивай, больше строк навернём на этом деле


# пожалуйста напиши, я займусь выводом и подключением объектов классов к интерфейсу. Хорошо, сделаю это сам.
# но товарища для следующего проекта ты НЕ НАЙДЁШЬ!
