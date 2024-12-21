import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def grade_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS opros_ (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    number_phone INTEGER,
                    grade TEXT,
                    food TEXT,
                    purity TEXT
                )
            """)
            conn.commit()

###############
database = Database('db.sqlite3')
database.grade_tables()