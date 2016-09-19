#!/usr/bin/env python

import re
import sys
import DNS
import requests
from bs4 import BeautifulSoup

def main(argv):
    try:
        dnsbl = argv[1]
        ip = argv[2]
    except:
        print("Usage:\n\t %s DNSBL IP" % argv[0])
        sys.exit(1)

    DNS.ParseResolvConf()

    if re.match(r'senderbase',dnsbl,flags=re.IGNORECASE):
        s = requests.Session()
        r = s.get('http://www.senderbase.org/lookup/?search_string=%s' % ip, cookies={'tos_accepted': '1330588800'})
        soup = BeautifulSoup(r.text, 'html.parser')
        if soup.find("table", { "class" : 'info_table' }).find("td", {"class": 'poor'}):
            return 1
    else:
        revip = '.'.join(reversed(ip.split('.')))
        try:
            if DNS.DnsRequest(name="%s.%s" % (revip, dnsbl),
                              qtype="A",
                              server=dnsbl,
                              timeout=5).req().answers[0]:
                return 1
        except:
            pass
    return 0


if __name__ == "__main__":
    print(main(sys.argv))
