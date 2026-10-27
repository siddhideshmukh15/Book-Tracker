books=[]
while True:
    print("===== Book Tracker====")
    print("1. Add Book")
    print("2. View Book ")
    print("3. Update Reading Status")
    print("4. Delete Book")
    print("5. Exit")

    choice=input("Enter your choice:")

    if choice=="1":
        title=input("Enter book title:")
        author=input("Enter author name:")

        book={
            "title":title,
            "author":author,
            "status":"Not started"

        }
        books.append(book)
        print("Book added successfully!")

    elif choice=="2":
        if not books:
            print("No books found!")
        else:
            print("\n Your book Collection:")
            for i ,book in enumerate(books,1):
                print(f"{i}.{book["status"]} by {book['author']}")
                print("status:",book["status"])

    elif choice=="3":
        if not books:
            print("no books available to update!")

        else:
            for i,book in enumerate(books,1):
                print(f"{i}.{book['title']}-{book['status']}")

                try:
                    number=int(input("Enter book number:"))

                    if 1<=number<=len(books):
                        print("1. Not Started")
                        print("2. Reading completed")
                        print("3.Completed")

                        status_choice=input("Choose new status:")

                        if status_choice=="1":
                            books[number-1]["status"]="Not Started"

                        elif status_choice=="2":

                            books[number-1]["status"]="Reading"
                        elif status_choice=="3":
                            books[number-1]["status"]="Completed"
                        else:
                            print("Invalid book number!")
                except ValueError:
                    print("please enter a valid number!")
    elif choice=="4":
        try:
            n=int(input("Book number to delete."))

            if 1<=n<=len(books):
                books.pop(n-1)
                print("Book deleted!")
            else:
                print("Invalid book number!")

        except ValueError:
            print("Enter a valid number!")
            

    elif choice=="5":
        print("Thank you for using Book Tracker!")
        break
    else:
        print("Invalid choice!please try again. ")
                