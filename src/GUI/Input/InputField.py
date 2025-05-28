import tkinter as tk


class InputField:
    """An abstract class for objects that handle switching between text and table input modes"""

    def __init__(self, master, switch_button: tk.Button):
        """basic setup, automatically configure the button"""
        self._master = master
        self._button = switch_button
        self._button.configure(command=self.__switch)
        self._mode_alt = False
        self._is_init = False
        self._fields = 1

    def activate(self, buffers: list[str]):
        """basic logic for activation of text input"""
        self._is_init = True
        self._mode_alt = False
        self._button.configure(fg="black")

    def _activate_alt(self, buffers: list):
        """basic logic for activation of table input"""
        self._is_init = True
        self._mode_alt = True
        self._button.configure(fg="green")

    def collapse(self):
        """collapses all input fields"""
        self._collapse_alt()
        self._collapse_text()
        self._is_init = False

    def _collapse_text(self) -> bool:
        """basic logic for collapsing text input
        Returns:
            (bool): whether there is something to collapse"""
        if self._is_init and not self._mode_alt:
            self._is_init = False
            return True
        return False

    def _collapse_alt(self) -> bool:
        """basic logic for collapsing table input
        Returns:
            (bool): whether there is something to collapse"""
        if self._is_init and self._mode_alt:
            self._is_init = False
            return True
        return False

    def read(self, field: int = 0) -> str:
        """returns the contents of the input field as text"""
        if self._mode_alt:
            return self._read_alt(field)
        return self._read_text(field)

    def _read_text(self, field: int = 0) -> str:
        """fetches text from the text input"""
        pass

    def _read_alt(self, field: int = 0) -> str:
        """reads text from the table input"""
        pass

    def __switch(self):
        """the button calls this one to switch the input type"""
        buffers = [self.read(field) for field in range(self._fields)]
        self.collapse()
        if self._mode_alt:
            self.activate(buffers)
        else:
            self._activate_alt(buffers)
