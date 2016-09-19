# zabbix-externalscripts
Some useful zabbix externalscripts

## Check host IP in various DNSBLs
* Clone this repo
* Put check_dnsbl/check_dnsbl into /usr/lib/zabbix/externalscripts/check_dnsbl
* Add read and execute rights (chmod a+rx /usr/lib/zabbix/externalscripts/check_dnsbl)
* Import template check_dnsbl/zbx_export_dnsbl_template.xml
* Add your host to 'Template Check DNSBL'

## Check host IP in Antizapret database (Roskomnadzor)
* Clone this repo
* Put check_antizapret/check_antizapret into /usr/lib/zabbix/externalscripts/check_antizapret
* Add read and execute rights (chmod a+rx /usr/lib/zabbix/externalscripts/check_antizapret)
* Import template zbx_export_antizapret_template.xml
* Add your host to 'Template Check DNSBL'
