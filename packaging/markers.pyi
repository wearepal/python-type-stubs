from typing import Any, Callable, Dict, Optional

Operator = Callable[[str, str], bool]

class InvalidMarker(ValueError): ...
class UndefinedComparison(ValueError): ...
class UndefinedEnvironmentName(ValueError): ...

class Node:
    value: Any = ...
    def __init__(self, value: Any) -> None: ...
    def serialize(self) -> str: ...

class Variable(Node):
    def serialize(self) -> str: ...

class Value(Node):
    def serialize(self) -> str: ...

class Op(Node):
    def serialize(self) -> str: ...

class Undefined: ...

def default_environment() -> Dict[str, str]: ...

class Marker:
    def __init__(self, marker: str) -> None: ...
    def evaluate(self, environment: Optional[Dict[str, str]]=...) -> bool: ...
