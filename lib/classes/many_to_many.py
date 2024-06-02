class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            raise Exception("The title cannot be changed")
        elif not isinstance(value, str):
            raise Exception("Title must be a string")
        elif not 5 <= len(value) <=50:
            raise Exception("The title must be between 5 and 50 char inclusive")
        else:
            self._title = value
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be of instance 'Author'")
        else:
            self._author = value
          
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be of instance 'Magazine'")
        else:
            self._magazine = value
        
class Author():

    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise Exception("Name cannot be changed")
        elif not type(value) is str:
            raise Exception("Name must be a string")
        else:
            self._name = value


    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in Article.all if article.author == self})
        # magazine_list = []
        # for article in Article.all:
        #     if article.author == self and article.magazine not in magazine_list:
        #         magazine_list.append(article.magazine)
        # return magazine_list

    def add_article(self, magazine, title):
        return Article(self, magazine, title)


    def topic_areas(self):
        topics = list({article.magazine.category for article in Article.all if article.author == self})
        return topics if topics else None

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        elif not 2 <= len(value) <= 16:
            raise Exception("Name must be between 2 and 16 char inclusive")
        else:
            self._name = value
            
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise Exception("Category must be a string")
        elif not len(value) > 0:
            raise Exception("Category must be filled ")
        else:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in Article.all if article.magazine == self})

    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        return titles if titles else None

    def contributing_authors(self):
        author_list = [article.author for article in Article.all if article.magazine == self]
        mt2 = []
        for i in author_list:
            if author_list.count(i) > 2:
                mt2.append(i)
        return mt2 if mt2 else None