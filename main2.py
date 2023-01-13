#!/bin/python3
# -*- coding: utf-8 -*-

import gi  # noqa
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk  # noqa

# PROJECT_PATH: str = "/home/app/Projects/dhobconv/"
PROJECT_PATH: str = "D:\\home\\projects\\gtk-dhobconv\\"
MAIN_WINDOW: str = "main_window2.glade"
BINARY_CHARS: tuple = ('0', '1')
DECIMAL_CHARS: tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
HEXADECIMAL_CHARS: tuple = ('0', '1', '2', '3', '4', '5', '6', '7',
                            '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
OCTAL_CHARS: tuple = ('0', '1', '2', '3', '4', '5', '6', '7')
ICON_POSITION = Gtk.EntryIconPosition.SECONDARY
ICON_OK: str = "object-select-symbolic"
ICON_ERROR: str = "process-stop-symbolic"


def check_entered_string(pset: tuple, pwidget) -> bool:
    """Проверяет введённую строку на корректность."""
    result: bool = True
    line: str = pwidget.get_text().upper()
    for char in line:

        if char not in pset:

            result = False
            break
    return result


class CApplication:

    def __init__(self):
        """Конструктор."""
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        self.builder = Gtk.Builder()
        self.builder.add_from_file(PROJECT_PATH + MAIN_WINDOW)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("main_window")
        # *** Строки ввода
        self.dec_entry = self.builder.get_object("dec_entry")
        self.dec_entry.set_icon_from_icon_name(ICON_POSITION, ICON_OK)
        self.hex_entry = self.builder.get_object("hex_entry")
        self.hex_entry.set_icon_from_icon_name(ICON_POSITION, ICON_OK)
        self.oct_entry = self.builder.get_object("oct_entry")
        self.oct_entry.set_icon_from_icon_name(ICON_POSITION, ICON_OK)
        self.bin_entry = self.builder.get_object("bin_entry")
        self.bin_entry.set_icon_from_icon_name(ICON_POSITION, ICON_OK)
        # *** Кнопки
        self.copy_bin_button = self.builder.get_object("copy_bin_button")
        self.copy_bin_button.set_sensitive(True)
        self.copy_dec_button = self.builder.get_object("copy_dec_button")
        self.copy_dec_button.set_sensitive(True)
        self.copy_hex_button = self.builder.get_object("copy_hex_button")
        self.copy_hex_button.set_sensitive(True)
        self.copy_oct_button = self.builder.get_object("copy_oct_button")
        self.copy_oct_button.set_sensitive(True)

        self.window.show_all()

    def bin_entry_changed(self, pwidget):
        """Обработчик ввода двоичного числа."""
        if check_entered_string(BINARY_CHARS, pwidget):

            pwidget.set_icon_from_icon_name(ICON_POSITION, ICON_OK)
            self.copy_bin_button.set_sensitive(True)
            line: str = pwidget.get_text().strip()
            # *** Что-то ввели?
            if len(line) > 0:

                # *** Приведем строку к инт и конвертим
                value: int = int(line, 2)
                self.dec_entry.set_text(str(value))

            else:

                self.dec_entry.set_text("")
                self.hex_entry.set_text("")
                self.oct_entry.set_text("")
        else:

            pwidget.set_icon_from_icon_name(ICON_POSITION, ICON_ERROR)
            self.copy_bin_button.set_sensitive(False)
            self.dec_entry.set_text("")
            self.hex_entry.set_text("")
            self.oct_entry.set_text("")

    def clear_entries(self):
        """Очищает все строки ввода."""

        self.dec_entry.set_text("")
        self.hex_entry.set_text("")
        self.oct_entry.set_text("")
        self.bin_entry.set_text("")

    def copy_bin_button_clicked(self, pwidget):
        """Обработчик нажатия кнопки копирования в буфер двоичного значения."""

        self.clipboard.set_text(self.bin_entry.get_text(), -1)

    def copy_dec_button_clicked(self, pwidget):
        """Обработчик нажатия кнопки копирования в буфер десятичного значения."""

        self.clipboard.set_text(self.dec_entry.get_text(), -1)

    def copy_hex_button_clicked(self, pwidget):
        """Обработчик нажатия кнопки копирования в буфер шестнадцатиричного значения."""

        self.clipboard.set_text(self.hex_entry.get_text(), -1)

    def copy_oct_button_clicked(self, pwidget):
        """Обработчик нажатия кнопки копирования в буфер восьмеричного значения."""

        self.clipboard.set_text(self.oct_entry.get_text(), -1)

    def dec_entry_changed(self, pwidget):
        """Обработчик ввода десятичного числа."""
        if check_entered_string(DECIMAL_CHARS, pwidget):

            pwidget.set_icon_from_icon_name(ICON_POSITION, ICON_OK)
            self.copy_dec_button.set_sensitive(True)

            line: str = pwidget.get_text().strip()
            # *** Что-то ввели?
            if len(line) > 0:

                # *** Приведем строку к инт и конвертим
                value: int = int(line)
                self.bin_entry.set_text(bin(value)[2:])
                self.hex_entry.set_text(hex(value)[2:])
                self.oct_entry.set_text(oct(value)[2:])

            else:

                self.bin_entry.set_text("")
                self.hex_entry.set_text("")
                self.oct_entry.set_text("")
        else:

            pwidget.set_icon_from_icon_name(ICON_POSITION, ICON_ERROR)
            self.copy_dec_button.set_sensitive(False)
            self.bin_entry.set_text("")
            self.hex_entry.set_text("")
            self.oct_entry.set_text("")

    def hex_entry_changed(self, pwidget):
        """Обработчик ввода шестнадцатиричного числа."""
        if check_entered_string(HEXADECIMAL_CHARS, pwidget):

            pwidget.set_icon_from_icon_name(ICON_POSITION, ICON_OK)
            self.copy_hex_button.set_sensitive(True)
            line: str = pwidget.get_text().strip()
            # *** Что-то ввели?
            if len(line) > 0:

                # *** Приведем строку к инт и конвертим
                value: int = int(line, 16)
                self.dec_entry.set_text(str(value))
            else:

                self.bin_entry.set_text("")
                self.dec_entry.set_text("")
                self.oct_entry.set_text("")
        else:

            pwidget.set_icon_from_icon_name(ICON_POSITION, ICON_ERROR)
            self.copy_hex_button.set_sensitive(False)
            self.bin_entry.set_text("")
            self.dec_entry.set_text("")
            self.oct_entry.set_text("")

    def oct_entry_changed(self, pwidget):
        """Обработчик ввода восьмеричного числа."""
        if check_entered_string(OCTAL_CHARS, pwidget):

            pwidget.set_icon_from_icon_name(ICON_POSITION, ICON_OK)
            self.copy_oct_button.set_sensitive(True)
            line: str = pwidget.get_text().strip()
            # *** Что-то ввели?
            if len(line) > 0:

                # *** Приведем строку к инт и конвертим
                value: int = int(line, 8)
                self.dec_entry.set_text(str(value))
            else:

                self.bin_entry.set_text("")
                self.dec_entry.set_text("")
                self.hex_entry.set_text("")
        else:

            pwidget.set_icon_from_icon_name(ICON_POSITION, ICON_ERROR)
            self.copy_oct_button.set_sensitive(False)
            self.bin_entry.set_text("")
            self.dec_entry.set_text("")
            self.hex_entry.set_text("")

    @staticmethod
    def on_destroy(self):
        """Обработчик нажатия кнопки закрытия программы."""
        Gtk.main_quit()


if __name__ == '__main__':
    app = CApplication()
    Gtk.main()
