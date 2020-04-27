# -*- coding: utf-8 -*-

from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import replace_escape_chars, strip_html5_whitespace

from mandatrampo.items import Job


class JobLoader(ItemLoader):
    default_item_class = Job
    default_output_processor = TakeFirst()


class JobIntera(JobLoader):
    title_in = MapCompose(replace_escape_chars, lambda x: x.split(
        '|')[-1], strip_html5_whitespace)
    company_in = MapCompose(replace_escape_chars,
                            lambda x: x.split('|'), strip_html5_whitespace)
