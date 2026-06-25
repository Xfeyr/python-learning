import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# Создать таблицу
cursor.execute("CREATE TABLE IF NOT EXISTS people (name TEXT, age INTEGER)")

# Очистить таблицу (чтобы не копились дубли)
cursor.execute("DELETE FROM people")

# Добавить трёх разных людей
cursor.execute("INSERT INTO people (name, age) VALUES (?, ?)", ("Анна", 14))
cursor.execute("INSERT INTO people (name, age) VALUES (?, ?)", ("Борис", 17))
cursor.execute("INSERT INTO people (name, age) VALUES (?, ?)", ("Вера", 13))
conn.commit()

# Отсортировать по возрасту (от старшего к младшему)
cursor.execute("SELECT * FROM people ORDER BY age DESC")
print("По возрасту:", cursor.fetchall())

# Выбрать только тех, кто старше 14
cursor.execute("SELECT name FROM people WHERE age > 14")
print("Старше 14:", cursor.fetchall())
conn.close()