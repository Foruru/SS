import os
import sqlite3
from typing import Self

class DatabaseCore():
	"""
    A class providing a basic interface to a SQLite database.

    This class offers a simplified way to interact with SQLite databases,
    handling connection, cursor, and transaction management.
    """

	def __init__(self, file: str) -> None:
		"""
        Initializes a new DatabaseCore instance.

        Args:
            file (str): The path to the SQLite database file.
        """
		self.file = file

	def __enter__(self) -> Self:
		"""
        Enables use of the 'with' statement for context management.

        Returns:
            Self: The current DatabaseCore instance.
        """
		try:
			self.conn = sqlite3.connect(self.file)
			self.cur = self.conn.cursor()
		except sqlite3.OperationalError as e:
			print(f"Error opening database: {e}")

		return self

	def __exit__(self, exc_type, exc_val, exc_tb) -> None:
		"""
        Handles cleanup when exiting the 'with' block.

        Commits any pending transactions and closes the database connection.
        """
		self.commit()
		self.close()

	def query(self, statement: str, parameters="") -> any:
		"""
		Executes a SELECT query.

		Args:
            statement (str): The SQL SELECT statement.
            parameters (tuple, optional): Parameters for the query. Defaults to "".

        Returns:
            any: The result of the query.
        """
		try:
			return self.cur.execute(statement, parameters)
		except sqlite3.Error as e:
			print(f"Sql runtime error: {e}")

	def execute(self, statement: str, parameters="") -> None:
		"""
        Executes an arbitrary SQL statement.

        Args:
            statement (str): The SQL statement to execute.
			parameters (tuple, optional): Parameters for the execute. Defaults to "".
        """
		try:
			self.cur.execute(statement, parameters)
		except sqlite3.Error as e:
			print(f"Sql runtime error: {e}")

	def commit(self) -> None:
		"""Commits any pending transactions."""
		try:
			self.conn.commit()
		except sqlite3.Error as e:
			print(f"Commit error: {e}")


	def close(self) -> None:
		"""Closes the database connection."""
		try:
			self.conn.close()
		except sqlite3.Error as e:
			print(f"Close error: {e}")
