from sys import maxsize

class Person:
    def __init__(self, fname=None, mname=None, lname=None, nname=None, homephone=None, mobilephone=None, workphone=None,
                 secondaryphone=None, allphones_from_home_page=None, email=None, email2=None, email3=None,
                 allemails_from_home_page=None, address=None, id=None):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.nname = nname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.allphones_from_home_page = allphones_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.allemails_from_home_page = allemails_from_home_page
        self.address = address
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.fname, self.lname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lname == other.lname and self.fname == other.fname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize