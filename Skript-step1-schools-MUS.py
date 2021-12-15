
import pandas as pd
import ipaddress

my_file1 = open('intEth-Mus(1st).cfg', 'w')
my_file2 = open('intGig-Mus(1st).cfg', 'w')
my_file3 = open('BGP-Mus(1st).cfg', 'w')

text1 = ''
text2 = ''
text3 = ''

data = pd.read_csv('my_text1.csv', encoding='cp1251', sep=',', skiprows=2, usecols=['kshwan', 'vlanvar'], dtype={'vlanvar': 'object'})

df = pd.DataFrame(data)


try:
 for m in range(200):

    ip = df.kshwan[m]
    i2 = df.vlanvar[m]
    ip1 = int(ipaddress.ip_address(ip)) - 2
    i1 = str(ipaddress.ip_address(ip1))


    text1 = text1 + (
        f'\n\n\ninterface eth-trunk0.{i2} \n vlan-type dot1q {i2} \n description "mo-oo-region" \n ip binding vpn-instance mo-oo-region \n ip address {i1} 29')
    text2 = text2 + (
        f'\n\n\ninterface GigabitEthernet0/3/43.{i2} \n vlan-type dot1q {i2} \n description "mo-oo-region" \n ip binding vpn-instance mo-oo-region \n ip address {i1} 29')
    text3 = text3 + (f'\n network {i1} 29')
except KeyError:
    print("ready")

my_file1.write(text1)
my_file1.close()

my_file2.write(text2)
my_file2.close()

my_file3.write('\n\n\nbgp 3.7283 \n ipv4-family vpn-instance mo-oo-region' + text3)
my_file3.close()
