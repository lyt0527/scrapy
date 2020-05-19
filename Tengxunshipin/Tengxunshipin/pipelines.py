# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class TengxunshipinPipeline(object):
    def process_item(self, item, spider):
        with open("腾讯视频.csv", "a+", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([item["url"], item["MonitorName"], item["read_num"], item["up_num"], item["comment_num"], item["zhuanfa"]])