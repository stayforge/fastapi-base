"""Helper utility functions."""

import re
from typing import Any, Dict


def to_camel_case(snake_str: str) -> str:
    """Convert snake_case to camelCase."""
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def to_snake_case(camel_str: str) -> str:
    """Convert camelCase to snake_case."""
    return re.sub(r"(?<!^)(?=[A-Z])", "_", camel_str).lower()


def dict_to_camel_case(data: Dict[str, Any]) -> Dict[str, Any]:
    """Convert all keys in a dictionary from snake_case to camelCase."""
    return {to_camel_case(key): value for key, value in data.items()}


def dict_to_snake_case(data: Dict[str, Any]) -> Dict[str, Any]:
    """Convert all keys in a dictionary from camelCase to snake_case."""
    return {to_snake_case(key): value for key, value in data.items()}

