import sqlite3

DB_NAME = "countries.db"

class CountryDB:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                capital TEXT,
                population INTEGER,
                region TEXT,
                searched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def save(self, country):
        self.cursor.execute("""
            INSERT INTO history (name, capital, population, region)
            VALUES (?, ?, ?, ?)
        """, (
            country["name"]["common"],
            ", ".join(country.get("capital", ["N/A"])),
            country.get("population", 0),
            country.get("region", "N/A")
        ))
        self.conn.commit()

    def get_history(self):
        self.cursor.execute("""
            SELECT name, capital, population, region, searched_at
            FROM history
            ORDER BY searched_at DESC
        """)
        return self.cursor.fetchall()

    def get_stats(self):
        self.cursor.execute("""
            SELECT region, COUNT(*) as count
            FROM history
            GROUP BY region
            ORDER BY count DESC
            LIMIT 1
        """)
        return self.cursor.fetchone()