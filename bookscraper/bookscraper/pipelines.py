import re
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):
        return item


class CleanPhonePipline:
    def process_item(self, item, spider):
        for key in item:
            item[key] = item[key].strip()

        if 'old_price' in item or 'special_price' in item:
            price_str = item['old_price']
            price = int(''.join(re.findall(r'\d+', price_str)))
            item['old_price'] = price

        if 'special_price' in item:
            price_str = item['special_price']
            price = int(''.join(re.findall(r'\d+', price_str)))
            item['special_price'] = price

        return item
