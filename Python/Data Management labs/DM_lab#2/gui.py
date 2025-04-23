import tkinter as tk
from tkinter import ttk, messagebox
import os
import shutil
import numpy as np
from database import Database


def main():
    db = Database('dbGames.txt')

    def refresh_table():
        """Обновить отображение данных в GUI."""
        for row in tree.get_children():
            tree.delete(row)
        for record in db.get_all_records():
            tree.insert("", "end", values=record)

    def create_db():
        """Создать базу данных, если её нет. Если есть, обновить таблицу."""
        if os.path.exists(db.filename):
            refresh_table()
            messagebox.showinfo("Info", "Database already exists. Table refreshed.")
        else:
            db.create()
            messagebox.showinfo("Info", "Database created successfully.")
            refresh_table()

    def delete_db():
        """Удалить базу данных."""
        db.delete()
        refresh_table()
        messagebox.showinfo("Info", "Database deleted successfully.")
        root.quit()

    def search_records():
        """Поиск записей по полю и значению."""
        field = search_field.get()
        value = search_value.get()
        if not field:
            messagebox.showerror("Error", "Please select a field.")
            return

        try:
            if field == "all":
                results = db.get_all_records()
            else:
                results = db.search(field, value)

            if not results:
                messagebox.showinfo("Info", "No matching records found.")
                return

            # Обновляем таблицу для отображения результатов поиска
            for row in tree.get_children():
                tree.delete(row)
            for record in results:
                tree.insert("", "end", values=record)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def add_record():
        """Добавить запись в базу данных."""
        try:
            record_id = np.uint64(entry_id.get())
            name = entry_name.get()
            if name.isdigit():
                raise ValueError
            price = float(entry_price.get())
            num_purchases = np.uint32(entry_num_purchases.get())
            db.add_record(record_id, name, price, num_purchases)
            messagebox.showinfo("Info", "Record added successfully.")
            refresh_table()

        except (ValueError, OverflowError):
            messagebox.showerror("Error", "Wrong type(s) of the entered data!")
        except AttributeError as e:
            messagebox.showerror("Error", str(e))

    def delete_record():
        """Удалить запись из базы данных."""
        try:
            field = delete_field.get()
            value = delete_value.get()
            if not field or not value:
                messagebox.showerror("Error", "Please select a field and enter a value.")
                return
            db.delete_records(field, value)
            messagebox.showinfo("Info", f"Record(s) deleted successfully by {field}.")
            refresh_table()
        except ValueError:
            messagebox.showerror("Error", "Nothing to delete.")

    def edit_record():
        """Редактировать запись в базе данных."""
        try:
            record_id = np.uint64(entry_id.get())
            name = str(entry_name.get())
            price = float(entry_price.get())
            num_purchases = np.uint32(entry_num_purchases.get())
            db.edit_record(record_id, name, price, num_purchases)
            messagebox.showinfo("Info", "Record edited successfully.")
            refresh_table()
        except ValueError as e:
            messagebox.showerror("Error", "Wrong type(s) of the entered data!")
        except OverflowError as e:
            messagebox.showerror("Error", "Wrong type(s) of the entered data!")
        except AttributeError as e:
            messagebox.showerror("Error", str(e))

    def clear_db():
        """Очистить базу данных"""
        db.clear()
        messagebox.showinfo("Info", "Database cleared successfully.")
        refresh_table()

    def update_db():
        """Обновить данные в GUI и ShiftTable"""
        db.update()
        messagebox.showinfo("Info", "Database updated.")
        refresh_table()

    def create_backup():
        """Создание резервной копии базы данных."""
        backup_file = db.filename + ".bak"
        shutil.copy2(db.filename, backup_file)
        messagebox.showinfo("Info", f"Backup created: {backup_file}")

    def restore_backup():
        """Восстановление базы данных из резервной копии."""
        backup_file = db.filename + ".bak"
        if not os.path.exists(backup_file):
            messagebox.showerror("Error", "Backup file does not exist.")
            return

        shutil.copy2(backup_file, db.filename)
        messagebox.showinfo("Info", "Database restored from backup.")
        refresh_table()
        db.update()

    def export_to_excel():
        """Экспорт базы данных в файл формата Excel (.xlsx)."""
        try:
            import openpyxl
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.title = "Database Records"

            # Добавляем заголовки
            sheet.append(["ID", "Name", "Price", "Number of purchases"])

            # Добавляем записи
            for record in db.get_all_records():
                sheet.append(record)

            excel_file = db.filename.replace(".txt", ".xlsx")
            workbook.save(excel_file)
            messagebox.showinfo("Info", f"Database exported to: {excel_file}")
        except ImportError:
            messagebox.showerror("Error", "Please install openpyxl to use this feature.")

    root = tk.Tk()
    root.title("File Database GUI")

    # Поля ввода
    tk.Label(root, text="ID:").grid(row=0, column=0)
    entry_id = tk.Entry(root)
    entry_id.grid(row=0, column=1)

    tk.Label(root, text="Name:").grid(row=1, column=0)
    entry_name = tk.Entry(root)
    entry_name.grid(row=1, column=1)

    tk.Label(root, text="Price:").grid(row=2, column=0)
    entry_price = tk.Entry(root)
    entry_price.grid(row=2, column=1)

    tk.Label(root, text="Number of purchases:").grid(row=3, column=0)
    entry_num_purchases = tk.Entry(root)
    entry_num_purchases.grid(row=3, column=1)

    # Поля для удаления записей по полю
    tk.Label(root, text="Delete by Field:").grid(row=6, column=0)
    delete_field = ttk.Combobox(root, values=["id", "name", "price", "num_purchases"])
    delete_field.grid(row=6, column=1)
    delete_field.set("id")

    tk.Label(root, text="Value:").grid(row=7, column=0)
    delete_value = tk.Entry(root)
    delete_value.grid(row=7, column=1)

    # Поля для поиска записей
    tk.Label(root, text="Search by Field:").grid(row=4, column=0)
    search_field = ttk.Combobox(root, values=["all", "id", "name", "price", "num_purchases"])
    search_field.grid(row=4, column=1)
    search_field.set("id")

    tk.Label(root, text="Value:").grid(row=5, column=0)
    search_value = tk.Entry(root)
    search_value.grid(row=5, column=1)

    # Таблица
    tree = ttk.Treeview(root, columns=("ID", "Name", "Price", "Number of purchases"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Price", text="Price")
    tree.heading("Number of purchases", text="Number of purchases")
    tree.grid(row=8, column=0, columnspan=3, pady=10)

    # Кнопки
    tk.Button(root, text="Create DB", command=create_db).grid(row=9, column=0)
    tk.Button(root, text="Update DB", command=update_db).grid(row=10, column=0)
    tk.Button(root, text="Clear DB", command=clear_db).grid(row=11, column=0)
    tk.Button(root, text="Delete DB", command=delete_db).grid(row=12, column=0)

    tk.Button(root, text="Add Record", command=add_record).grid(row=9, column=1)
    tk.Button(root, text="Edit Record", command=edit_record).grid(row=10, column=1)
    tk.Button(root, text="Search", command=search_records).grid(row=11, column=1)
    tk.Button(root, text="Delete Record", command=delete_record).grid(row=12, column=1)

    tk.Button(root, text="Create Backup", command=create_backup).grid(row=9, column=2)
    tk.Button(root, text="Restore Backup", command=restore_backup).grid(row=10, column=2)
    tk.Button(root, text="Export to Excel", command=export_to_excel).grid(row=11, column=2)


    root.mainloop()


if __name__ == "__main__":
    main()
