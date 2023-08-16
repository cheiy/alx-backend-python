#!/usr/bin/env python3
"""
Module contains a coroutine called async_generator
"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """
    coroutine loops 10 times, waiting 1 second each time and then
    yields a random number between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
