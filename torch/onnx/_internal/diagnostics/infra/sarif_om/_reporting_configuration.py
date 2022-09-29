# DO NOT EDIT! This file was generated by jschema_to_python version 0.0.1.dev29,
# with extension for dataclasses and type annotation.

from __future__ import annotations

import dataclasses
from typing import Any


@dataclasses.dataclass
class ReportingConfiguration(object):
    """Information about a rule or notification that can be configured at runtime."""

    enabled: Any
    level: Any
    parameters: Any
    properties: Any
    rank: Any


# flake8: noqa