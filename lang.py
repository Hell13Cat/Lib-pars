class Lang():
    def __init__(self, lang) -> None:
        super().__init__()
        if lang == "en":
            self.name = ""
        elif lang == "ru":
            self.name = "Парсер книг"
        else:
            self.name = "Book parser"