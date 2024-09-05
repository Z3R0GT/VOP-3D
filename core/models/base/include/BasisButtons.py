from .BasisUI import MARK_SCAPE, BasisUI
from ..tools.ScreenTools import *


class BasisButtons(BasisUI):

    def __func__(self, func):
        self.action = func

    def _input_(self, msg:tuple[str]):
        self._in_ = []

        if not len(msg) == 0:
            if not msg[0] == "":
                if not type(msg) == type(""):
                    for text in msg:
                        self._in_.append(input(f"{text}{MARK_SCAPE}"))
                else:
                    self._in_.append(input(f"{msg}{MARK_SCAPE}"))
        self.action(self._in_, self.var)

    def execute(self, *arg):
        self.action(arg, self.var)