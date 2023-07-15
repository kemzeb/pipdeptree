from __future__ import annotations

import sys
from typing import NoReturn

from pipdeptree._models import guess_version

if sys.version_info >= (3, 8):
    import importlib.metadata as importlib_metadata
else:
    import importlib_metadata


def raise_import_error(name: str) -> NoReturn:
    raise ImportError(name)


importlib_metadata.version = raise_import_error  # type: ignore[assignment]
print(guess_version("setuptools"), end="")  # noqa: T201