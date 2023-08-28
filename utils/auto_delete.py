import os
import asyncio


async def delete_file_after_delay(file_path):
    await asyncio.sleep(60)  # Wait for 1 hour (3600 seconds)
    os.remove(file_path)
    print('============== Message Deleted successfully ===========')
