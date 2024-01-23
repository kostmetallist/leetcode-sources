from dataclasses import dataclass
from typing import Self


@dataclass
class Node:
    val: int = None
    children: [Self] = None
