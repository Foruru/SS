from examples.users import Users

class Database(Users):
	"""
	Handles database operations for the application.

	Inherits from the Users class for user-related functionalities.
	"""

	def create_tables(self) -> None:
		"""
		Creates the necessary tables for the application.

		This method creates two tables:
			- users: Stores user information (ID, name, username, chat_id, balance)
			- for_delete: Temporary storage for usernames to be deleted
		"""
		self.execute("""
				CREATE TABLE IF NOT EXISTS users (
					ID INTEGER PRIMARY KEY AUTOINCREMENT,
					first_name TEXT,
					last_name TEXT,
					username TEXT,
					chat_id INTEGER UNIQUE,
					balance INTEGER
				);
			""")
		self.execute("""
				CREATE TABLE IF NOT EXISTS for_delete (
					username TEXT
				);
			""")

	def delete_table(self, name: str) -> None:
		"""
		Deletes a specified table.

		Args:
			name (str): The name of the table to delete.
		"""
		self.execute(f'DROP TABLE IF EXISTS {name};')

