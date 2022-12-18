### Router

```
set interfaces ethernet eth0 hw-id '50:00:00:01:00:00'
set interfaces ethernet eth0 vif 10 address '10.0.10.5/24'
set interfaces ethernet eth0 vif 20 address '10.0.20.5/24'
set interfaces ethernet eth1 address '12.12.12.12/24'
set interfaces ethernet eth1 hw-id '50:00:00:01:00:01'
set interfaces ethernet eth2 hw-id '50:00:00:01:00:02'
set interfaces ethernet eth3 hw-id '50:00:00:01:00:03'
set interfaces loopback lo
set nat source rule 20 outbound-interface 'eth1'
set nat source rule 20 source
set nat source rule 20 translation address '12.12.12.12'
set protocols static route 0.0.0.0/0 next-hop 12.12.12.13
set service dhcp-server shared-network-name VLAN10 subnet 10.0.10.0/24 default-router '10.0.10.5'
set service dhcp-server shared-network-name VLAN10 subnet 10.0.10.0/24 name-server '10.0.10.5'
set service dhcp-server shared-network-name VLAN10 subnet 10.0.10.0/24 range 0 start '10.0.10.10'
set service dhcp-server shared-network-name VLAN10 subnet 10.0.10.0/24 range 0 stop '10.0.10.254'
set service dhcp-server shared-network-name VLAN20 subnet 10.0.20.0/24 default-router '10.0.20.5'
set service dhcp-server shared-network-name VLAN20 subnet 10.0.20.0/24 name-server '10.0.20.5'
set service dhcp-server shared-network-name VLAN20 subnet 10.0.20.0/24 range 0 start '10.0.20.10'
set service dhcp-server shared-network-name VLAN20 subnet 10.0.20.0/24 range 0 stop '10.0.20.254'
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

### Router2

```
set interfaces ethernet eth0 hw-id '50:00:00:07:00:00'
set interfaces ethernet eth1 address '12.12.12.13/24'
set interfaces ethernet eth1 hw-id '50:00:00:07:00:01'
set interfaces ethernet eth2 hw-id '50:00:00:07:00:02'
set interfaces ethernet eth3 hw-id '50:00:00:07:00:03'
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