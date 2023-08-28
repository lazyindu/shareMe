import os
import asyncio


async def delete_file_after_delay(file_path):
    await asyncio.sleep(3600)  # Wait for 1 hour (3600 seconds)
    os.remove(file_path)