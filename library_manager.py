library = []

def add_book():
    title = input("Book title: ")
    author = input("Author: ")
    genre = input("Genre: ")
    year = input("Publication year: ")
    rating = input("Rating 1-5: ")
    status = input("Status (Read/Unread/Currently Reading): ")
    notes = input("Personal notes: ")

    book = {
        "title": title,
        "author": author,
        "genre": genre,
        "year": year,
        "rating": rating,
        "status": status,
        "notes": notes
    }

    library.append(book)
    print("Book added successfully.")

def view_books():
    if not library:
        print("No books added yet.")
        return

    for book in library:
        print("\n------------------------")
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Genre:", book["genre"])
        print("Year:", book["year"])
        print("Rating:", book["rating"])
        print("Status:", book["status"])
        print("Notes:", book["notes"])

def search_books():
    search = input("Search by title, author, genre, or status: ").lower()
    found = False

    for book in library:
        if (
            search in book["title"].lower()
            or search in book["author"].lower()
            or search in book["genre"].lower()
            or search in book["status"].lower()
        ):
            print("\nFound Book:")
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Genre:", book["genre"])
            print("Status:", book["status"])
            found = True

    if not found:
        print("No matching books found.")

def library_stats():
    total = len(library)
    read = sum(1 for book in library if book["status"].lower() == "read")
    unread = sum(1 for book in library if book["status"].lower() == "unread")
    currently_reading = sum(1 for book in library if book["status"].lower() == "currently reading")

    fantasy = sum(1 for book in library if book["genre"].lower() == "fantasy")
    nonfiction = sum(1 for book in library if book["genre"].lower() == "nonfiction")
    romance = sum(1 for book in library if book["genre"].lower() == "romance")

    print("\nLibrary Statistics")
    print("------------------")
    print("Total Books:", total)
    print("Books Read:", read)
    print("Books Unread:", unread)
    print("Currently Reading:", currently_reading)
    print("Fantasy Books:", fantasy)
    print("Nonfiction Books:", nonfiction)
    print("Romance Books:", romance)

def reading_goal():
    goal = int(input("How many books do you want to read this year? "))
    read = sum(1 for book in library if book["status"].lower() == "read")

    print("\nReading Goal Progress")
    print("---------------------")
    print(f"Goal: {goal} books")
    print(f"Books Read: {read}")

    if goal > 0:
        progress = (read / goal) * 100
        print(f"Progress: {progress:.2f}%")

        if progress >= 100:
            print("Goal completed!")
        elif progress >= 50:
            print("You are making good progress.")
        else:
            print("Keep going. You can do it.")

def delete_book():
    title = input("Enter the title of the book to delete: ").lower()

    for book in library:
        if book["title"].lower() == title:
            library.remove(book)
            print("Book deleted.")
            return

    print("Book not found.")

def main():
    while True:
        print("\nPersonal Library Manager")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. View Library Stats")
        print("5. Reading Goal Progress")
        print("6. Delete Book")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_books()
        elif choice == "4":
            library_stats()
        elif choice == "5":
            reading_goal()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

main()
