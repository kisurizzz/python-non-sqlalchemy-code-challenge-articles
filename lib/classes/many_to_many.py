class Article:
    all = []
    def __init__(self, author, magazine, title):
        if not isinstance(title,str):
            raise ValueError('Title must be a string')
        if not (5 <= len(title) <= 50):
            raise ValueError('Title must be between 5 and 50 characters')
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        raise AttributeError ('Title is immutable')
       
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError('Name must be a string')
        if not name:
            raise ValueError('Name cannot be empty')
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        raise AttributeError ('Name is immutable')


    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass