"""
Задание 1.
Условие:
Написать функцию на Python, которой передаются в качестве параметров команда и текст.
Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False в противном случае.
Передаваться должна только одна строка, разбиение вывода использовать не нужно.
"""
import subprocess

def return_res(cmd, text):
    result = subprocess.run(cmd,
                            shell=True,
                            stdout=subprocess.PIPE,
                            encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(return_res("cat /etc/os-release", "22.04.1"))