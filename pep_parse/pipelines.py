import csv
from collections import defaultdict

from itemadapter import ItemAdapter

from constants import TIMESTAMP
from pep_parse import settings


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_counts = defaultdict(int)
        self.total = 0
        settings.RESULTS_DIR.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        status = adapter.get('status') or ''
        status = status.strip()
        self.status_counts[status] += 1
        self.total += 1
        return item

    def close_spider(self, spider):
        with open(
            settings.RESULTS_DIR / f'status_summary_{TIMESTAMP}.csv',
            mode='w',
            encoding='utf-8',
            newline=''
        ) as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            for status, count in sorted(self.status_counts.items()):
                writer.writerow([status, count])
            writer.writerow(['Итого', self.total])
