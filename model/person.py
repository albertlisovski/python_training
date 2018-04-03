from sys import maxsize

class Person:
    def __init__(self, fname=None, mname=None, lname=None, nname=None, phone=None, email=None, address=None, id=None):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.nname = nname
        self.phone = phone
        self.email = email
        self.address = address
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.lname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.lname == other.lname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize