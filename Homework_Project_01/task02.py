"""
Задание 2. (повышенной сложности)
Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы,
в котором вывод разбивается на слова с удалением всех знаков пунктуации
(их можно взять из списка string.punctuation модуля string).
В этом режиме должно проверяться наличие слова в выводе.
"""
import subprocess
import string

def return_res(cmd, text):
    result = subprocess.run(cmd,
                            shell=True,
                            stdout=subprocess.PIPE,
                            encoding='utf-8')
    for i in result.stdout:
        if i in string.punctuation:
            result.stdout = result.stdout.replace(i, " ")
    out = result.stdout.split()

    if text in out and result.returncode == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(return_res("cat /etc/os-release", "jammy"))