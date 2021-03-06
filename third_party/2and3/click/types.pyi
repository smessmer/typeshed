from typing import Any, Callable, IO, Iterable, List, Optional, Text, TypeVar, Union
import uuid

from click.core import Context, Parameter


class ParamType:
    name: Text
    is_composite: bool
    envvar_list_splitter: Optional[Text]

    def __call__(
        self,
        value: Optional[Text],
        param: Optional[Parameter] = ...,
        ctx: Optional[Context] = ...,
    ) -> Any:
        ...

    def get_metavar(self, param: Parameter) -> Text:
        ...

    def get_missing_message(self, param: Parameter) -> Text:
        ...

    def convert(
        self,
        value: Text,
        param: Optional[Parameter],
        ctx: Optional[Context],
    ) -> Any:
        ...

    def split_envvar_value(self, rv: Text) -> List[Text]:
        ...

    def fail(self, message: Text, param: Optional[Parameter] = ..., ctx: Optional[Context] = ...) -> None:
        ...


class BoolParamType(ParamType):
    def __call__(
        self,
        value: Optional[Text],
        param: Optional[Parameter] = ...,
        ctx: Optional[Context] = ...,
    ) -> bool:
        ...

    def convert(
        self,
        value: Text,
        param: Optional[Parameter],
        ctx: Optional[Context],
    ) -> bool:
        ...


class CompositeParamType(ParamType):
    arity: int


class Choice(ParamType):
    choices: Iterable[Text]
    def __init__(self, choices: Iterable[Text]) -> None:
        ...


class FloatParamType(ParamType):
    def __call__(
        self,
        value: Optional[Text],
        param: Optional[Parameter] = ...,
        ctx: Optional[Context] = ...,
    ) -> float:
        ...

    def convert(
        self,
        value: Text,
        param: Optional[Parameter],
        ctx: Optional[Context],
    ) -> float:
        ...


class FloatRange(FloatParamType):
    ...


class File(ParamType):
    def __init__(
        self,
        mode: Text = ...,
        encoding: Optional[Text] = ...,
        errors: Optional[Text] = ...,
        lazy: Optional[bool] = ...,
        atomic: Optional[bool] = ...,
    ) -> None:
        ...

    def __call__(
        self,
        value: Optional[Text],
        param: Optional[Parameter] = ...,
        ctx: Optional[Context] = ...,
    ) -> IO:
        ...

    def convert(
        self,
        value: Text,
        param: Optional[Parameter],
        ctx: Optional[Context],
    ) -> IO:
        ...

    def resolve_lazy_flag(self, value: Text) -> bool:
        ...


_F = TypeVar('_F')  # result of the function
_Func = Callable[[Optional[Text]], _F]


class FuncParamType(ParamType):
    func: _Func

    def __init__(self, func: _Func) -> None:
        ...

    def __call__(
        self,
        value: Optional[Text],
        param: Optional[Parameter] = ...,
        ctx: Optional[Context] = ...,
    ) -> _F:
        ...

    def convert(
        self,
        value: Text,
        param: Optional[Parameter],
        ctx: Optional[Context],
    ) -> _F:
        ...


class IntParamType(ParamType):
    def __call__(
        self,
        value: Optional[Text],
        param: Optional[Parameter] = ...,
        ctx: Optional[Context] = ...,
    ) -> int:
        ...

    def convert(
        self,
        value: Text,
        param: Optional[Parameter],
        ctx: Optional[Context],
    ) -> int:
        ...


class IntRange(IntParamType):
    def __init__(
        self, min: Optional[int] = ..., max: Optional[int] = ..., clamp: bool = ...
    ) -> None:
        ...


_PathType = TypeVar('_PathType', Text, bytes)


class Path(ParamType):
    def __init__(
        self,
        exists: bool = ...,
        file_okay: bool = ...,
        dir_okay: bool = ...,
        writable: bool = ...,
        readable: bool = ...,
        resolve_path: bool = ...,
        allow_dash: bool = ...,
        path_type: Optional[_PathType] = ...,
    ) -> None:
        ...

    def coerce_path_result(self, rv: Union[Text, bytes]) -> _PathType:
        ...

    def __call__(
        self,
        value: Optional[Text],
        param: Optional[Parameter] = ...,
        ctx: Optional[Context] = ...,
    ) -> _PathType:
        ...

    def convert(
        self,
        value: Text,
        param: Optional[Parameter],
        ctx: Optional[Context],
    ) -> _PathType:
        ...

class StringParamType(ParamType):
    def __call__(
        self,
        value: Optional[Text],
        param: Optional[Parameter] = ...,
        ctx: Optional[Context] = ...,
    ) -> Text:
        ...

    def convert(
        self,
        value: Text,
        param: Optional[Parameter],
        ctx: Optional[Context],
    ) -> Text:
        ...


class Tuple(CompositeParamType):
    types: List[ParamType]

    def __init__(self, types: Iterable[Any]) -> None:
        ...

    def __call__(
        self,
        value: Optional[Text],
        param: Optional[Parameter] = ...,
        ctx: Optional[Context] = ...,
    ) -> Tuple:
        ...

    def convert(
        self,
        value: Text,
        param: Optional[Parameter],
        ctx: Optional[Context],
    ) -> Tuple:
        ...


class UnprocessedParamType(ParamType):
    ...


class UUIDParameterType(ParamType):
    def __call__(
        self,
        value: Optional[Text],
        param: Optional[Parameter] = ...,
        ctx: Optional[Context] = ...,
    ) -> uuid.UUID:
        ...

    def convert(
        self,
        value: Text,
        param: Optional[Parameter],
        ctx: Optional[Context],
    ) -> uuid.UUID:
        ...


def convert_type(ty: Any, default: Optional[Any] = ...) -> ParamType:
    ...

# parameter type shortcuts

BOOL = BoolParamType()
FLOAT = FloatParamType()
INT = IntParamType()
STRING = StringParamType()
UNPROCESSED = UnprocessedParamType()
UUID = UUIDParameterType()
