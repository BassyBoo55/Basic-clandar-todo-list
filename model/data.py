class data:
    def __init__(self, name, importance):
        self.name = name
        self.importance = importance

    def save(self, cursor):
        cursor.execute(f'INSERT INTO data (name, importance) VALUES ("{self.name}",{self.rank})')