class ShiftTable:
    def __init__(self):
        self.table = {}  # Словарь: ключ - номер записи, значение - индекс символа

    def add(self, record_id, shift):
        self.table[record_id] = shift

    def remove(self, record_id):
        if record_id in self.table:
            del self.table[record_id]

    def get(self, record_id):
        return self.table.get(record_id, None)

    def clear(self):
        self.table.clear()