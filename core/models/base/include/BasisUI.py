from .BasisViewport import *
from ..constant.BasisTracer import *
from ..constant.BasisSquare import *

from ..tools.ScreenTools import *

class BasisUI(BasisSquare, BasisViewPort):
    def __init__(self, name: str, id: int, abs: str, x:int, y:int, comment: str | None = None) -> None:
        super().__init__(name, id, abs, comment)
        super().__viewport__()
        super().__set_vec_2d__(x, y)

    def create_text(self,
                    text:str,
                    sector:Literal["CENTER", "UPPER", "LOWER", "CUSTOM"],
                    line:tuple[int, int]=...,
                    chk=True):
        checker_coord(line, self.vec)
        def __recursive__(ver:list[bool, int]):
            temp = []
            new  = ""
            checker_coord(ver, self.vec)
            for chr_per in range(len(text)-ver[1]-2, len(text)):
                temp.append(text[chr_per])

            for chr_all in range(len(temp)):
                new += temp[chr_all]

            self.create_text(new, [line[0], line[1]+1],sector, False)
            del new, temp, chr_per, chr_all

        self.__del_pre_view__()

        if sector == "CUSTOM":
            ver = self._edit_line_square_2d_([(line)], text)
            if ver[0]:
                __recursive__(ver)
        elif sector == "UPPER":
            if chk:
                line = (1,1)
            ver = self._edit_line_square_2d_([(line)], text)
        elif sector == "CENTER":
            if chk:
                line = (int(self.vec[0]/2)-5, int(self.vec[1]/2))
            ver = self._edit_line_square_2d_([(line)], text)
            if ver[0]:
                __recursive__(ver)
        elif sector == "LOWER":
            if chk:
                line = (1, self.vec[1]-2)
            ver = self._edit_line_square_2d_([(line)], text)
            if ver[0]:
                self.square[-2] = self._set_frame_square_2d_(self.vec, "last")
                __recursive__(ver)

        self.__set_pre_view__()