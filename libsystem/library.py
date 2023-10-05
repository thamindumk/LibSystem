class Library:
    def __init__(self):
        pass
    
    # return a list of book dictionary object
    def getBookList(self):
        x = open('books_list.txt','r')
        books = x.readlines()
        bookLIst = []
        for line in books[1:]:
            line = line.strip('\n')
            lst = line.split(',')
            if '"' in lst[0] and '"' in lst[2]:
                book = {'title':lst[0]+" ,"+lst[1],
                        'author':lst[2][1:]+" ,"+lst[3][:-1],
                        'genre':lst[4],
                        'hight':lst[5],
                        'publisher':lst[6]}
                bookLIst.append(book)
            elif '"' not in lst[0] and '"' in lst[1]:
                book = {'title':lst[0],
                        'author':lst[1][1:]+" ,"+lst[2][:-1],
                        'genre':lst[3],
                        'hight':lst[4],
                        'publisher':lst[5]}
                bookLIst.append(book)
            elif '"' in lst[0] and '"' not in lst[2]:
                book = {'title':lst[0]+" ,"+lst[1],
                        'author':lst[2],
                        'genre':lst[3],
                        'hight':lst[4],
                        'publisher':lst[5]}
                bookLIst.append(book)    
            else:
                book = {'title':lst[0],
                        'author':lst[1],
                        'genre':lst[2],
                        'hight':lst[3],
                        'publisher':lst[4]}
                bookLIst.append(book)
        x.close()
        return bookLIst
    
    # search books by it's title
    def searchByTitle(self,title,booklist):
        lst = []
        for b in booklist:
            if title in b.get('title'):
                lst.append(b)
        return lst
    
    # search books by it's genre
    def searchByGenre(self,genre,booklist):
        lst = []
        for b in booklist:
            if genre in b.get('genre'):
                lst.append(b)
        return lst
    