import psycopg2 as ps
from psycopg2 import sql

# TODO: В этом файле прописаны функции, которые вызываются из файла GUI при нажатии на кнопки
#  Эти функции в свою очередь берут запросы с хранимыми функциями из файла sql
#  и отправляют их на сервер
# заменить конкретные параметры user and password на "username", "password", когда всё будет готово
#  "guest_user", "guest_password"


conn = None

def connect_db(username, password):
    global conn
    try:
        conn = ps.connect(
            dbname="game_market_case",
            user="postgres",
            password="11111111",
            host="localhost",
            port="5432"
        )
        print("Connected!")
        return conn
    except ps.OperationalError as e:
        print("Connection error. Check password and username")
        return None
    except Exception as e:
        print(f"Another error: {e}")
        return None

def create_database(dbname, username, password):
    if conn is None:
        print("No connection")
        return
    try:
        with conn.cursor() as cur:
            cur.callproc('createDatabase', [dbname, username, password])
            conn.commit()
            print(f"Database {dbname} created successfully")
    except Exception as e:
        print(f"Error occurred while creating database: {e}")

def create_table(table_name):
    if conn is None:
        print("No connection")
        return
    try:
        with conn.cursor() as cur:
            query = f"call create_table('{table_name}');"
            cur.execute(query)
            conn.commit()
            print(f"Table {table_name} created successfully")
    except Exception as e:
        print(f"Error occurred while creating table: {e}")

def clear_table(table_name):
    if conn is None:
        print("No connection")
        return
    try:
        with conn.cursor() as cur:
            query = f"call clear_table('{table_name}');"
            cur.execute(query)
            conn.commit()
            print(f"Table {table_name} cleared successfully")
    except Exception as e:
        print(f"Error occurred while clearing table: {e}")

def add_data_games(val_1, val_2, val_3):
    if conn is None:
        print("No connection")
        return
    try:
        with conn.cursor() as cur:
            query = f"call add_data_games('{val_1}', '{val_2}', '{val_3}');"
            cur.execute(query)
            conn.commit()
            print(f"Table games is filled with new record successfully")
    except Exception as e:
        print(f"Error occurred while additing in table: {e}")

def which_num_columns(table):
    # таблица - выводимый параметр из choose_table, отправляется запрос
    # выводит количество столбцов таблицы в целочисленном формате
    if table == 'games':
        return 3

def show_table(table_name):
    # выполняет запрос select и выводит в основное текстовое окно графического интерфейса
    if conn is None:
        print("No connection")
        return
    try:
        with conn.cursor() as cur:
            query = f'select * from show_table_{table_name}() as t(id int, name varchar, genre varchar, price int);'
            cur.execute(query)
            res = cur.fetchall()
            conn.commit()
            print(f"Table games is shown")
            return res
    except Exception as e:
        print(f"Error occurred while clearing table: {e}")



# def send_query(text):
#     if conn is None:
#         print("No connection")
#         return
#     try:
#         with conn.cursor() as cur:
#             print(text, type(text))
#             cur.execute(text)
#             res = cur.fetchall()
#             if res:
#                 for row in res:
#                     print(row)
#             else:
#                 print("No data received")
#             conn.commit()
#             print("Query sent successfully")
#     except Exception as e:
#         print("Error occurred!")