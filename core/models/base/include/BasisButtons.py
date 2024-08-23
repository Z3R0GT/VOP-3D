from .BasisUI import *
from ..tools.ScreenTools import *

MARK_SCAPE = "\n>  "

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
        print(self._in_, self.var)
        input()
        self.action(self._in_, self.var)

    def execute(self, arg):
        self.action(arg, self.var)