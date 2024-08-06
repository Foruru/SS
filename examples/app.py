import os
from dotenv import load_dotenv

from examples.db import Database

def main():
	load_dotenv()
	with Database(os.getenv('DB_PATH')) as db:
		db.create_tables()

		user = ["qwer", "ty", "qwert", 1234567890]
		db.new_user(*user)

		db.replenishment(1234567890, 1488)
		print(db.get_balance(1234567890))

if __name__ == '__main__':
	main()
