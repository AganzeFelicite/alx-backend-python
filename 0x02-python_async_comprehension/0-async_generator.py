#!/usr/bin/env python3
"""
this is a python
script that returns a
generator
"""


from typing import AsyncGenerator
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """
    generators in python
    and asyncio
    """
    a: int = 1
    while a <= 10:
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        a += 1
