import os
import pandas as pd

pd.options.display.max_columns = None

def database_search():
    print("Функция Database Search пока не реализована. Возвращение в меню...\n")

def telegram_search():
    print("Поиск в базе Telegram...")
    telegram_folder = "FAVAKIN/Telegram"
    files = [
        "tg1.csv", "tg2.csv", "tg3.csv", "tg4.csv", "tg5.csv",
        "tg6.txt", "tg7.txt", "tg8.txt", "tg9.csv", "tg10.csv",
        "tg11.csv", "tg12.txt", "tg13.txt", "tg14.csv"
    ]
    search_term = input("Введите запрос для поиска: ").lower()
    for file in files:
        file_path = os.path.join(telegram_folder, file)
        if not os.path.exists(file_path):
            print(f"Файл {file} не найден. Пропускаем.")
            continue
        try:
            if file.endswith(".csv"):
                print(f"Ищем в {file}...")
                for chunk in pd.read_csv(file_path, chunksize=100000, low_memory=False):
                    results = chunk[chunk.apply(
                        lambda row: search_term in row.astype(str).str.lower().to_list(), axis=1)]
                    if not results.empty:
                        print(f"Найдено совпадений в {file}:")
                        print(results)
                        return
                print(f"Совпадений не найдено в {file}.")
            elif file.endswith(".txt"):
                print(f"Ищем в {file}...")
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    matches = [line for line in lines if search_term in line.lower()]
                    if matches:
                        print(f"Найдено совпадений в {file}:")
                        for match in matches:
                            print(match.strip())
                        return
                print(f"Совпадений не найдено в {file}.")
        except Exception as e:
            print(f"Ошибка обработки файла {file}: {e}")
    print("Поиск завершен. Возвращение в меню...")

def getcontact_search():
    print("Функция GetContact Search пока не реализована. Возвращение в меню...\n")

def discord_facebook_search():
    print("Функция Discord Facebook Search пока не реализована. Возвращение в меню...\n")

def nickname_search():
    print("Функция Nickname Search пока не реализована. Возвращение в меню...\n")

def vk_search():
    print("Функция VK Search пока не реализована. Возвращение в меню...\n")

def card_search():
    print("Функция Card Search пока не реализована. Возвращение в меню...\n")

def tiktok_search():
    print("Функция TikTok Search пока не реализована. Возвращение в меню...\n")

def avito_search():
    print("Функция Avito Search пока не реализована. Возвращение в меню...\n")

def main_menu():
    while True:
        print("\nВыберите функцию:")
        print("1. Database Search")
        print("2. Telegram Search")
        print("3. GetContact Search")
        print("4. Discord Facebook Search")
        print("5. Nickname Search")
        print("6. VK Search")
        print("7. Card Search")
        print("8. TikTok Search")
        print("9. Avito Search")
        print("0. Выход")
        choice = input("\nВаш выбор: ")
        if choice == "1":
            database_search()
        elif choice == "2":
            telegram_search()
        elif choice == "3":
            getcontact_search()
        elif choice == "4":
            discord_facebook_search()
        elif choice == "5":
            nickname_search()
        elif choice == "6":
            vk_search()
        elif choice == "7":
            card_search()
        elif choice == "8":
            tiktok_search()
        elif choice == "9":
            avito_search()
        elif choice == "0":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

main_menu()