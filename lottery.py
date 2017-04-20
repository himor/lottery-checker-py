import urllib
import json
import logging

class Lottery(object):
    url = "http://data.ny.gov/resource/5xaw-6ayf.json"

    def __init__(self):
        self.data = []

    def fetch(self):
        try:
            content = urllib.urlopen(self.url)
        except IOError as e:
            logging.error(e)
            return

        try:
            data = json.loads(content.read())
            self.convert(data)
        except ValueError as e:
            logging.error(e)
            return

    def convert(self, data):
        for item in data:
            if item['draw_date'] < "2013-10-15T00:00:00":
                continue
            numbers = map(int, item["winning_numbers"].split(" "))
            self.data.append({
                'date': item['draw_date'][:10],
                'numbers':numbers,
                'mega': int(item["mega_ball"])
            })

