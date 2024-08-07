import os
from dotenv import load_dotenv

from examples.db import Database

SHEMAS = ["""
			CREATE TABLE IF NOT EXISTS users (
				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				first_name TEXT,
				last_name TEXT,
				username TEXT,
				chat_id INTEGER UNIQUE,
				balance INTEGER
			);
		""", 
		"""
			CREATE TABLE IF NOT EXISTS for_delete (
				username TEXT
			);
		"""
]

def main():
	load_dotenv()
	with Database(os.getenv('DB_PATH')) as db:
		db.create_tables(SHEMAS)

		user = ["qwer", "ty", "qwert", 1234567890]
		db.new_user(*user)

		db.replenishment(1234567890, 1488)
		print(db.get_balance(1234567890))

if __name__ == '__main__':
	main()
