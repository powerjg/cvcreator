
from cvCreator import *
from datetime import date

l = Link('http://google.com/', 'Google')
print l.format()
assert(str(l.format()) == '<a href="http://google.com/">Google</a>')

item = BaseItem(
    title = 'title',
    authors = [
        'Jason',
        'Tiffany',
        'Other'
    ],
    date = date(2017, 1, 1),
    location = 'here',
    details = 'extra details',
    other_links = [l, l],
    shortname = 'testing',
    url = 'http://nothing.com/'
)

print item.formatTitle()

print item.formatAuthors()

print item.formatDate()

print item.formatLocation()

print item.formatDetails()

print item.formatLinks()
