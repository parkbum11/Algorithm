import json


class SearchByTag:

    def __init__(self, data_file, query_tag):
        with open(data_file) as data_file:
            self._data = json.load(data_file)
        self.query = query_tag

    def search(self):
        new_items = {'serch_items': []}
        for item in self._data['items']:
            if 'tags' not in item: continue
            if self.query in item['tags']:
                new_items['serch_items'].append(item)

    def first(self):
        for item in self._data['items']:
            if 'tags' not in item: continue
            if self.query in item['tags']:
                return item