import re
import time

import keyboard
import pyperclip

from windows import wait_windows

time_sleep = 0.3
import pygetwindow as pg


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


def ctrlc():
    keyboard.press_and_release('ctrl + c')
    time.sleep(0.1)
    c = pyperclip.paste()
    return c


def ctrl_v():
    keyboard.press_and_release('ctrl + v')
    time.sleep(0.1)


def replace_name(s='80 MSK ulanova katya', num=0):
    s = re.sub(r'[_\s]+', ' ', s)
    s = s.strip()
    s = s.lower()
    l = ['vm_minsk', 'msk', 'minsk', 'kz']
    k = 'msk'
    for w in l:
        if w in s:
            k = w
            break

    s = re.sub(r'\d+', '', s)
    s = re.sub(k, '', s)
    s = re.sub(r'\s+', ' ', s)
    s = s.strip()
    s = f'{k} {num} {s}'
    l = s.split(' ')
    l = [w.capitalize() for w in l]
    s = '_'.join(l)
    # '80_Msk_Ulanova_Katya'
    return s


def main(window_name):
    wait_windows(window_name, timeout=10)
    time.sleep(0.5)

    pyperclip.copy('')

    keyboard.press_and_release('enter')
    time.sleep(time_sleep)

    num_peer = re.findall(r'\d+', ctrlc())[0]

    keyboard.press_and_release('shift + tab')
    time.sleep(time_sleep)
    name = re.sub('[\s\+]+$', '', ctrlc())

    time.sleep(time_sleep)
    keyboard.write(replace_name(s=name, num=num_peer))

    keyboard.press_and_release('enter')
    time.sleep(time_sleep)

    print(num_peer)

    keyboard.press_and_release('down')
    return


if __name__ == '__main__':
    replace_name()
    print(pg.getAllTitles())
    window_name = '192.168.11.1:48291'
    for i in range(38):
        main(window_name=window_name)

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
