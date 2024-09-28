def _demo(*args, **kwargs):
    print("FUCK YOU, EASTER EGG FOUND >:D")

class Function:
    def __func__(self, func):
        self.var:dict  = {}
        if func == ...:
            self.action = _demo
        else:
            self.action = func
        
    def execute(self, *args):
        self.action(*args, **self.var)
        