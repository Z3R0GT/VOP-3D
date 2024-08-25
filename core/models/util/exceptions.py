#NAME SIDE
class CoordNotFound(ValueError):
    """Raised when the coord need more numbers"""
    def __init__(self, foo, *args: object) -> None:
        self.message = f"Need one or more coords ({foo}, {len(foo)})"
        self.foo = foo

        super().__init__(self.message, *args)


class CoordInConflic(ValueError):
    """Raised when the coord is colision with another"""
    def __init__(self, foo, *args: object) -> None:
        self.message = f"The node is in conlict from {foo.name} with {args[0].name} ({foo.vec}, {args[0].vec})"
        self.foo = foo
        #del args
        super().__init__(self.message)


class CoordExced(ValueError):
    """Raised when some coord is out of the limit"""
    def __init__(self, foo, local, *args: object) -> None:
        self.message = f"One or more coords are of the limit ({foo}, limit: {local})"
        self.foo = foo
        self.local = local
        
        super().__init__(self.message, *args)


class IncorrectVector(TypeError):
    """Raised when the vector is not a list"""
    def __init__(self, foo, *args: object) -> None:
        self.message = f"Need a list, not {type(foo)}"
        self.foo = foo
        
        super().__init__(self.message, *args)
 

class IncorrectTypeNode(TypeError):
    """Raised when a node isn't correct"""
    def __init__(self, foo, *args: object) -> None:
        self.message = f"The object is {type(foo)} ({foo.name}) is not compatible"
        self.foo = foo
        
        super().__init__(self.message, *args)


class IsNotAChild(AttributeError):
    """Raised when a node isn't a child"""
    def __init__(self, foo, *args: object) -> None:
        self.message = f"The object {foo.name} isn't a child or cannot be a child"
        self.foo = foo
        
        super().__init__(self.message, *args)


class IsNotAFather(AttributeError):
    """Raised when a node isn't a father"""
    def __init__(self, foo, *args: object) -> None:
        self.message = f"The object {foo.name} isn't a father or cannot be a father"
        self.foo = foo
        
        super().__init__(self.message, *args)
