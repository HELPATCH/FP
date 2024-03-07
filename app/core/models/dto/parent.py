from dataclasses import dataclass


@dataclass
class Parent:
    catalog_id: int
    name: str
    num: str
    id: int | None = None