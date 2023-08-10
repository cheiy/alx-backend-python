#!/usr/bin/env python3
"""
Module contains an async routine called wait_n that takes in 2 in arguments
(n, max_delay). It then spawns wait_random n times with the specified max_delay
wait_n returns the list of all the delays in ascending order.
"""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """
    Function spawns wait_random n times
    """
    times_list: float = []
    for i in range(n: int):
        times_list.append(await wait_random(max_delay))
    return float(times_list)
