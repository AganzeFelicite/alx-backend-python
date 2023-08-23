#!/usr/bin/env python3
"""
this is a python
script that returns a
generator
"""


from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, Non]:
    """
    generators in python
    and asyncio
    """
    a: int = 1
    while a <= 10:
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        a += 1
