import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('SCHEDULE.db')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Todo (task TEXT)")  # Create Todo table if it doesn't exist
        self.cur.execute("CREATE TABLE IF NOT EXISTS inProgress (task TEXT)")  # Create inProgress table if it doesn't exist
        self.cur.execute("CREATE TABLE IF NOT EXISTS Completed (task TEXT)")  # Create Completed table if it doesn't exist

    def insert(self, table, task):
        self.cur.execute(f"INSERT INTO {table} VALUES (?)", (task,))  # Insert task into the specified table
        self.conn.commit()

    def fetch(self, table):
        self.cur.execute(f"SELECT * FROM {table}")  # Fetch all rows from the specified table
        rows = self.cur.fetchall()
        return rows
    
    def delete(self, table, task):
        self.cur.execute(f"DELETE FROM {table} WHERE task=?", (task,))  # Delete the specified task from the specified table
        self.conn.commit()

    def update(self, table, task, new_task):
        self.cur.execute(f"UPDATE {table} SET task=? WHERE task=?", (new_task, task))   # Update the specified task in the specified table
        self.conn.commit()

    def delete_all(self, table = None):
        if table:
            self.cur.execute(f"DELETE FROM {table}")  # Delete all data from the specified table

        else:
            self.cur.execute("DELETE FROM Todo")  # Delete all data from the Todo table
            self.cur.execute("DELETE FROM inProgress")  # Delete all data from the inProgress table
            self.cur.execute("DELETE FROM Completed")  # Delete all data from the Completed table

        self.conn.commit()

    def close(self):
        self.conn.close()
