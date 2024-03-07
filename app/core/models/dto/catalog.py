from dataclasses import dataclass


@dataclass
class Catalog:
    name: str
    id: int | None = None