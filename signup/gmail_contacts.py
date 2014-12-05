import gdata.contacts.data
import gdata.contacts.client


class ContactsEmail(object):

    def __init__(self, email, password):
        self.gd_client = gdata.contacts.client.ContactsClient(source='GoogleInc-ContactsPythonSample-1')
        self.gd_client.ClientLogin(email, password, self.gd_client.source)
        self.contacts_emails = list()

    def GetPaginatedFeed(self, feed, print_method):
        ctr = 0
        while feed:
            ctr = print_method(feed=feed, ctr=ctr)
            next = feed.GetNextLink()
            feed = None
            if next:
                if self.PromptOperationShouldContinue():
                    feed = self.gd_client.GetContacts(uri=next.href)
                else:
                    feed = None

    def PromptOperationShouldContinue(self):
        return True

    def ListAllContacts(self):
        feed = self.gd_client.GetContacts()
        self.GetPaginatedFeed(feed, self.GetContactsFeed)
        return self.contacts_emails

    def GetContactsFeed(self, feed, ctr):
        if not feed.entry:
            print '\nNo contacts in feed.\n'
            return 0
        for i, entry in enumerate(feed.entry):
            if not entry.name is None:
                family_name = entry.name.family_name is None and " " or entry.name.family_name.text
                full_name = entry.name.full_name is None and " " or entry.name.full_name.text
                given_name = entry.name.given_name is None and " " or entry.name.given_name.text
                try:
                    email = entry.email[0].address
                    self.contacts_emails.append(email)
                except Exception as e:
                    pass
        return len(feed.entry) + ctr

