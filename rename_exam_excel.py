import re
import time

import keyboard
import pyperclip

time_sleep = 0.2


def replace_string(s: str) -> str:
    separator_char = (',', '.', '?', ';', ':', '…')
    s = s.strip()
    rows = s.split('\n')
    out = ''
    for row in rows:
        row = row.strip()

        try:
            if row == '"':
                raise IndexError
            _row_begin_quotation_marks = False
            _row_end_quotation_marks = False

            if row[0] == '"':
                _row_begin_quotation_marks = True
                row = row[1:]

            if row[-1] == '"':
                _row_end_quotation_marks = True
                row = row[:-1]

            for char in separator_char:
                row = row.replace(char, f'{char} ')

            row = f'{row[0].upper()}{row[1:]}'
            row = row.strip()
            if row[-1] not in separator_char:
                row = f'{row}.'

            row = re.sub(r' +', ' ', row)
            for char in separator_char:
                row = row.replace(f' {char}', char)
            row = re.sub(r' +', ' ', row)
            row = row.strip()
            if _row_end_quotation_marks:
                row = f'{row}"'
            if _row_begin_quotation_marks:
                row = f'"{row}'
        except IndexError:
            out += ''
        out += f'{row}\n'

    return out.strip()


def main():
    pyperclip.copy('')
    while True:
        p = pyperclip.paste()
        time.sleep(time_sleep)
        if p != '':
            s = replace_string(p)
            if p != s:
                pyperclip.copy(s)
                time.sleep(0.2)
                p = pyperclip.paste()
                if p == s:
                    keyboard.press_and_release('ctrl + v')


if __name__ == '__main__':
    main()

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
