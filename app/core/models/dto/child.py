from dataclasses import dataclass


@dataclass
class Child:
    parent_id: int
    name: str
    image_url: str
    id: int | None = None