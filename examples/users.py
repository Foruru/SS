from src.core import DatabaseCore

class Users(DatabaseCore):
	"""
	Handles user-related database operations.

	Inherits from the DatabaseCore class for database interactions.
	"""

	def new_user(self, first_name: str, last_name: str, username: str, chat_id: int) -> None:
		"""
		Creates a new user in the database.

		Args:
			first_name (str): The user's first name.
			last_name (str): The user's last name.
			username (str): The user's username.
			chat_id (int): The user's chat ID.
		"""
		self.execute(
			'INSERT INTO users (first_name, last_name, username, chat_id, balance) VALUES (?, ?, ?, ?, ?)', 
			[first_name, last_name, username, chat_id, 0]
		)

	def remove_user(self, chat_id: int) -> None:
		"""
		Removes a user from the database.

		Args:
			chat_id (int): The chat ID of the user to remove.
		"""
		self.query('DELETE FROM users WHERE chat_id=?', [chat_id]);

	def get_first_name(self, chat_id: int) -> str:
		"""
		Retrieves the first name of a user.

		Args:
			chat_id (int): The chat ID of the user.

		Returns:
			str: The user's first name.
		"""
		return self.query('SELECT first_name FROM users WHERE chat_id=?', [chat_id]).fetchone()[0]

	def get_balance(self, chat_id: int) -> int:
		"""
		Retrieves the balance of a user.

		Args:
			chat_id (int): The chat ID of the user.

		Returns:
			int: The user's balance.
		"""
		return self.query('SELECT balance FROM users WHERE chat_id=?', [chat_id]).fetchone()[0]

	def replenishment(self, chat_id, amount) -> None:
		"""
		Updates the balance of a user.

		Args:
			chat_id (int): The chat ID of the user.
			amount (int): The amount to add to the balance.
		"""
		self.execute('UPDATE users SET balance=? WHERE chat_id=?', [amount, chat_id])
