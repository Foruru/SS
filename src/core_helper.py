from src.core import DatabaseCore

class DatabaseHelper(DatabaseCore):
	"""A class that provides auxiliary functions."""

	def create_tables(self, shemas: list[str]) -> None:
		for shema in shemas:
			self.execute(shema)

	def delete_table(self, name: str) -> None:
		self.execute(f'DROP TABLE IF EXISTS {name};')
