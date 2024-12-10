# Özellikler:
"""
Kitap listesi görüntüleme.
Kitap ekleme ve silme.
Kitap ödünç alma.
Kitap geri teslim etme.
Veritabanını (JSON dosyası) kullanarak
kitapların durumunu kaydetme.
"""

import json

# Kitap veritabanın dosyası
DB_FILE = "kutuphane.json"

# Veritabanını yükleme veya yeni oluşturma
def load_database():
    try:
        with open(DB_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Veritabanını kaydetme     
def save_database(data):
    with open(DB_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Kitapları listeleme
def list_books(library):
    print("\nKütüphane Kitapları:")
    for book, status in library.items():
        print(f"- {book} (Durum: {'Mevcut' if status else 'Ödünçte'})")
    print()

# Kitap ekleme
def add_book(library):
    book_name = input("Eklemek istediğiniz kitabın adını girin: ").strip()
    if book_name in library:
        print("Bu kitap zaten kütüphanede mevcut!")
    else:
        library[book_name] = True
        print(f"'{book_name}' kütüphaneye eklendi.")
    save_database(library)

# Kitap silme
def remove_book(library):
    book_name = input("Silmek istediğiniz kitabın adını girin: ").strip()
    if book_name in library:
        del library[book_name]
        print(f"'{book_name}' kütüphaneden silindi.")
    else:
        print("Bu kitap kütüphanede bulunamadı!")
    save_database(library)

# Kitap ödünç alma
def borrow_book(library):
    book_name = input("Ödünç almak istediğiniz kitabın adını girin: ").strip()
    if book_name in library and library[book_name]:
        library[book_name] = False  # Kitabın durumu True'dan False'a değiştirilir
        print(f"'{book_name}' kitabını ödünç aldınız.")
    elif book_name in library:
        print(f"'{book_name}' kitabı şu anda ödünçte.")
    else:
        print("Bu kitap kütüphanede bulunamadı!")
    save_database(library)

# Kitap geri teslim etme
def return_book(library):
    book_name = input("Geri teslim etmek istediğiniz kitabın adını girin: ").strip()
    if book_name in library and not library[book_name]:
        library[book_name] = True
        print(f"'{book_name}' kitabını geri teslim ettiniz.")
    elif book_name in library:
        print(f"'{book_name}' zaten kütüphanede mevcut!")
    else:
        print("Bu kitap kütüphanede bulunamadı!")
    save_database(library)

# Ana menü
def main():
    library = load_database()
    while True:
        print("\nKütüphane Yönetim Sistemi")
        print("1. Kitapları Listele")
        print("2. Kitap Ekle")
        print("3. Kitap Sil")
        print("4. Kitap Ödünç Al")
        print("5. Kitap Geri Teslim Et")
        print("6. Çıkış")

        choice = input("Seçiminizi yapın (1-6): ").strip()

        if choice == "1":
            list_books(library)
        elif choice == "2":
            add_book(library)
        elif choice == "3":
            remove_book(library)
        elif choice == "4":
            borrow_book(library)
        elif choice == "5":
            return_book(library)
        elif choice == "6":
            print("Çıkış yapılıyor. İyi günler!")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

# Uygulamayı başlat
if __name__ == "__main__":
    main()

