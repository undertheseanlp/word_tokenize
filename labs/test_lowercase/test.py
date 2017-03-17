# -*- coding: utf-8 -*-
vietnamse_map = {
    "Đ": "đ"
}


def vietnamese_lower(s):
    if type(s) == type(u""):
        return s.lower()
    return unicode(s, "utf8").lower().encode("utf8")


s = "Đi học"
s = vietnamese_lower(s)
print 0
