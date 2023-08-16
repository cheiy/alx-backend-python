#!/usr/bin/env python3
"""
Module contains a coroutine that imports async_comprehension and
runs it 4 times, and measures the total execution time
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    coroutine executes async_comprehension 4 times and measures the
    total execution time.
    """
    start_time = time.time()
    for i in range(4):
        await async_comprehension()
    return time.time() - start_time
