class Phone(object):
    def __init__(self, pname, pnum, qq, email):
        self._pname = pname
        self._pnum = pnum
        self._qq = qq
        self._email = email
    @property
    def pname(self):
        return self._pname
    @property
    def pnum(self):
        return self._pnum
    @property
    def qq(self):
        return self._qq
    @property
    def email(self):
        return self._email

class Dept(object):
    def __init__(self, dno, dname, dloc):
        self._dno = dno
        self._dname = dname
        self._dloc = dloc
    @property
    def dname(self):
        return self._dname
    @property
    def dno(self):
        return self._dno
    @property
    def dloc(self):
        return self._dloc