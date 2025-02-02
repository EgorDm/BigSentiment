import click

from scraping.bitstamp import bitstamp
from scraping.binance import binance
from scraping.coinmarketcap import coinmarketcap
from scraping.news import news
from scraping.twitter import twitter


@click.group()
def scraper():
    pass


scraper.add_command(twitter)
scraper.add_command(news)
scraper.add_command(binance)
scraper.add_command(coinmarketcap)
scraper.add_command(bitstamp)
