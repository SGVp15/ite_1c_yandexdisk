import re
import time

import keyboard
import pyperclip

from windows import wait_windows

time_sleep = 0.3


def write_in_1c(urls):
    for url in urls:
        time.sleep(time_sleep)
        wait_windows('192.168.20.3 — Подключение к удаленному рабочему столу')
        keyboard.press_and_release('insert')
        time.sleep(time_sleep)
        keyboard.write(url)
        print(url)
        time.sleep(time_sleep)
        keyboard.press_and_release('enter')


def get_urls_yandex(num=5) -> [str]:
    urls = []
    pyperclip.copy('')
    time.sleep(time_sleep)
    keyboard.press_and_release('home')
    pyperclip.copy('')

    for i in range(num):
        keyboard.press_and_release('space')

        k = 0
        while True:
            k += 1
            if k > 20:
                raise 'Error url'

            time.sleep(0.5)
            url = pyperclip.paste()
            if re.findall('https://disk.yandex.ru', url) and url not in urls:
                urls.append(url)
                break
            else:
                # pyautogui.hotkey('alt', 'ф')
                keyboard.press_and_release('alt')
                for _ in range(5):
                    keyboard.press_and_release('down')
                    time.sleep(0.1)
                keyboard.press_and_release('enter')
                time.sleep(0.5)
        keyboard.press_and_release('down')
    return urls


def main(urls, inc=5):
    if not urls:
        wait_windows('Яндекс.Диск')
        time.sleep(1)
        wait_windows('Яндекс.Диск')
        urls = get_urls_yandex(num=inc)

    wait_windows('192.168.20.3 — Подключение к удаленному рабочему столу', timeout=10)
    time.sleep(0.5)
    write_in_1c(urls)


if __name__ == '__main__':
    count_url=5

    urls = ''''''


    urls = urls.split('\n')
    urls = [u.strip() for u in urls if u.strip()]

    main(inc=count_url, urls=urls)

# ['\t', '\n',
# '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
# ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
# '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
# 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
# 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
# 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
# 'browserb
# ack', 'browserfavorites', 'browserforward', 'browserhome',
# 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
# 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
# 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
# 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
# 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
# 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
# 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
# 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
# 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
# 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
# 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
# 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
# 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
# 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
# 'command', 'option', 'optionleft', 'optionright']
