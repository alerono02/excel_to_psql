***Convert Excel/CSV files to PSQL database***
---

**Предустановка**
- Создать таблицу в PostgreSQL
- Создайте файл `.env` и укажите параметры на основе `.env.example`
- Закинуть импортируемый файл в директорию проекта

**Установка зависимостей командной:**
>pip3 install -r requirements.txt

**Запуск скрипта**
>python3 main.py {_**filename.csv**_} {_**db_table_name**_}`
 
**Экземпляр таблицы в БД**
-----
_Первые 2 столбца должны быть uuid и дата создания с данными форматами_

`CREATE TABLE {_**table_name**_}(
   transaction_id UUID,    
    created_at timestamp,
    ...
);`

