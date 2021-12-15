from pprint import pprint
import yaml
import pandas as pd
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,

)


#huawei_NE20 = {
  #  'device_type' : 'huawei',
   # 'ip': '10.100.138.1',
    #'username': 'stepanover.adm',
    #'password': 'P@ssw0rd21'
#}


#commands=('dis cur conf vpn-instance')

#ssh = ConnectHandler(**huawei_NE20)
#ssh.enable()
#data1 = ssh.send_command(commands)
#ssh.exit_enable_mode()
#df=pd.DataFrame.to_string(eval(data1))
#df = df['data1'].apply(str)
data1 = pd.read_table('vpn.txt', encoding='cp1251', sep='S+', )
print (data1)

#print(result1)




