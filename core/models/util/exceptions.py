#NAME SIDE
class CoordNotFound(ValueError):
    """Raised when the coord need more numbers"""
    def __init__(self, foo, *args: object) -> None:
        self.message = f"Need one or more coords ({foo}, {len(foo)})"
        self.foo = foo

        super().__init__(self.message, *args)

class CoordExced(ValueError):
    """Raised when some coord is out of the limit"""
    def __init__(self, foo, local, *args: object) -> None:
        self.message = f"One or more coords are of the limit ({foo}, limit: {local})"
        self.foo = foo
        self.local = local
        
        super().__init__(self.message, *args)


class VectorIncorrect(TypeError):
    """Raised when the vector is not a list"""
    def __init__(self, foo, *args: object) -> None:
        self.message = f"Need a list, not {type(foo)}"
        self.foo = foo
        
        super().__init__(self.message, *args)
        