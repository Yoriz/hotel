from dataclasses import dataclass, field
from enum import Enum, auto
from types import MethodType
from typing import Callable, ClassVar, Hashable, NamedTuple
from uuid import uuid4
from weakref import WeakValueDictionary


class EventTypeSignature(NamedTuple):
    event_type: Hashable
    signature: str = ""


class ChannelEnum(Enum):
    DEFAULT = uuid4()


@dataclass
class Callables:
    _callables: WeakValueDictionary = field(
        default_factory=WeakValueDictionary, init=False, repr=False
    )

    def add_callable(self, callable: Callable) -> None:
        if isinstance(callable, MethodType):
            self._callables[
                (id(callable.__self__), callable.__func__.__name__)
            ] = callable.__self__
        else:
            self._callables[(id(callable), None)] = callable
        return None

    def call_all(self, *args, **kwargs):
        for key, value in self._callables.items():
            _, name = key
            callable = value if not name else getattr(value, name)
            callable(*args, **kwargs)
        return None

    def remove_callable(self, callable: Callable) -> None:
        if isinstance(callable, MethodType):
            key = (id(callable.__self__), callable.__func__.__name__)
        else:
            key = (id(callable), None)
        try:
            del self._callables[key]
        except KeyError:
            pass
        return None

    def remove_all_callables(self) -> None:
        self._callables.clear()
        return None

    @property
    def has_callables(self) -> bool:
        return bool(self._callables)


@dataclass
class Event:
    _events: dict[Hashable, Callables] = field(default_factory=dict, init=False)

    def bind(self, event_type: Hashable, callable: Callable) -> None:
        if not event_type in self._events:
            self._events[event_type] = Callables()
        self._events[event_type].add_callable(callable)

    def notify(self, event_type: Hashable, *args, **kwargs):
        callables = self._events.get(event_type)
        if not callables:
            return
        if callables.has_callables:
            callables.call_all(*args, **kwargs)
        else:
            del self._events[event_type]


@dataclass
class Events:
    channel: Hashable = ChannelEnum.DEFAULT
    channels: ClassVar[dict[Hashable, Event]] = {}

    def __post_init__(self):
        if not self.channels.get(self.channel):
            self.channels[self.channel] = Event()

    def change_channel(self, channel: Hashable) -> None:
        if not self.channels.get(self.channel):
            self.channels[self.channel] = Event()
        self.channel = channel
        return None

    def bind(self, event_type: Hashable, callable: Callable) -> None:
        self.channels[self.channel].bind(event_type=event_type, callable=callable)

    def notify(self, event_type: Hashable, *args, **kwargs):
        self.channels[self.channel].notify(event_type=event_type, *args, **kwargs)


def main():
    import inspect
    from typing import get_type_hints

    class EventEnum(Enum):
        EVENT1 = auto()
        EVENT2 = auto()

    @dataclass
    class EventMessage:
        customer: str

    def func1(event_message: EventMessage):
        print(event_message)

    def func2():
        print("func2")

    @dataclass
    class Test:
        name: str

        def test_func1(self, event_message: EventMessage):
            print(f"From {self.name}: {event_message}")

        def test_print(self, this: str, that):
            print("test_print")

        def test_signature(self, *args, **kwargs):
            print(args)
            print(kwargs)

    test = Test("Test1")
    test2 = Test("Test2")

    event1 = Event()
    event1.bind(EventEnum.EVENT1, func1)
    event1.notify(EventEnum.EVENT1, event_message=EventMessage(customer="Success"))
    main_events = Events()
    main_events.bind(event_type=EventEnum.EVENT1, callable=func1)
    main_events.notify(
        event_type=EventEnum.EVENT1,
        event_message=EventMessage(customer="Success events"),
    )
    main_events.bind(event_type=EventEnum.EVENT2, callable=test.test_func1)
    main_events.bind(event_type=EventEnum.EVENT2, callable=test2.test_func1)
    main_events.notify(
        event_type=EventEnum.EVENT2,
        event_message=EventMessage(customer="Success events"),
    )
    hints = get_type_hints(test.test_func1)
    print(hints)
    signature = inspect.signature(test.test_func1)
    print(signature)
    test.test_signature(
        this="this", event_message=EventMessage(customer="Success events")
    )


if __name__ == "__main__":
    main()
