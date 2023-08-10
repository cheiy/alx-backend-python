#!/usr/bin/env python3
"""
Module contains function that measures the total execution
time for wait_n(n, max_delay) and returns total_time / n.
"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    This function measures the total execution time for wait_n
    """
    begin_time = time.time()
    asyncio.run(wait_n(n, max_delay))

    return float((time.time() - begin_time) / n)
