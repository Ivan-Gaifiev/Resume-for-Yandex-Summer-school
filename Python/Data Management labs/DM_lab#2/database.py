import os
import ShiftTable as s
import numpy as np

class Database:

    def __init__(self, filename):
        self.filename = filename
        self.shift_table = s.ShiftTable()

    def create(self):
        with open(self.filename, 'w') as f:
            f.write('')  # Создание пустого файла

    def delete(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def clear(self):
        self.create()
        self.shift_table.clear()

    def add_record(self, record_id, name, price, num_purchases):
        if self.shift_table.get(record_id) is not None:
            raise AttributeError("Record with this ID already exists.")

        with open(self.filename, 'a') as f:
            shift = f.tell()
            record = f"{record_id},{name},{price},{num_purchases}\n"
            f.write(record)

        self.shift_table.add(record_id, shift)

    def search(self, field, value):
        """Поиск записей по указанному полю и значению."""
        if field == "all":
            return self.get_all_records()

        field_idx = {"id": 0, "name": 1, "price": 2, "num_purchases": 3}.get(field)
        if field_idx is None:
            raise ValueError("Invalid field for search.")

        with open(self.filename, 'r') as f:
            return [line.strip().split(',') for line in f if line.strip().split(',')[field_idx] == value]

    def delete_records(self, field, value):
        """
        Удалить запись(и) по указанному полю и значению.
        Если поле - "id", удаляется соответствующая запись с обновлением shift_table.
        Для других полей удаляются все записи, соответствующие значению.
        """
        temp_filename = self.filename + '.tmp'
        field_idx = {"id": 0, "name": 1, "price": 2, "num_purchases": 3}[field]

        deleted_ids = []  # Для хранения ID удалённых записей

        with open(self.filename, 'r') as infile, open(temp_filename, 'w') as outfile:
            for line in infile:
                fields = line.strip().split(',')
                if (field == "id" and int(fields[field_idx]) == int(value)) or \
                        (field == "price" and float(fields[field_idx]) == float(value)) or \
                        (field == "num_purchases" and int(fields[field_idx]) == int(value)):
                    deleted_ids.append(int(fields[0]))
                elif fields[field_idx] == value:
                    deleted_ids.append(int(fields[0]))
                else:
                    outfile.write(line)

        os.replace(temp_filename, self.filename)
        if not deleted_ids:
            raise ValueError
        # Удалить записи из shift_table, если они присутствуют
        for record_id in deleted_ids:
            self.shift_table.remove(record_id)

    def edit_record(self, record_id, name, price, num_purchases):
        """
        Редактировать запись: перезаписать, если ID существует.
        Удаляет существующую запись по ID и добавляет новую с тем же ID.
        """
        # Удаляем старую запись по ID
        self.delete_records("id", record_id)
        # Добавляем новую запись с обновлёнными данными
        self.add_record(record_id, name, price, num_purchases)

    def update(self):
        """
        Обновить содержмое таблицы смещений в зависимости от
        текущего содержимого базы данных.
        """
        with open(self.filename, 'r') as f:
            shift = 0
            for line in f:
                ind = np.uint64(line.strip().split(',')[0])
                self.shift_table.add(ind, shift)
                shift += len(line)

    def get_all_records(self):
        with open(self.filename, 'r') as f:
            return [line.strip().split(',') for line in f]


