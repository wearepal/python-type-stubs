from .after import after_log as after_log
from .before import before_log as before_log
from .before_sleep import before_sleep_log as before_sleep_log, before_sleep_nothing as before_sleep_nothing
from .nap import sleep_using_event as sleep_using_event
from .retry import retry_all as retry_all, retry_always as retry_always, retry_any as retry_any, retry_if_exception as retry_if_exception, retry_if_exception_message as retry_if_exception_message, retry_if_not_exception_message as retry_if_not_exception_message, retry_if_not_result as retry_if_not_result, retry_if_result as retry_if_result, retry_never as retry_never, retry_unless_exception_type as retry_unless_exception_type
from .stop import stop_after_attempt as stop_after_attempt, stop_after_delay as stop_after_delay, stop_all as stop_all, stop_any as stop_any, stop_when_event_set as stop_when_event_set
from .wait import wait_chain as wait_chain, wait_combine as wait_combine, wait_exponential as wait_exponential, wait_fixed as wait_fixed, wait_incrementing as wait_incrementing, wait_random as wait_random, wait_random_exponential as wait_random_exponential
from concurrent import futures
from tenacity._asyncio import AsyncRetrying as AsyncRetrying
from tenacity.tornadoweb import TornadoRetrying as TornadoRetrying
from typing import Any, Optional

WrappedFn: Any

def retry(fn: WrappedFn) -> WrappedFn: ...

class TryAgain(Exception): ...

NO_RESULT: Any

class DoAttempt: ...
class DoSleep(float): ...

class BaseAction:
    REPR_FIELDS: Any = ...
    NAME: Any = ...

class RetryAction(BaseAction):
    REPR_FIELDS: Any = ...
    NAME: str = ...
    sleep: Any = ...
    def __init__(self, sleep: Any) -> None: ...

class RetryError(Exception):
    last_attempt: Any = ...
    def __init__(self, last_attempt: Any) -> None: ...
    def reraise(self) -> None: ...

class AttemptManager:
    retry_state: Any = ...
    def __init__(self, retry_state: Any) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any): ...

class BaseRetrying:
    sleep: Any = ...
    reraise: Any = ...
    retry_error_cls: Any = ...
    fn: Any = ...
    def __init__(self, sleep: Any = ..., stop: Any = ..., wait: Any = ..., retry: Any = ..., before: Any = ..., after: Any = ..., before_sleep: Optional[Any] = ..., reraise: bool = ..., retry_error_cls: Any = ..., retry_error_callback: Optional[Any] = ...) -> None: ...
    def stop(self): ...
    def wait(self): ...
    def retry(self): ...
    def before(self): ...
    def after(self): ...
    def before_sleep(self): ...
    def retry_error_callback(self): ...
    def copy(self, sleep: Any = ..., stop: Any = ..., wait: Any = ..., retry: Any = ..., before: Any = ..., after: Any = ..., before_sleep: Any = ..., reraise: Any = ...): ...
    @property
    def statistics(self): ...
    def wraps(self, f: Any): ...
    def begin(self, fn: Any) -> None: ...
    def iter(self, retry_state: Any): ...
    def __iter__(self) -> Any: ...

class Retrying(BaseRetrying):
    def call(self, fn: Any, *args: Any, **kwargs: Any): ...
    __call__: Any = ...

class Future(futures.Future):
    attempt_number: Any = ...
    def __init__(self, attempt_number: Any) -> None: ...
    @property
    def failed(self): ...
    @classmethod
    def construct(cls, attempt_number: Any, value: Any, has_exception: Any): ...

class RetryCallState:
    start_time: Any = ...
    retry_object: Any = ...
    fn: Any = ...
    args: Any = ...
    kwargs: Any = ...
    attempt_number: int = ...
    outcome: Any = ...
    outcome_timestamp: Any = ...
    idle_for: int = ...
    next_action: Any = ...
    def __init__(self, retry_object: Any, fn: Any, args: Any, kwargs: Any) -> None: ...
    @property
    def seconds_since_start(self): ...
    def prepare_for_next_attempt(self) -> None: ...
    def set_result(self, val: Any) -> None: ...
    def set_exception(self, exc_info: Any) -> None: ...
