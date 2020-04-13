from math import ceil


class PaginationHelper:
    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self._page = [self.collection[i:i+self.items_per_page] for i in range(0, len(self.collection), self.items_per_page)]
        print(self._page)

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return len(self._page)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        try:
            return len(self._page[page_index])
        except IndexError:
            return -1
    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range

    def page_index(self, item_index):
        if item_index > self.items_per_page:
            return -1
        try:
            return ceil(item_index / self.items_per_page)
        except (IndexError, ZeroDivisionError):
            return -1


collection = range(1,25)
helper = PaginationHelper(collection, 10)
print(helper.page_item_count(2))
print(helper._page)

l=[1,2,23,4,5,67,7,8,9]
l_final = []
for i in range(0, len(l), 4):
    l_final.append(l[i:i+4])
print(l_final)

print([l[i:i+4] for i in range(0, len(l), 4)])


