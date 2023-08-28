import os
import asyncio


async def delete_file_after_delay(file_path):
    try:
        await asyncio.sleep(3600)  # Wait for 1 hour (3600 seconds)
        print('============== Deleting file now ===========')
        os.remove(file_path)
        print('============== File Deleted successfully ===========')
    except Exception as e:
        print('============== File Deletion Failed ===========')
        print(e)
