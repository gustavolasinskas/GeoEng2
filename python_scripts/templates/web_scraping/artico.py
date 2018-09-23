#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import scrapy


class ArticoSpider(scrapy.Spider):
    #Esse Spider salva os URLs abaixo em arquivos HTML no diretório em que for rodado
    name = "artico"
    start_urls = [
            "https://smpressa.wordpress.com/2015/01/31/artico-cenico/",
            "https://smpressa.wordpress.com/2015/01/13/26/",
            "https://smpressa.wordpress.com/2014/06/11/yosemite/",
        ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = "artico-%s.html" %page
        with open(filename, "wb") as f:
            f.write(response.body)
        self.log("Saved file %s" % filename)
