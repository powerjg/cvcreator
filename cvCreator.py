from dominate.tags import *

class Link(object):

    def __init__(self, target, text):
        self.target = target
        self.text = text

    def format(self):
        return a(text, href = target)

class BaseItem(object):
    fields = ['title', 'authors', 'date', 'location', 'details', 'links',
              'isInvited']

    def __init__(self, **kwargs):
        for field in self.fields:
            self.tryAddMember(field, kwargs)

    def tryAddMember(self, name, args):
        if name in args:
            setattr(self, name, args[name])
        else:
            setattr(self, name, '')

    def formatTitle(self):
        if not self.title: return ''
        if self.isInvited:
            t = span('Invited', cls = 'invited')
        else:
            t = ''
        return div(h2(t, self.title), cls = 'item-title')

    def formatDate(self):
        if not self.date: return ''
        return div(self.date, cls = 'item-date')

    def formatLocation(self):
        if not self.location: return ''
        return div(self.location, cls = 'item-location')

    def formatLinks(self):
        if not self.links: return ''
        tmp = div(cls = 'item-links')
        for link in self.links:
            tmp.add(a(span(link.text, cls = 'item-link', __inline = True),
                      href = link.target))
        return tmp

    def formatDetails(self):
        if not self.details: return ''
        return div([p(line) for line in self.details.split('\n')], cls = 'item-details')

    def formatAuthors(self):
        if not self.authors: return ''
        tmp = div(cls = 'item-authors')
        for i,author in enumerate(self.authors):
            if i == len(authors) - 1:
                comma = ''
            else:
                comma = ', '
            if author.startswith('Tiffany') or author.startswith('Jason'):
                tmp.add(span(author, cls = 'author-me'), comma)
            else:
                tmp.add(author + comma)
        return tmp

class PublicationItem(BaseItem):
    pass

class PresenationItem(BaseItem):

    def formatTitle(self):
        if not self.title: return ''
        if self.isInvited:
            t = span('Invited talk', cls='invited')
        else:
            t = ''
        return div(h2(t, self.title), cls='title')

class TeachingItem(BaseItem):
    pass

class TeachingItem(BaseItem):
    pass

class WorkItem(BaseItem):
    pass

class AwardItem(BaseItem):
    pass
