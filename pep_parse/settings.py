from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR_NAME = 'results'
FEEDS_FILENAME = f'{RESULTS_DIR_NAME}/pep_%(time)s.csv'
FORMAT = 'csv'
RESULTS_DIR = PROJECT_ROOT / RESULTS_DIR_NAME
ALLOWED_DOMAINS = ['peps.python.org']
PEP_SPIDER_NAME = 'pep'
BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]


ROBOTSTXT_OBEY = True

FEED_EXPORT_ENCODING = 'utf-8'
FEEDS = {
    FEEDS_FILENAME: {
        'format': FORMAT,
        'overwrite': True,
        'fields': ['number', 'name', 'status'],
    }
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
