import tkinter as tk

class InputField:
    def __init__(self, master, switch_button: tk.Button):
        self._master = master
        self._button = switch_button
        self._button.configure(command=self.__switch)
        self._mode_alt = False
        self._is_init = False
        self._fields = 1

    def activate(self, buffers: list):
        self._is_init = True
        self._mode_alt = False
        self._button.configure(fg="black")
    
    def _activate_alt(self, buffers: list):
        self._is_init = True
        self._mode_alt = True
        self._button.configure(fg="green")

    def collapse(self):
        self._collapse_alt()
        self._collapse_text()
        self._is_init = False

    def _collapse_text(self) -> bool:
        if self._is_init and not self._mode_alt:
            self._is_init = False
            return True
        return False

    def _collapse_alt(self):
        if self._is_init and self._mode_alt:
            self._is_init = False
            return True
        return False
    
    def read(self, field: int = 0) -> str:
        if self._mode_alt:
            return self._read_alt(field)
        return self._read_text(field)

    def _read_text(self, field: int = 0) -> str:
        pass

    def _read_alt(self, field: int = 0) -> str:
        pass

    def __switch(self):
        buffers = [self.read(field) for field in range(self._fields)]
        self.collapse()
        if self._mode_alt:
            self.activate(buffers)
        else:
            self._activate_alt(buffers)