from django.shortcuts import render
from .form import BookForm,SearchForm
from .library import Library

# list view of home page
def bookList(request):
    l = Library()
    bookList = l.getBookList()
    return render(request, 'book_list.html',{'books':bookList})

# add a new book procedure 
def addBook(request):
    form = BookForm()
    msg = ''
    if request.method =='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            if ',' in form.cleaned_data['title'] and ',' in form.cleaned_data['author']:
                str = '\n"'+form.cleaned_data['title']+'",'+'"'+form.cleaned_data['author']+'",'+form.cleaned_data['genre']+','+form.cleaned_data['hight']+','+form.cleaned_data['publisher']
            elif ',' not in form.cleaned_data['title'] and ',' in form.cleaned_data['author']:
                str = '\n'+form.cleaned_data['title']+','+'"'+form.cleaned_data['author']+'",'+form.cleaned_data['genre']+','+form.cleaned_data['hight']+','+form.cleaned_data['publisher']
            elif ',' in form.cleaned_data['title'] and ',' not in form.cleaned_data['author']:
                str = '\n"'+form.cleaned_data['title']+'",'+form.cleaned_data['author']+','+form.cleaned_data['genre']+','+form.cleaned_data['hight']+','+form.cleaned_data['publisher']
            else:
                str = '\n'+form.cleaned_data['title']+', '+form.cleaned_data['author']+', '+form.cleaned_data['genre']+','+form.cleaned_data['hight']+','+form.cleaned_data['publisher']
            f = open('books_list.txt','a')
            f.write(str)
            f.close()
            msg = 'Succsessfully added' 
        else:
            msg = "Book isn't added, please fill all fields" 
    return render(request, 'book_form.html',{'msg':msg})

#deleting a recode procedure
def delete(request,id):
    before = True
    after = True
    with open('books_list.txt', 'r') as fr:
        lines = fr.readlines()
        ptr = 1
        with open('books_list.txt', 'w') as fw:
            for line in lines:
                if ptr != id+1:
                    fw.write(line)
                    if not before:
                        after = False
                else:
                    before =False
                ptr+=1
    if after:
        with open('books_list.txt') as f_input:
            data = f_input.read().rstrip('\n')
        with open('books_list.txt', 'w') as f_output:    
            f_output.write(data)
    l = Library()
    bookList = l.getBookList()
    return render(request, 'book_list.html',{'books':bookList})


#searching procedure
def search(request):
    l = Library()
    b = l.getBookList()
    text = ''
    select = ''
    form = SearchForm()
    if request.method =='POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            select = form.cleaned_data['select']
            text = form.cleaned_data['search']
    if select == 'title':
        bookList = l.searchByTitle(text,b)
    else:
        bookList = l.searchByGenre(text,b) 
    return render(request, 'search_list.html',{'books':bookList})