from os import name
import time
import asyncio
from typing import List, Dict
from .config import *
from .local_sign import AutoSign
from .log import log_error_msg
from .message import server_chan_send


@log_error_msg
async def gen_run(name,username, password, enc=None):
    """运行"""
    auto_sign = AutoSign(name,username, password, enc=enc)
    result = await auto_sign.start_sign_task()
    # 关闭会话
    await auto_sign.close_session()
    return result


async def local_run():
    tasks = []
    for info in USER_INFOS:
        coro = gen_run(name=info['name'],
                        username=info['username'],
                        password=info['password'],
                        enc=info.get('enc', None))
        tasks.append(coro)
    results = await asyncio.gather(*tasks)
    await server_chan_send(results) # [[{'username': '135xxxx', 'name': 'test', 'date': '05-02 22:32', 'status': '学生端-签到成功'}]]
    results=sum(results,[])
    return results


async def qcode_run(enc):
    tasks = []
    for info in USER_INFOS:
        coro = gen_run(name=info['name'],
                        username=info['username'],
                        password=info['password'],
                        enc=enc)
        tasks.append(coro)
    results = await asyncio.gather(*tasks)
    results=sum(results,[])
    return results






def qcode_sign(enc):
    """
    二维码签到
    """
    loop = asyncio.new_event_loop()
    loop.run_until_complete(qcode_run(enc))
