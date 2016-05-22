from dominate.tags import *

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
        if not title:
            return ''
        return h2(title)


class PublicationItem(BaseItem):
    pass

class PresenationItem(BaseItem):
    pass

class TeachingItem(BaseItem):
    pass

class TeachingItem(BaseItem):
    pass

class WorkItem(BaseItem):
    pass

class AwardItem(BaseItem):
    pass
