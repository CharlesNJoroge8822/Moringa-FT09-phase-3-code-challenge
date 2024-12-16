class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.name}>'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        # Ensure the name is between 2 and 16 characters
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        # Ensure category is not empty
        if len(category) == 0:
            raise ValueError("Category must not be empty.")
        self._category = category

    def repr(self):
        return f'<Magazine {self.name}>'
