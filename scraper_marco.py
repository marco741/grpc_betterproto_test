from definitions.scraper import ScraperBase, ScrapeReply, DisamiguousLink
from async_scraper_server import ScraperServer
import logging
import sys

class ScraperMarco(ScraperBase):
    async def search(self, text: str) -> ScrapeReply:
        logging.info("RICEVUTO!")
        return ScrapeReply(language="it", disambiguous=False, data=f'{text} è bello')

    async def long_search(self, text: str) -> ScrapeReply:
        logging.info("RICEVUTO!")
        return ScrapeReply(language="it", disambiguous=True, data=f'{text} è molto molto molto bello', disambiguous_data=[DisamiguousLink(label=f"{text} 1", url="https://www.google.com/images")]*3)


if __name__ == '__main__':
    logging.basicConfig(format='<%(asctime)s> %(levelname)s: %(message)s', level=logging.INFO)
    ScraperServer(ScraperMarco(), port=sys.argv[1]).run()
