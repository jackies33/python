import pandas as pd
import ipaddress

my_file1 = open('intEth-Mus(2st).cfg', 'w')
my_file2 = open('intGig-Mus(2st).cfg', 'w')
my_file3 = open('vpn-Mus(2st).cfg', 'w')
my_file4 = open('static-route-Mus(2st).cfg', 'w')
my_file5 = open('BGP-Mus(2st).cfg', 'w')

text1 = ''
text2 = ''
text3 = ''
text4 = ''
text5 = ''

data = pd.read_csv('losino.csv', encoding='cp1251', sep=',', skiprows=2, usecols=['vlanvar1', 'vlanvar2', 'vargw', 'oc', 'warnet'], dtype={'vlanvar2': 'object'})

df = pd.DataFrame(data)


try:
 for m in range(200):

    ip = df.vargw[m]
    i2 = df.vlanvar1[m]
    i8 = df.vlanvar2[m]
    ip2 = df.oc[m]
    ip5 = df.warnet[m]
    i7 = str(ipaddress.ip_address(ip))
    ip1 = int(ipaddress.ip_address(ip)) - 2
    i1 = str(ipaddress.ip_address(ip1))
    ip6 = ipaddress.ip_network(ip5)
    ip3 = ipaddress.ip_network(ip2)
    i5 = str(ip6.network_address)
    i6 = str(ip6.netmask)
    i3 = str(ip3.network_address)
    i4 = str(ip3.netmask)
    if i2 < 1000:
     text1 = text1 + (f'\n\n\ninterface eth-trunk0.{i8} \n vlan-type dot1q {i8} \n description "mo-oo-rtk-espd-school-0{i2} \n ip binding vpn-instance mo-oo-rtk-espd-school-0{i2} \n ip address {i1} 29')
     text2 = text2 + (f'\n\n\ninterface -GigabitEthernet0/3/43.{i8} \n vlan-type dot1q {i8} \n description "mo-oo-rtk-espd-school-0{i2} \n ip binding vpn-instance mo-oo-rtk-espd-school-0{i2} \n ip address {i1} 29')
     text3 = text3 + (f'\n\n\nip vpn-instance mo-oo-rtk-espd-school-{i2} \n ipv4-family \n route-distinguisher 105:3010{i2} \n apply-label per-instance \n vpn-target 105:3010{i2} export-extcommunity \n vpn-target 105:3010{i2} import-extcommunity \n vpn-target 105:3010510{i2} import-extcommunity')
     text4 = text4 + (f'\n\n\nip route-static vpn-instance mo-oo-rtk-espd-school-0{i2} {i3} {i4} {i7}')
     text5 = text5 + (f'\n\n\nipv4-family vpn-instance mo-oo-rtk-espd-school-0{i2} \n network {i5} {i6} \n network {i3} {i4}')
    elif i2 >= 1000:
        text1 = text1 + (f'\n\n\ninterface eth-trunk0.{i8} \n vlan-type dot1q {i8} \n description "mo-oo-rtk-espd-school-{i2} \n ip binding vpn-instance mo-oo-rtk-espd-school-{i2} \n ip address {i1} 29')
        text2 = text2 + (f'\n\n\ninterface -GigabitEthernet0/3/43.{i8} \n vlan-type dot1q {i8} \n description "mo-oo-rtk-espd-school-{i2} \n ip binding vpn-instance mo-oo-rtk-espd-school-{i2} \n ip address {i1} 29')
        text3 = text3 + (f'\n\n\nip vpn-instance mo-oo-rtk-espd-school-{i2} \n ipv4-family \n route-distinguisher 105:301{i2} \n apply-label per-instance \n vpn-target 105:301{i2} export-extcommunity \n vpn-target 105:301{i2} import-extcommunity \n vpn-target 105:301051{i2} import-extcommunity')
        text4 = text4 + (f'\n\n\nip route-static vpn-instance mo-oo-rtk-espd-school-{i2} {i3} {i4} {i7}')
        text5 = text5 + (f'\n\n\nipv4-family vpn-instance mo-oo-rtk-espd-school-{i2} \n network {i5} {i6} \n network {i3} {i4}')
except KeyError:
    print("ready")








my_file1.write(text1)
my_file1.close()

my_file2.write(text2)
my_file2.close()


my_file3.write(text3)
my_file3.close()

my_file4.write(text4)
my_file4.close()



my_file5.write('\n\n\nbgp 3.7283 \n ' + text5)
my_file5.close()
