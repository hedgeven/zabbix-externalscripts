# zabbix-externalscripts
Some useful zabbix externalscripts

## Check host IP in various DNSBLs
* Clone this repo
* Put check_dnsbl/check_dnsbl into /usr/lib/zabbix/externalscripts/check_dnsbl
* Import template check_dnsbl/zbx_export_dnsbl_template.xml
* Add your host to 'Template Check DNSBL'
