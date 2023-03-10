### Router
```
set interfaces ethernet eth0 hw-id '50:00:00:01:00:00'
set interfaces ethernet eth0 vif 10 address '10.0.10.5/24'
set interfaces ethernet eth0 vif 20 address '10.0.20.5/24'
set interfaces ethernet eth1 hw-id '50:00:00:01:00:01'
set interfaces ethernet eth2 hw-id '50:00:00:01:00:02'
set interfaces ethernet eth3 hw-id '50:00:00:01:00:03'
set interfaces loopback lo
set system config-management commit-revisions '100'
set system conntrack modules ftp
set system conntrack modules h323
set system conntrack modules nfs
set system conntrack modules pptp
set system conntrack modules sip
set system conntrack modules sqlnet
set system conntrack modules tftp
set system console device ttyS0 speed '115200'
set system host-name 'vyos'
set system login user vyos authentication encrypted-password '$6$Geh/wadCOu4LCvAT$diIPyzS8J.BgNQN2.eW9JT42.7XVrugXPSETt7n7M0BJLrPsRRkxKfmbSxSk9lNiln3FULVrlneb5n6YSbg9R/'
set system login user vyos authentication plaintext-password ''
set system ntp server time1.vyos.net
set system ntp server time2.vyos.net
set system ntp server time3.vyos.net
set system syslog global facility all level 'info'
set system syslog global facility protocols level 'debug'
```

### Switch1
```
set interfaces bridge br0 enable-vlan
set interfaces bridge br0 member interface eth0 allowed-vlan '10'
set interfaces bridge br0 member interface eth0 allowed-vlan '20'
set interfaces bridge br0 member interface eth1 allowed-vlan '20'
set interfaces bridge br0 member interface eth1 allowed-vlan '10'
set interfaces bridge br0 member interface eth2 allowed-vlan '10'
set interfaces bridge br0 member interface eth2 allowed-vlan '20'
set interfaces bridge br0 priority '1'
set interfaces bridge br0 stp
set interfaces ethernet eth0 hw-id '50:00:00:02:00:00'
set interfaces ethernet eth1 hw-id '50:00:00:02:00:01'
set interfaces ethernet eth2 hw-id '50:00:00:02:00:02'
set interfaces ethernet eth3 hw-id '50:00:00:02:00:03'
set interfaces loopback lo
set system config-management commit-revisions '100'
set system conntrack modules ftp
set system conntrack modules h323
set system conntrack modules nfs
set system conntrack modules pptp
set system conntrack modules sip
set system conntrack modules sqlnet
set system conntrack modules tftp
set system console device ttyS0 speed '115200'
set system host-name 'vyos'
set system login user vyos authentication encrypted-password '$6$Geh/wadCOu4LCvAT$diIPyzS8J.BgNQN2.eW9JT42.7XVrugXPSETt7n7M0BJLrPsRRkxKfmbSxSk9lNiln3FULVrlneb5n6YSbg9R/'
set system login user vyos authentication plaintext-password ''
set system ntp server time1.vyos.net
set system ntp server time2.vyos.net
set system ntp server time3.vyos.net
set system syslog global facility all level 'info'
set system syslog global facility protocols level 'debug'
```

### Switch2
```
set interfaces bridge br0 enable-vlan
set interfaces bridge br0 member interface eth0 native-vlan '10'
set interfaces bridge br0 member interface eth1 allowed-vlan '10'
set interfaces bridge br0 member interface eth1 allowed-vlan '20'
set interfaces bridge br0 member interface eth3 allowed-vlan '10'
set interfaces bridge br0 member interface eth3 allowed-vlan '20'
set interfaces bridge br0 priority '2'
set interfaces bridge br0 stp
set interfaces ethernet eth0 hw-id '50:00:00:03:00:00'
set interfaces ethernet eth1 hw-id '50:00:00:03:00:01'
set interfaces ethernet eth2 hw-id '50:00:00:03:00:02'
set interfaces ethernet eth3 hw-id '50:00:00:03:00:03'
set interfaces loopback lo
set system config-management commit-revisions '100'
set system conntrack modules ftp
set system conntrack modules h323
set system conntrack modules nfs
set system conntrack modules pptp
set system conntrack modules sip
set system conntrack modules sqlnet
set system conntrack modules tftp
set system console device ttyS0 speed '115200'
set system host-name 'vyos'
set system login user vyos authentication encrypted-password '$6$Geh/wadCOu4LCvAT$diIPyzS8J.BgNQN2.eW9JT42.7XVrugXPSETt7n7M0BJLrPsRRkxKfmbSxSk9lNiln3FULVrlneb5n6YSbg9R/'
set system login user vyos authentication plaintext-password ''
set system ntp server time1.vyos.net
set system ntp server time2.vyos.net
set system ntp server time3.vyos.net
set system syslog global facility all level 'info'
set system syslog global facility protocols level 'debug'
```

### Switch3
```
set interfaces bridge br0 enable-vlan
set interfaces bridge br0 member interface eth0 native-vlan '20'
set interfaces bridge br0 member interface eth2 allowed-vlan '10'
set interfaces bridge br0 member interface eth2 allowed-vlan '20'
set interfaces bridge br0 member interface eth3 allowed-vlan '10'
set interfaces bridge br0 member interface eth3 allowed-vlan '20'
set interfaces bridge br0 priority '2'
set interfaces bridge br0 stp
set interfaces ethernet eth0 hw-id '50:00:00:04:00:00'
set interfaces ethernet eth1 hw-id '50:00:00:04:00:01'
set interfaces ethernet eth2 hw-id '50:00:00:04:00:02'
set interfaces ethernet eth3 hw-id '50:00:00:04:00:03'
set interfaces loopback lo
set system config-management commit-revisions '100'
set system conntrack modules ftp
set system conntrack modules h323
set system conntrack modules nfs
set system conntrack modules pptp
set system conntrack modules sip
set system conntrack modules sqlnet
set system conntrack modules tftp
set system console device ttyS0 speed '115200'
set system host-name 'vyos'
set system login user vyos authentication encrypted-password '$6$Geh/wadCOu4LCvAT$diIPyzS8J.BgNQN2.eW9JT42.7XVrugXPSETt7n7M0BJLrPsRRkxKfmbSxSk9lNiln3FULVrlneb5n6YSbg9R/'
set system login user vyos authentication plaintext-password ''
set system ntp server time1.vyos.net
set system ntp server time2.vyos.net
set system ntp server time3.vyos.net
set system syslog global facility all level 'info'
set system syslog global facility protocols level 'debug'
```
