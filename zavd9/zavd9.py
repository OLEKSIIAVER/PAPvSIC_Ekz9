import pefile


def list_imports(pe_file):
    # Завантажуємо PE-файл
    pe = pefile.PE(pe_file)

    # Перевіряємо наявність розділу імпорту
    if not hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
        print("Цей файл не має імпортованих бібліотек.")
        return

    # Проходимо по всіх імпортах
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        print(f"\nБібліотека: {entry.dll.decode()}")

        for imp in entry.imports:
            print(f"  - {imp.name.decode() if imp.name else 'Невідома функція'} (за адресою: {hex(imp.address)})")


if __name__ == "__main__":
    # Введіть шлях до PE-файлу
    pe_file = input("Введіть шлях до PE-файлу: ")

    try:
        list_imports(pe_file)
    except Exception as e:
        print(f"Помилка при аналізі файлу: {e}")

#C:\Windows\System32\kernel32.dll
