import csv
from collections import defaultdict
from datetime import datetime

from pep_parse import settings


class PepParsePipeline:
    @classmethod
    def from_crawler(cls, crawler):
        settings.RESULTS_DIR.mkdir(exist_ok=True)
        return cls()

    def open_spider(self, spider):
        self.status_counts = defaultdict(int)

    def process_item(self, item, spider):
        self.status_counts[item['status'].strip()] += 1
        return item

    def close_spider(self, spider):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        with open(
            settings.RESULTS_DIR / f'status_summary_{timestamp}.csv',
            mode='w',
            encoding='utf-8',
            newline=''
        ) as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'],)
            for status, count in sorted(self.status_counts.items()):
                writer.writerow([status, count])
            writer.writerow(['Итого', sum(self.status_counts.values())])
