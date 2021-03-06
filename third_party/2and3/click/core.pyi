from contextlib import contextmanager
from typing import (
    Any,
    Callable,
    Dict,
    Generator,
    Iterable,
    List,
    Mapping,
    Optional,
    Sequence,
    Set,
    Text,
    Tuple,
    TypeVar,
    Union,
)

from click.formatting import HelpFormatter
from click.parser import OptionParser


def invoke_param_callback(
    callback: Callable[['Context', 'Parameter', Optional[Text]], Any],
    ctx: 'Context',
    param: 'Parameter',
    value: Optional[Text]
) -> Any:
    ...


@contextmanager
def augment_usage_errors(
    ctx: 'Context', param: Optional['Parameter'] = ...
) -> Generator[None, None, None]:
    ...


def iter_params_for_processing(
    invocation_order: Sequence['Parameter'],
    declaration_order: Iterable['Parameter'],
) -> Iterable['Parameter']:
    ...


class Context:
    parent: Optional['Context']
    command: 'Command'
    info_name: Optional[Text]
    params: Dict
    args: List[Text]
    protected_args: List[Text]
    obj: Any
    default_map: Mapping[Text, Any]
    invoked_subcommand: Optional[Text]
    terminal_width: Optional[int]
    max_content_width: Optional[int]
    allow_extra_args: bool
    allow_interspersed_args: bool
    ignore_unknown_options: bool
    help_option_names: List[Text]
    token_normalize_func: Optional[Callable[[Text], Text]]
    resilient_parsing: bool
    auto_envvar_prefix: Optional[Text]
    color: Optional[bool]
    _meta: Dict[Text, Any]
    _close_callbacks: List
    _depth: int

    # properties
    meta: Dict[Text, Any]
    command_path: Text

    def __init__(
        self,
        command: 'Command',
        parent: Optional['Context'] = ...,
        info_name: Optional[Text] = ...,
        obj: Optional[Any] = ...,
        auto_envvar_prefix: Optional[Text] = ...,
        default_map: Optional[Mapping[Text, Any]] = ...,
        terminal_width: Optional[int] = ...,
        max_content_width: Optional[int] = ...,
        resilient_parsing: bool = ...,
        allow_extra_args: Optional[bool] = ...,
        allow_interspersed_args: Optional[bool] = ...,
        ignore_unknown_options: Optional[bool] = ...,
        help_option_names: Optional[List[Text]] = ...,
        token_normalize_func: Optional[Callable[[Text], Text]] = ...,
        color: Optional[bool] = ...
    ) -> None:
        ...

    @contextmanager
    def scope(self, cleanup: bool = ...) -> Generator['Context', None, None]:
        ...

    def make_formatter(self) -> HelpFormatter:
        ...

    def call_on_close(self, f: Callable) -> Callable:
        ...

    def close(self) -> None:
        ...

    def find_root(self) -> 'Context':
        ...

    def find_object(self, object_type: type) -> Any:
        ...

    def ensure_object(self, object_type: type) -> Any:
        ...

    def lookup_default(self, name: Text) -> Any:
        ...

    def fail(self, message: Text) -> None:
        ...

    def abort(self) -> None:
        ...

    def exit(self, code: Union[int, Text] = ...) -> None:
        ...

    def get_usage(self) -> Text:
        ...

    def get_help(self) -> Text:
        ...

    def invoke(
        self, callback: Union['Command', Callable], *args, **kwargs
    ) -> Any:
        ...

    def forward(
        self, callback: Union['Command', Callable], *args, **kwargs
    ) -> Any:
        ...

class BaseCommand:
    allow_extra_args: bool
    allow_interspersed_args: bool
    ignore_unknown_options: bool
    name: Text
    context_settings: Dict

    def __init__(self, name: Text, context_settings: Optional[Dict] = ...) -> None:
        ...

    def get_usage(self, ctx: Context) -> Text:
        ...

    def get_help(self, ctx: Context) -> Text:
        ...

    def make_context(
        self, info_name: Text, args: List[Text], parent: Optional[Context] = ..., **extra
    ) -> Context:
        ...

    def parse_args(self, ctx: Context, args: List[Text]) -> List[Text]:
        ...

    def invoke(self, ctx: Context) -> Any:
        ...

    def main(
        self,
        args: Optional[List[Text]] = ...,
        prog_name: Optional[Text] = ...,
        complete_var: Optional[Text] = ...,
        standalone_mode: bool = ...,
        **extra
    ) -> Any:
        ...

    def __call__(self, *args, **kwargs) -> Any:
        ...


class Command(BaseCommand):
    callback: Optional[Callable]
    params: List['Parameter']
    help: Optional[Text]
    epilog: Optional[Text]
    short_help: Optional[Text]
    options_metavar: Text
    add_help_option: bool

    def __init__(
        self,
        name: Text,
        context_settings: Optional[Dict] = ...,
        callback: Optional[Callable] = ...,
        params: Optional[List['Parameter']] = ...,
        help: Optional[Text] = ...,
        epilog: Optional[Text] = ...,
        short_help: Optional[Text] = ...,
        options_metavar: Text = ...,
        add_help_option: bool = ...
    ) -> None:
        ...

    def get_params(self, ctx: Context) -> List['Parameter']:
        ...

    def format_usage(
        self,
        ctx: Context,
        formatter: HelpFormatter
    ) -> None:
        ...

    def collect_usage_pieces(self, ctx: Context) -> List[Text]:
        ...

    def get_help_option_names(self, ctx: Context) -> Set[Text]:
        ...

    def get_help_option(self, ctx: Context) -> Optional['Option']:
        ...

    def make_parser(self, ctx: Context) -> OptionParser:
        ...

    def format_help(self, ctx: Context, formatter: HelpFormatter) -> None:
        ...

    def format_help_text(self, ctx: Context, formatter: HelpFormatter) -> None:
        ...

    def format_options(self, ctx: Context, formatter: HelpFormatter) -> None:
        ...

    def format_epilog(self, ctx: Context, formatter: HelpFormatter) -> None:
        ...


