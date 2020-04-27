# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import hashlib
import json
from base64 import b64decode
from os import environ, getcwd, path

import firebase_admin
from firebase_admin import credentials, firestore
from scrapy import log
from scrapy.exporters import BaseItemExporter


class InteraPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'intera':
            item['url'] = '{0}?hunter={1}'.format(
                item['url'], spider.settings['INTERA_HUNTER_CODE'])

        return item


class FirebasePipeline(BaseItemExporter):
    def load_spider(self, spider):
        self.crawler = spider.crawler
        self.settings = spider.settings

    def open_spider(self, spider):
        self.load_spider(spider)
        filename = path.normpath(path.join(getcwd(), 'firestore_secrets.json'))

        with open(filename, 'w') as json_file:
            json_file.write(
                b64decode(self.settings['FIRESTORE_SECRETS']).decode('utf-8'))

        cred = credentials.Certificate(filename)
        firebase_admin.initialize_app(cred, {
            'projectId': self.settings['FIRESTORE_ID']
        })
        self.db = firestore.client()

    def process_item(self, item, spider):
        doc_ref = self.db.collection(self.settings['FIRESTORE_COLLECTION']).document(
            hashlib.sha1(item['url'].encode('utf-8')).hexdigest())
        doc_ref.set(dict(item))
        return item
