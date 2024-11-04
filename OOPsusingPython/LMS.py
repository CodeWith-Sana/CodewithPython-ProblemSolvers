class Book:
    title = ""
    _authName = ""
    __ISBN = None
    def __init__(self , title ,authName , ISBN):
        self.title = title
        self._authName = authName
        self.__ISBN = ISBN
    def get_BOOKdata(self):
        print(f"Book title  is  :{self.title}")
        print(f"Book Author   is  :{self._authName}")
        print(f"Book ISBN  is  :{self.__ISBN}")
    def get_ISBN(self, isbn):
        self.__ISBN =  isbn
        return self.__ISBN
        print(f"the new ISBN number is :{self.__ISBN}")
b1 =  Book("Evolution Of Man" , "Darwin" , 123456789)
b1.get_BOOKdata()
print(b1.get_ISBN(123456))
#will throw an erro b/c aof private attribute
# print(b1.__ISBN)