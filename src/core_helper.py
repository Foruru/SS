from typing import List

from src.core import DatabaseCore

class DatabaseHelper(DatabaseCore):
	"""A class that provides auxiliary functions."""

	def create_tables(self, shemas: List[str]) -> None:
		"""
		Create table from shemas.

		Parameters:
			schemas (List[str]): A list of SQL statements representing table creation schemas.
		"""
		for shema in shemas:
			self.execute(shema)

	def delete_table(self, name: str) -> None:
		self.execute(f'DROP TABLE IF EXISTS {name};')
