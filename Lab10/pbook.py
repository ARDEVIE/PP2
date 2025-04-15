import psycopg2


def create_table_if_not_exists():
    """Создаёт таблицу phonebook, если она ещё не существует"""
    sql = """
    CREATE TABLE IF NOT EXISTS phonebook (
        user_id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        phone_number VARCHAR(20) NOT NULL
    );
    """
    try:
        with psycopg2.connect(
            dbname='pbook',
            user='postgres',
            password='12345',
            host='localhost'
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Ошибка при создании таблицы:", error)


def collecting_info():
    """ Извлекать данные из таблицы phonebook """
    try:
        with psycopg2.connect(
            dbname='pbook',
            user='postgres',
            password='12345',
            host='localhost'
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT user_id, name, phone_number FROM phonebook ORDER BY user_id")
                rows = cur.fetchall()

                print("Количество контактов:", cur.rowcount)
                for row in rows:
                    print(row)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def update_info(user_id, name, phone_number):
    """ Обновление контакта """
    update_row_count = 0

    sql = """UPDATE phonebook
             SET name = %s, phone_number = %s
             WHERE user_id = %s"""
    
    try:
        with psycopg2.connect(
            dbname='pbook',
            user='postgres',
            password='12345',
            host='localhost'
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, phone_number, user_id))
                update_row_count = cur.rowcount
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return update_row_count


def delete_info(user_id):
    """ Удаление контакта """
    rows_deleted = 0
    sql = 'DELETE FROM phonebook WHERE user_id = %s'
    
    try:
        with psycopg2.connect(
            dbname='pbook',
            user='postgres',
            password='12345',
            host='localhost'
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (user_id,))
                rows_deleted = cur.rowcount
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return rows_deleted


def insert_contact(name, phone_number):
    """ Вставка нового контакта в таблицу phonebook """
    sql = """INSERT INTO phonebook(name, phone_number)
             VALUES(%s, %s) RETURNING user_id;"""

    user_id = None
    
    try:
        with psycopg2.connect(
            dbname='pbook',
            user='postgres',
            password='12345',
            host='localhost'
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, phone_number))
                row = cur.fetchone()
                if row:
                    user_id = row[0]
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return user_id


def search_contacts():
    """ Поиск контактов по фильтрам """
    print("\nФильтры:")
    print("1 - По имени")
    print("2 - По номеру телефона")
    print("3 - По ID")
    choice = input("Выберите фильтр: ")

    try:
        with psycopg2.connect(
            dbname='pbook',
            user='postgres',
            password='12345',
            host='localhost'
        ) as conn:
            with conn.cursor() as cur:
                if choice == "1":
                    name = input("Введите имя: ")
                    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", (name,))
                elif choice == "2":
                    phone = input("Введите номер телефона: ")
                    cur.execute("SELECT * FROM phonebook WHERE phone_number = %s", (phone,))
                elif choice == "3":
                    id_min = input("Введите ID: ")
                    cur.execute("SELECT * FROM phonebook WHERE user_id = %s", (id_min,))
                else:
                    print("Некорректный выбор.")
                    return

                rows = cur.fetchall()
                if rows:
                    for row in rows:
                        print(row)
                else:
                    print("Ничего не найдено.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


if __name__ == '__main__':
    create_table_if_not_exists()  # создаёт таблицу при запуске, если её нет

    operation = input("Выберите:\n1 - записать контакт\n2 - обновить контакт\n3 - показать все контакты\n4 - показать контакт (фильтр)\n5 - удалить контакт\n")

    if operation == "1":
        name = input("Введите имя нового контакта: ")
        phone_number = input("Введите номер телефона: ")
        user_id = insert_contact(name, phone_number)
        if user_id is not None:
            print("Контакт успешно добавлен. ID:", user_id)
        else:
            print("Ошибка при добавлении контакта.")
    
    elif operation == "2":
        user_id = int(input("Введите ID контакта для обновления: "))
        name = input("Введите новое имя: ")
        phone_number = input("Введите новый номер телефона: ")
        updt = update_info(user_id, name, phone_number)
        if updt:
            print("Контакт успешно обновлён.")
        else:
            print("Контакт не найден или ошибка.")
    
    elif operation == "3":
        collecting_info()
    
    elif operation == "4":
        search_contacts()
    
    elif operation == "5":
        user_id = int(input("Введите ID контакта для удаления: "))
        dlt = delete_info(user_id)
        if dlt:
            print("Контакт успешно удалён.")
        else:
            print("Контакт не найден или ошибка.")
