from typing import Any, Dict, Iterable
from .doc import Doc
from .span import Span

class SpanGroup:
    name: str
    attrs: Dict[str, Any]
    def __init__(
        self,
        doc: Doc,
        *,
        name: str = ...,
        attrs: Dict[str, Any] = ...,
        spans: Iterable[Span] = ...
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def doc(self) -> Doc: ...
    @property
    def has_overlap(self) -> bool: ...
    def __len__(self) -> int: ...
    def append(self, span: Span) -> None: ...
    def extend(self, spans: Iterable[Span]) -> None: ...
    def __getitem__(self, i: int) -> Span: ...
    def to_bytes(self) -> bytes: ...
    def from_bytes(self, bytes_data: bytes) -> SpanGroup: ...
    def copy(self) -> SpanGroup: ...
