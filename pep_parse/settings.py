from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = PROJECT_ROOT / 'results'

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

FEED_EXPORT_ENCODING = "utf-8"
FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'overwrite': True,
        'fields': ['number', 'name', 'status'],
    }
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