_T = TypeVar('_T')
_Decorator = Callable[[_T], _T]


class MultiCommand(Command):
    no_args_is_help: bool
    invoke_without_command: bool
    subcommand_metavar: Text
    chain: bool
    result_callback: Callable

    def __init__(
        self,
        name: Optional[Text] = ...,
        invoke_without_command: bool = ...,
        no_args_is_help: Optional[bool] = ...,
        subcommand_metavar: Optional[Text] = ...,
        chain: bool = ...,
        result_callback: Optional[Callable] = ...,
        **attrs
    ) -> None:
        ...

    def resultcallback(
        self, replace: bool = ...
    ) -> _Decorator:
        ...

    def format_commands(self, ctx: Context, formatter: HelpFormatter) -> None:
        ...

    def resolve_command(
        self, ctx: Context, args: List[Text]
    ) -> Tuple[Text, Command, List[Text]]:
        ...

    def get_command(self, ctx: Context, cmd_name: Text) -> Optional[Command]:
        ...

    def list_commands(self, ctx: Context) -> Iterable[Command]:
        ...


class Group(MultiCommand):
    commands: Dict[Text, Command]

    def __init__(
        self, name: Optional[Text] = ..., commands: Optional[Dict[Text, Command]] = ..., **attrs
    ) -> None:
        ...

    def add_command(self, cmd: Command, name: Optional[Text] = ...):
        ...

    def command(self, *args, **kwargs) -> _Decorator:
        ...

    def group(self, *args, **kwargs) -> _Decorator:
        ...


class CommandCollection(MultiCommand):
    sources: List[MultiCommand]

    def __init__(
        self, name: Optional[Text] = ..., sources: Optional[List[MultiCommand]] = ..., **attrs
    ) -> None:
        ...

    def add_source(self, multi_cmd: MultiCommand) -> None:
        ...


class Parameter:
    param_type_name: Text
    name: Text
    opts: List[Text]
    secondary_opts: List[Text]
    type: 'ParamType'
    required: bool
    callback: Optional[Callable[[Context, 'Parameter', Text], Any]]
    nargs: int
    multiple: bool
    expose_value: bool
    default: Any
    is_eager: bool
    metavar: Optional[Text]
    envvar: Union[Text, List[Text], None]
    # properties
    human_readable_name: Text

    def __init__(
        self,
        param_decls: Optional[List[Text]] = ...,
        type: Optional[Union[type, 'ParamType']] = ...,
        required: bool = ...,
        default: Optional[Any] = ...,
        callback: Optional[Callable[[Context, 'Parameter', Text], Any]] = ...,
        nargs: Optional[int] = ...,
        metavar: Optional[Text] = ...,
        expose_value: bool = ...,
        is_eager: bool = ...,
        envvar: Optional[Union[Text, List[Text]]] = ...
    ) -> None:
        ...

    def make_metavar(self) -> Text:
        ...

    def get_default(self, ctx: Context) -> Any:
        ...

    def add_to_parser(self, parser: OptionParser, ctx: Context) -> None:
        ...

    def consume_value(self, ctx: Context, opts: Dict[Text, Any]) -> Any:
        ...

    def type_cast_value(self, ctx: Context, value: Any) -> Any:
        ...

    def process_value(self, ctx: Context, value: Any) -> Any:
        ...

    def value_is_missing(self, value: Any) -> bool:
        ...

    def full_process_value(self, ctx: Context, value: Any) -> Any:
        ...

    def resolve_envvar_value(self, ctx: Context) -> Text:
        ...

    def value_from_envvar(self, ctx: Context) -> Union[Text, List[Text]]:
        ...

    def handle_parse_result(
        self, ctx: Context, opts: Dict[Text, Any], args: List[Text]
    ) -> Tuple[Any, List[Text]]:
        ...

    def get_help_record(self, ctx: Context) -> Tuple[Text, Text]:
        ...

    def get_usage_pieces(self, ctx: Context) -> List[Text]:
        ...


class Option(Parameter):
    prompt: Text  # sic
    confirmation_prompt: bool
    hide_input: bool
    is_flag: bool
    flag_value: Any
    is_bool_flag: bool
    count: bool
    multiple: bool
    allow_from_autoenv: bool
    help: Optional[Text]
    show_default: bool

    def __init__(
        self,
        param_decls: Optional[List[Text]] = ...,
        show_default: bool = ...,
        prompt: Union[bool, Text] = ...,
        confirmation_prompt: bool = ...,
        hide_input: bool = ...,
        is_flag: Optional[bool] = ...,
        flag_value: Optional[Any] = ...,
        multiple: bool = ...,
        count: bool = ...,
        allow_from_autoenv: bool = ...,
        type: Optional[Union[type, 'ParamType']] = ...,
        help: Optional[Text] = ...,
        **attrs
    ) -> None:
        ...

    def prompt_for_value(self, ctx: Context) -> Any:
        ...


class Argument(Parameter):
    def __init__(
        self,
        param_decls: Optional[List[Text]] = ...,
        required: Optional[bool] = ...,
        **attrs
    ) -> None:
        ...

# cyclic dependency
from click.types import ParamType  # noqa: E402
