from data import get_contacts, add_contact, update_contact, delete_contact, conn
import time
import os


def clear_terminal():
	# Clear the terminal screen based on the operating system
	os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
	while True:
		clear_terminal()
		print("\n=== Меню управления контактами ===")
		print("1. Показать все контакты")
		print("2. Найти контакт по ID")
		print("3. Добавить контакт")
		print("4. Обновить контакт")
		print("5. Удалить контакт")
		print("6. Выйти")
		choice = input("\nВыберите действие (1-6): ")

		if choice == "1":
			get_contacts()
			time.sleep(2)

		elif choice == "2":
			contact_id = int(input("Введите id контакта: "))
			get_contacts(contact_id)
			time.sleep(2)

		elif choice == "3":
			add_contact()
			time.sleep(2)

		elif choice == "4":

			update_contact()
			time.sleep(2)

		elif choice == "5":
			delete_contact()
			time.sleep(2)
		elif choice == "6":
			print("\nДо свидания!")
			time.sleep(1)
			break
		else:
			print("\nНеверный выбор, попробуйте снова.\n")
			time.sleep(2)

# Запуск программы
if __name__ == "__main__":
	main_menu()

	# Закрытие соединения
	conn.close()
