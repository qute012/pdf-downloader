# -*- coding: utf-8 -*-
import scrapy

class Crawler(scrapy.Spider):
    name = "downloader"
    start_urls = None

    def __init__(self):
        with open("downloader/pdflink.txt", "rt") as f:
            self.start_urls = f.read().split("\n")

    def parse(self, response):
        dir = "downloader/pdf/"
        file_name = response.url.split('/')[-1]
        with open(dir+file_name, "wb") as f:
            f.write(response.body)