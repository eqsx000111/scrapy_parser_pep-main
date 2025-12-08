import csv
from collections import defaultdict
from datetime import datetime

from pep_parse import settings


class PepParsePipeline:

    def __init__(self):
        settings.RESULTS_DIR.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counts[item['status']] += 1
        return item

    def close_spider(self, spider):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        with open(
            settings.RESULTS_DIR / f'status_summary_{timestamp}.csv',
            mode='w',
            encoding='utf-8',
            newline=''
        ) as f:
            writer = csv.writer(f, dialect=csv.excel)
            writer.writerows([
                ['Статус', 'Количество'],
                *sorted(self.status_counts.items()),
                ['Итого', sum(self.status_counts.values())]
            ])
