import csv
import re
import time
import aiohttp
import asyncio
from aiohttp import ClientTimeout


async def getData(url, headers, sm):
    print(url)
    #创建回话asyncio
    sm.acquire()
    try:
        async with aiohttp.ClientSession(timeout=ClientTimeout(total=15)) as session:
            #发送get请求
            async with session.get(url, headers=headers) as response:
                #返回响应内容
                # print(await response.text())
                sm.release()
                print('====')
                if response.status == 200:
                    return await response.text()
    except Exception as e:
        print(e, "======================================")


def saveData(result):
    # print(data)
    # print('+++++')
    with open(r"data.csv", "a+", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Url", "MonitorName", "阅读", "点赞", "评论", "转发"])
        for j in result:
            # print(m, n)
            # break
            try:
                number = re.findall(r'<span class="red" style="margin-right:3px">(.+?)</span>', j)
                if number == []:
                    print(number)
                    writer.writerow([j[0], j[1], "", "", "", ""])
                    # print("评论数：", "")
                else:
                    writer.writerow([j[0], j[1], "", "", number[0], ""])
                    print(number)
                    # print("评论数：", number[0])
            except:
                pass


def main():
    data = csv.reader(open(r"C:\Users\liuyuntao\Desktop\贴吧.csv"))

    for i in data:
        #遍历data中的url，传给getData函数
        task = asyncio.ensure_future(getData(i[0], headers, sm))
        #将所有的请求加入到tasks中
        tasks.append(task)

    #等待所有请求执行完成，返回响应内容
    result = loop.run_until_complete(asyncio.gather(*tasks))

    saveData(result)


if __name__ == "__main__":
    start_time = time.time()
    headers={
        "User-Agent" : "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    tasks = []
    #创建get_event_loop对象
    loop = asyncio.get_event_loop()
    sm = asyncio.Semaphore(3)
    main()
    end_time = time.time()
    print("总共用时：", end_time - start_time)
    loop.close()

        

