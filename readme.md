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
- Первые 2 колонки должны быть sync_id и дата создания (_created_at_) с данными форматами
- Далее колонки таблице в Postgresql должны совпадать с CSV/XSL/XSLX файлом
  (_**пример 1ый столбец в file.xls - `company`, 
значит 3 по счёту столбец в БД таблице - `company varchar(255)` и т.д.**_)

>CREATE TABLE {_**table_name**_}(
    sync_id UUID,    
    created_at timestamp,
    ...
);

