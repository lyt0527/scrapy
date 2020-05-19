# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import pymysql

class WeiboPipeline(object):

    def process_item(self, item, spider):

        with open("weibo.csv", "a+", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([item["url"], item["MonitorName"], item["read_num"], item["up_num"], item["comment_num"], item["zhuanfa"]])


    # def __init__(self):
    #     self.db = pymysql.connect(host="172.22.14.51", port=8097, user="root", password="system", db="lyt")
    #     self.cur = self.db.cursor()
    #
    # def process_item(self, item, spider):
    #     # 往数据库里面写入数据
    #     self.cur.execute('insert into weibo1(Id, Url, MonitorName, read_num, up_num, comment_num, zhuanfa)VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}")'.\
    #                         format(0, item["url"], item["MonitorName"], item["read_num"], item["up_num"], item["comment_num"], item["zhuanfa"]))
    #     self.db.commit()
    #     return item
    #
    # def close_spider(self, spider):
    #     self.cur.close()
    #     self.db.close()


