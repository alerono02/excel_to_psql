import time

import psycopg2


def check_columns(df, table_name: str):
    conn = psycopg2.connect(
        database="test",
        user='postgres',
        password='1234',
        host='localhost',
        port='5432'
    )

    conn.autocommit = True
    cursor = conn.cursor()

    # sql = f'''SELECT * FROM {table_name}'''
    sql = f'''
    SELECT column_name FROM information_schema.columns 
    WHERE table_name = '{table_name}' 
    ORDER BY ordinal_position;'''
    # изменить на получение названия column
    start_time = time.time()
    cursor.execute(sql)
    column_names_db = [row[0] for row in cursor]
    if len(column_names_db) == len(df.columns):
        for i in range(len(column_names_db)):
            if column_names_db[i] != df.columns[i]:
                raise NameError(f"Указанно неверное название столбца: rename {df.columns[i]} to {column_names_db[i]}")
        print("Successfully checked column names!")
    elif len(column_names_db) < len(df.columns):
        raise ValueError("В EXCEL таблицы указанны лишние столбцы")
    else:
        raise ValueError("В EXCEL таблицы указанны не все столбцы")
    conn.commit()
    conn.close()
    print("--- %s seconds ---" % (time.time() - start_time))
