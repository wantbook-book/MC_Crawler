from crawler.crawler import MC_BaiscCrawler
from crawler.url_crawler import URLCrawler
from pathlib import Path
from utils.markdown import split_file


def crawl():
    urls_dir = Path('crawler_data/urls')
    url_crawler = URLCrawler(
        base_url='https://minecraft.wiki',
        urls=[
            'https://minecraft.wiki/w/Mob',
            'https://minecraft.wiki/w/Block',
            'https://minecraft.wiki/w/Item',
        ],
        output_dir=urls_dir
    )
    url_crawler.crawl()
    for file in urls_dir.iterdir():
        if file.is_file():
            with open(file, 'r') as f:
                urls = f.readlines()
                urls = [url.strip() for url in urls]
                output_dir = Path('crawler_data') / file.stem
                crawler = MC_BaiscCrawler(urls, output_dir)
                crawler.crawl()

def split_content():
    content_dirs = [
        Path('crawler_data/Mob'),
        Path('crawler_data/Block'),
        Path('crawler_data/Item'),
    ]
    for content_dir in content_dirs:
        for content_file in content_dir.iterdir():
            if content_file.is_file():
                split_file(content_file, word_count_limit=1000, word_count_thres=40)

if __name__ == '__main__':
    # crawl()
    split_content()
    