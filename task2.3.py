class Books:
    def __init__(self, name, author):
        self.name=name
        self.author=author

War_And_Peace=Books("Война и мир","Л.Н. Толстой")
print(f"Книга с названием \"{War_And_Peace.name}\" от автора {War_And_Peace.author}")