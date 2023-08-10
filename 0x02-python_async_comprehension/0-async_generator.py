#!/usr/bin/env python3
"""
Module contains a corouting called async_generator
"""
import asyncio, random


async def async_generator():
    num_list = []
    async for i in range(10):
        await asyncio.sleep(1)
        num_list.append(random.uniform(0,10))
    return num_list
