# TODO Найдите количество книг, которое можно разместить на дискете
disk_size=1.44
pages=100
lines_on_page=50
count_on_page=25
bytes_on_char=4

disk_size_bytes=disk_size*1024*1024
how_book_size_page=bytes_on_char*count_on_page*lines_on_page*pages
books_on_disk=disk_size_bytes//how_book_size_page

print(f"Количество книг, помещающихся на дискету: {books_on_disk:.0f}" )
