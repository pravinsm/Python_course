#converting dict {key:value} into dict {value:key}
port1={21:"FTP",22:"SSH",23:"telnet",80:"http"}

port2={port1[i]:i for i in port1}

print(port2)
