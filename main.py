import threading
import requests
import time
import asyncio
import aiohttp

urls = ["http://postman-echo.com/delay/3"] * 10

def get_data_sync(urls):
    start_time = time.time()
    json_array = []
    for url in urls:
        json_array.append(requests.get(url).json())
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Execution time: ",elapsed_time," seconds")
    return json_array

#get_data_sync(urls) # 33 seconds

class ThreadingDownloader(threading.Thread):
    json_array = []

    def __init__(self,url):
        super().__init__()
        self.url = url

    def run(self):
        response = requests.get(self.url)
        self.json_array.append(response.json())
        print(self.json_array)
        return self.json_array

def get_data_threading(urls):
    start_time = time.time()
    threads = []
    for url in urls:
        t= ThreadingDownloader(url)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        print(t)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Execution time: ",elapsed_time," seconds")

#get_data_threading(urls) # 3.5 seconds


async def get_data_async_but_as_wrapper(urls):
    start_time =time.time()
    json_array = []

    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.get(url) as response:
                json_array.append(await response.json())

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Execution time: ", elapsed_time, " seconds")

#asyncio.run(get_data_async_but_as_wrapper(urls)) # 32 seconds

async def get_data(session,url, json_array):
    async with session.get(url) as response:
        json_array.append(await response.json())

async def get_data_async_concurrently(urls):
    start_time = time.time()
    json_array = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(asyncio.ensure_future(get_data(session,url,json_array)))
        await asyncio.gather(*tasks)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Execution time: ", elapsed_time , "seconds")

#asyncio.run(get_data_async_concurrently(urls)) # 3.3 seconds
