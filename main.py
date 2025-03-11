# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import subprocess

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def check_git_version():
    try:
        # Выполняем команду 'git --version' через командную строку
        result = subprocess.run(['git', '--version'], capture_output=True, text=True, check=True)

        # Выводим результат, если команда выполнена успешно
        print("Git установлен. Версия:", result.stdout.strip())
    except FileNotFoundError:
        # Если команда 'git' не найдена, значит Git не установлен
        print("Git не установлен или не добавлен в PATH.")
    except subprocess.CalledProcessError as e:
        # Обработка ошибок, если команда завершилась с ошибкой
        print("Произошла ошибка при проверке версии Git:", e)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_git_version()


