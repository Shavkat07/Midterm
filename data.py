import sqlite3

# Подключение к базе данных
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()


def get_contacts(contact_id=None):
	if contact_id is not None:
		cursor.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
		print(cursor.fetchone())
		return


	cursor.execute("SELECT * FROM contacts")
	for i in cursor.fetchall():
		print(i)
	return


# Функция для добавления контакта
def add_contact():
	name = input("Введите имя: ")
	phone = input("Введите телефон: ")
	email = input("Введите email: ")
	address = input("Введите адрес: ")
	cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
	               (name, phone, email, address))
	conn.commit()
	print("Successfully added contact!")

# Функция для обновления контакта
def update_contact():
	contact_id = input("Введите ID контакта, который хотите обновить: ")
	name = input("Введите новое имя (или оставьте пустым, чтобы не изменять): ")
	phone = input("Введите новый телефон (или оставьте пустым, чтобы не изменять): ")
	email = input("Введите новый email (или оставьте пустым, чтобы не изменять): ")
	address = input("Введите новый адрес (или оставьте пустым, чтобы не изменять): ")
	
	if name:
		cursor.execute("UPDATE contacts SET name = ? WHERE id = ?", (name, contact_id))
	if phone:
		cursor.execute("UPDATE contacts SET phone = ? WHERE id = ?", (phone, contact_id))
	if email:
		cursor.execute("UPDATE contacts SET email = ? WHERE id = ?", (email, contact_id))
	if address:
		cursor.execute("UPDATE contacts SET address = ? WHERE id = ?", (address, contact_id))
	conn.commit()

	print("Contact updated successfully!")

# Функция для удаления контакта
def delete_contact():
	contact_id = input("Введите ID контакта, который хотите удалить: ")
	cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
	conn.commit()

	print("Contact deleted successfully!")



# Пример вызовов функций
# add_contact("Shavkat", "998901234567", "shavkat@example.com", "Asia/Toshkent")
# update_contact(1, name="Shavkat")
# delete_contact(1)

# Закрытие соединения
# conn.close()
