from dataclasses import dataclass


@dataclass
class Note:
    name: str
    comment: str
    id: int | None = None