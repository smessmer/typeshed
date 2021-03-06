from distutils.version import Version
from typing import Any, Callable, Dict, List, Optional, Text, Type, TypeVar, Union

from click.core import Command, Group, Argument, Option, Parameter, Context
from click.types import ParamType

_T = TypeVar('_T')
_Decorator = Callable[[_T], _T]

_Callback = Callable[
    [Context, Union[Option, Parameter], Union[bool, int, Text]],
    Any
]

def pass_context(_T) -> _T:
    ...


def pass_obj(_T) -> _T:
    ...


def make_pass_decorator(
    object_type: type, ensure: bool = ...
) -> Callable[[_T], _T]:
    ...


# NOTE: Decorators below have **attrs converted to concrete constructor
# arguments from core.pyi to help with type checking.

def command(
    name: Optional[Text] = ...,
    cls: Optional[Type[Command]] = ...,
    # Command
    context_settings: Optional[Dict] = ...,
    help: Optional[Text] = ...,
    epilog: Optional[Text] = ...,
    short_help: Optional[Text] = ...,
    options_metavar: Text = ...,
    add_help_option: bool = ...,
) -> _Decorator:
    ...


# This inherits attrs from Group, MultiCommand and Command.

def group(
    name: Optional[Text] = ...,
    cls: Type[Command] = ...,
    # Group
    commands: Optional[Dict[Text, Command]] = ...,
    # MultiCommand
    invoke_without_command: bool = ...,
    no_args_is_help: Optional[bool] = ...,
    subcommand_metavar: Optional[Text] = ...,
    chain: bool = ...,
    result_callback: Optional[Callable] = ...,
    # Command
    help: Optional[Text] = ...,
    epilog: Optional[Text] = ...,
    short_help: Optional[Text] = ...,
    options_metavar: Text = ...,
    add_help_option: bool = ...,
    # User-defined
    **kwargs: Any,
) -> _Decorator:
    ...


def argument(
    *param_decls: Text,
    cls: Type[Argument] = ...,
    # Argument
    required: Optional[bool] = ...,
    # Parameter
    type: Optional[Union[type, ParamType]] = ...,
    default: Optional[Any] = ...,
    callback: Optional[_Callback] = ...,
    nargs: Optional[int] = ...,
    metavar: Optional[Text] = ...,
    expose_value: bool = ...,
    is_eager: bool = ...,
    envvar: Optional[Union[Text, List[Text]]] = ...
) -> _Decorator:
    ...


def option(
    *param_decls: Text,
    cls: Type[Option] = ...,
    # Option
    show_default: bool = ...,
    prompt: Union[bool, Text] = ...,
    confirmation_prompt: bool = ...,
    hide_input: bool = ...,
    is_flag: Optional[bool] = ...,
    flag_value: Optional[Any] = ...,
    multiple: bool = ...,
    count: bool = ...,
    allow_from_autoenv: bool = ...,
    type: Optional[Union[type, ParamType]] = ...,
    help: Optional[Text] = ...,
    # Parameter
    default: Optional[Any] = ...,
    required: bool = ...,
    callback: Optional[_Callback] = ...,
    nargs: Optional[int] = ...,
    metavar: Optional[Text] = ...,
    expose_value: bool = ...,
    is_eager: bool = ...,
    envvar: Optional[Union[Text, List[Text]]] = ...
) -> _Decorator:
    ...


def confirmation_option(
    *param_decls: Text,
    cls: Type[Option] = ...,
    # Option
    show_default: bool = ...,
    prompt: Union[bool, Text] = ...,
    confirmation_prompt: bool = ...,
    hide_input: bool = ...,
    is_flag: bool = ...,
    flag_value: Optional[Any] = ...,
    multiple: bool = ...,
    count: bool = ...,
    allow_from_autoenv: bool = ...,
    type: Optional[Union[type, ParamType]] = ...,
    help: Text = ...,
    # Parameter
    default: Optional[Any] = ...,
    callback: Optional[_Callback] = ...,
    nargs: Optional[int] = ...,
    metavar: Optional[Text] = ...,
    expose_value: bool = ...,
    is_eager: bool = ...,
    envvar: Optional[Union[Text, List[Text]]] = ...
) -> _Decorator:
    ...


def password_option(
    *param_decls: Text,
    cls: Type[Option] = ...,
    # Option
    show_default: bool = ...,
    prompt: Union[bool, Text] = ...,
    confirmation_prompt: bool = ...,
    hide_input: bool = ...,
    is_flag: Optional[bool] = ...,
    flag_value: Optional[Any] = ...,
    multiple: bool = ...,
    count: bool = ...,
    allow_from_autoenv: bool = ...,
    type: Optional[Union[type, ParamType]] = ...,
    help: Optional[Text] = ...,
    # Parameter
    default: Optional[Any] = ...,
    callback: Optional[_Callback] = ...,
    nargs: Optional[int] = ...,
    metavar: Optional[Text] = ...,
    expose_value: bool = ...,
    is_eager: bool = ...,
    envvar: Optional[Union[Text, List[Text]]] = ...
) -> _Decorator:
    ...


def version_option(
    version: Optional[Union[Text, Version]] = ...,
    *param_decls: Text,
    cls: Type[Option] = ...,
    # Option
    prog_name: Optional[Text] = ...,
    message: Optional[Text] = ...,
    show_default: bool = ...,
    prompt: Union[bool, Text] = ...,
    confirmation_prompt: bool = ...,
    hide_input: bool = ...,
    is_flag: bool = ...,
    flag_value: Optional[Any] = ...,
    multiple: bool = ...,
    count: bool = ...,
    allow_from_autoenv: bool = ...,
    type: Optional[Union[type, ParamType]] = ...,
    help: Text = ...,
    # Parameter
    default: Optional[Any] = ...,
    callback: Optional[_Callback] = ...,
    nargs: Optional[int] = ...,
    metavar: Optional[Text] = ...,
    expose_value: bool = ...,
    is_eager: bool = ...,
    envvar: Optional[Union[Text, List[Text]]] = ...
) -> _Decorator:
    ...


def help_option(
    *param_decls: Text,
    cls: Type[Option] = ...,
    # Option
    show_default: bool = ...,
    prompt: Union[bool, Text] = ...,
    confirmation_prompt: bool = ...,
    hide_input: bool = ...,
    is_flag: bool = ...,
    flag_value: Optional[Any] = ...,
    multiple: bool = ...,
    count: bool = ...,
    allow_from_autoenv: bool = ...,
    type: Optional[Union[type, ParamType]] = ...,
    help: Text = ...,
    # Parameter
    default: Optional[Any] = ...,
    callback: Optional[_Callback] = ...,
    nargs: Optional[int] = ...,
    metavar: Optional[Text] = ...,
    expose_value: bool = ...,
    is_eager: bool = ...,
    envvar: Optional[Union[Text, List[Text]]] = ...
) -> _Decorator:
    ...
