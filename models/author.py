class Author:
    def __init__(self, id, name):  
        self.id = id
        self.name = name

    def __repr__(self): 
        return f'<Author {self.name}>'

    # Getter for name
    @property
    def name(self):
        return self._name


    @name.setter #setter for name to enforce the parameters passed ...
    def name(self, value):
        if not hasattr(self, '_name'):
            self._name = value
        else:
            raise ValueError("Name cannot be changed after instantiation.")
