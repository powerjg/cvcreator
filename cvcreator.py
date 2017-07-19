import dominate
from dominate.tags import *

class Website(object):
    def __init__(self, title):
        self.title = title
        self.sections = []

    def add_section(self, section):
        self.sections.append(section)

    def format(self):
        doc = dominate.document(title = 'Title')
        with doc.head:
            link(rel='stylesheet', href='style.css')
        with doc:
            with div(cls = 'body'):
                for section in self.sections:
                    section.format()
        return doc

    def export(self, directory):
        if type(self) != Website:
            print "output should only be called with a Website!"
            return
        import os
        if not os.path.exists(directory):
            print "Creating directory", directory
            os.makedirs(directory)
        elif not os.path.isdir(directory):
            print "directory", directory, "is not a direcory!"

        doc = self.format()
        with open(os.path.join(directory, 'index.html'), 'w') as f:
            f.write(doc.render())

class Section(object):
    def __init__(self, name, ItemFactory):
        if name:
            self.name = h1(name)
        else:
            self.name = ''
        self.ItemFactory = ItemFactory
        self.items = []

    def add_item(self, **kwargs):
        self.items.append(self.ItemFactory(**kwargs))

    def format(self):
        if not self.items: return ''
        tmp = div(cls = self.__class__.__name__)
        tmp.add(self.name)
        for item in self.items:
            tmp.add(item.format())
        return tmp

class SubSection(Section):
    def __init__(self, section, name):
        if name:
            self.name = h2(name)
        else:
            self.name = ''
        self.section = section
        self.ItemFactory = self.section.ItemFactory
        self.items = []
        self.section.items.append(self)

class Link(object):

    def __init__(self, target, text):
        self.target = target
        self.text = text

    def format(self):
        return a(self.text, href = self.target)

class BaseItem(object):
    fields = ['title', 'authors', 'date', 'location', 'details', 'other_links',
              'isInvited', 'shortname', 'url']

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
        return div(h3(a(t, self.title, href=self.url)), cls = 'item-title')

    def formatDate(self):
        if not self.date: return ''
        return div(self.date.strftime('%B %Y'), cls = 'item-date')

    def formatLocation(self):
        if not self.location: return ''
        return div(self.location, cls = 'item-location')

    def formatLinks(self):
        if not self.other_links: return ''
        tmp = div(cls = 'item-links')
        for link in self.other_links:
            # tmp.add(a(span(link.text, cls = 'item-link', __inline = True),
            #           href = link.target))
            tmp.add(link.format())
        return tmp

    def formatDetails(self):
        if not self.details: return ''
        return div([p(line) for line in self.details.split('\n')], cls = 'item-details')

    def formatAuthors(self):
        if not self.authors: return ''
        tmp = div(cls = 'item-authors')
        for i,author in enumerate(self.authors):
            if i == len(self.authors) - 1:
                comma = ''
            else:
                comma = ', '
            if author.startswith('Tiffany') or author.startswith('Jason'):
                tmp.add(span(author, cls = 'author-me'), comma)
            else:
                tmp.add(author + comma)
        return tmp

class PublicationItem(BaseItem):

    def format(self):
        tmp = div(cls = self.__class__.__name__)
        tmp.add(self.formatTitle())
        tmp.add(self.formatAuthors())
        tmp.add(self.formatLocation())
        tmp.add(self.formatDate())
        tmp.add(self.formatDetails())
        tmp.add(self.formatLinks())
        return tmp

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
