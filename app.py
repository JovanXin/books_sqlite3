from utils import database
import sqlite3

USER_CHOICE = """
Enter:
-'a' to add a new book
-'l' to list all books
-'r' to mark a book as read
-'s' to search books
-'d' to delete a book
-'q' to quit

Your choice:"""

def menu():
	database.create_book_table()
	while True:
		user_input = input(USER_CHOICE)
		if user_input == "q":
			break
		elif user_input == "a":
			prompt_add_book()
		elif user_input == "l":
			list_books()
		elif user_input == "r":
			prompt_read_book()
		elif user_input == "s":
			search_books()
		elif user_input == "d":
			prompt_delete_book()
		else:
			print("Unknown command, please try again\n")


def prompt_add_book():
	name = input("Enter book name:")
	author = input("Enter book author:")
	database.insert_book(name,author)


def list_books():
    for book in database.get_all_books():
        read = "YES" if book["read"] else "NO"  # book[3] will be a falsy value (0) if not read
        print(f'{book["name"]} by {book["author"]} — Read: {read}')


def search_books():
	search_type = input("Search by 'name' or 'author'")
	search_entry = input("What would you like to look for?:")
	try:
		results = database.search_books(search_type,search_entry)
	except sqlite3.OperationalError:
		print("Not a valid selection. Choose 'name' or 'author'")
	else:
		if results:
			for book in results:
				read = "YES" if book["read"] else "NO"
				print(f"{book['name']} by {book['author']} - Read:{read}")
		else:
			print(f"Sorry, no books were found with search type: {search_type} and search entry: {search_entry}")


def prompt_read_book():
	name = input("Enter which book you'd like to mark as read:")
	database.mark_book_as_read(name)


def prompt_delete_book():
	name = input("Enter which book you'd like to delete:")
	database.delete_book(name)


if __name__ == '__main__':
	menu()