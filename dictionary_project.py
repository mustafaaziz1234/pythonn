books = ["Matilda", 'Diary of a wimpykid', 'Junglebook', 'Charlottes web' , 'Web']
print('list of books', books)
print("first book:", books[0])
print('Second book:', books[1])
print('Last book:',books[-1])

books.append("Harry potter")
books.remove("Web")
books.sort()
books.reverse()

#dictionary

teacher = {'name:': "Ms.Priya", 'Section:': 'children books', 'Experience': 5}
teacher["email"] = "priya123@gmail.com"
teacher['Experience'] = 4
teacher.pop("Section:")

#converting

list = [101,102,103,104,105]
book_names = {'Matilda', 'Junglebook', 'Harry potter', 'Diary of a wimpykid', 'Charlottes web'}
book_nums = dict(zip(list,book_names))
#summary
print("==========LIBRARY ORGANISER SUMMARY==========")
print("\nlibrarian details:", teacher)
print("\nAvailable books:", book_names)
print("\nbooks ids:", book_nums) 



