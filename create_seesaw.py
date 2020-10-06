import yaml
# nodeA, nodeB, nodeC
# {{ node.nodeA.ip_v4 if (ansible_hostname != node.nodeA.fqdn) else node.nodeB.ip_v4 }}
# {{ node.nodeA.ip_v4 if (ansible_hostname != node.nodeA.fqdn) else node.nodeC.ip_v4 }}
# {{ node.nodeB.ip_v4 if (ansible_hostname != node.nodeB.fqdn) else node.nodeA.ip_v4 }}
# {{ node.nodeB.ip_v4 if (ansible_hostname != node.nodeB.fqdn) else node.nodeC.ip_v4 }}
# {{ node.nodeC.ip_v4 if (ansible_hostname != node.nodeC.fqdn) else node.nodeA.ip_v4 }}
# {{ node.nodeC.ip_v4 if (ansible_hostname != node.nodeC.fqdn) else node.nodeB.ip_v4 }}
# 1 (2,3)
# 2 (1,3)
# 3 (1,2)
# peer_ipv4 = '''{{ node.nodeA.ip_v4 if (ansible_hostname != node.nodeA.fqdn) else node.nodeB.ip_v4 }}''' % (item)
with open('./hosts') as host:
    data = host.readlines()
with open('./group_vars/all') as template:
    data_yaml = yaml.full_load(template)
    for item, value in data_yaml['node'].items():
        for i in range(1, len(data)):
            if value['ip_v4'] != data[i].strip():
                print ('{{ node.%s.ip_v4 if (ansible_hostname != node.%s.fqdn) else node.%s.ip_v4 }}' % (item,item,i))

a = [1, 2, 3]
b = [1, 2, 3]
for i in a:
    for j in b:
        if i != j:
            print (i,j)
        
