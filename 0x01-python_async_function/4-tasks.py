#!/usr/bin/env python3
"""
Module contains the task_wait_n function.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: float) -> List[float]:
    """
    Function calls the task_wait_random async function and returns
    a list of times
    """
    times_list = []
    for i in range(n):
        task = await task_wait_random(max_delay)
        times_list.append(task)

    return sorted(times_list)
