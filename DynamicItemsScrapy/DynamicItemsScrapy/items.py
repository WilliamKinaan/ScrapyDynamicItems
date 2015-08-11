from scrapy.item import Item, Field
class Website(Item):
    def __setitem__(self, key, value):
        if key not in self.fields:
            self.fields[key] = Field()
        self._values[key] = value