# DO NOT EDIT! This file was generated by jschema_to_python version 0.0.1.dev29,
# with extension for dataclasses and type annotation.

from __future__ import annotations

import dataclasses
from typing import Any


@dataclasses.dataclass
class StackFrame(object):
    """A function call within a stack trace."""

    location: Any
    module: Any
    parameters: Any
    properties: Any
    thread_id: Any


# flake8: noqa