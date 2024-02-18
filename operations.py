from datetime import datetime
class Library:
    def __init__(self):
        self.file_name = "books.txt"

    def add_book(self):
        while True:
            try:
                new_book_name = input("Name of the book: ")
                new_author_name = input("Author of the book: ")            
                new_publish_str = input("Publish year of the book in YYY-MM-DD format: ")
                new_publish_date = datetime.strptime(new_publish_str, "%Y-%m-%d")
                new_number_pages = int(input("Number of pages of the book: "))
                
                if not new_book_name or not new_author_name or not new_publish_date or not  new_number_pages:
                    print("Book title, author, publication date and number of pages are mandatory fields. Make sure you enter the information for all three.")
                    continue
                
                info_of_books = f"{new_book_name},{new_author_name},{new_publish_date.strftime('%Y-%m-%d')},{new_number_pages}"

                with open(self.file_name, mode = 'a+', encoding='utf-8') as file: #Türkçe karakter sorunu çözümü encoding='utf-8'
                    file.write(info_of_books+"\n")
                    print("New book successfully added.")
                break 

            except ValueError as ve:
                print(f"Incorrect entry. \n Please enter the date in YYYY-MM-DD format. \n Use numbers when entering the number of pages in the legend. \n Error : '{ve}'") 

            except Exception as e:
                print(f"Error occurred! Error: '{e}'")


    def list_of_books(self):
        try:
            with open(self.file_name, mode='a+', encoding='utf-8') as file:
                file.seek(0) #İmleç sayfa başına gider
                info_of_books=file.read().splitlines()
                if info_of_books:
                    for i in info_of_books:
                        control_books_of_value =  i.split(',')
                        if len(control_books_of_value) == 4: 
                            book_name, author_name, publish_date, number_pages = control_books_of_value
                            print(f"Name of book : {book_name}  Author of book : {author_name}")
                        else:
                            print("incorrect registration!", )
                            break
                else:
                    print("No books have been added to the list yet.")
        except FileNotFoundError:
            print("File not found!")

    def remove_book(self):
        try:
            remove_book_name = input("Enter the name of the book you want to delete: ")

            with open(self.file_name, mode='a+', encoding='utf-8') as file:
                file.seek(0) #imleci sayfanın en başına getirir
                all_books = file.readlines()
                file.truncate(0)  #dosyayı temizler

                found_book = False 

                for info_remove_book in all_books:
                    if remove_book_name not in info_remove_book:
                        file.write(info_remove_book)
                    else:
                        found_book = True
                
                if found_book:
                    print(f"The book {remove_book_name} was successfully deleted.")
                else:
                    print(f"The book {remove_book_name}  is not on the list.")


            with open(self.file_name, mode='+a', encoding='utf-8') as file:
                # Dosyada kalan kitapları tekrar yaz
                file.seek(0)
                remaining_books = file.read()
                print("Remaining books:\n",remaining_books)

        except Exception as e:
            print(f"Error occurred! Error: '{e}'")


  
