import yaml

f = open("./templates/cluster.pb", "w")
seesaw_vip = '''
seesaw_vip: <
  fqdn: "{{ seesaw_vip.fqdn }}"
  ipv4: "{{ seesaw_vip.ipv4 }}"
  status: TESTING
> '''
vserver = '''
vserver: <
  name: "{{ vserver.name }}"
  entry_address: <
    fqdn: "{{ vserver.fqdn }}"
    ipv4: "{{ vserver.ipv4 }}"
    status: TESTING
  >
  rp: "{{ vserver.rp}}"
  vserver_entry: <
    protocol: {{ vserver_entry.protocol}}
    port: {{ vserver_entry.port }}
    scheduler: {{ vserver_entry.scheduler }}
    healthcheck: <
      type: {{ vserver_entry.healthcheck.type }}
      port: {{ vserver_entry.healthcheck.port }}
 #     mode: {{ vserver_entry.healthcheck.mode }}
 #     proxy: {{ vserver_entry.healthcheck.proxy }}
      tls_verify: {{ vserver_entry.healthcheck.tls_verify }}
    >
  >'''
endFile = '''
>'''
f.write(seesaw_vip)
with open('./group_vars/all') as template:
    data_yaml = yaml.full_load(template)
for item, _ in data_yaml['node'].items():
    node_cluster = '''
node: < 
  fqdn: "{{ node.%s.fqdn }}" 
  ipv4: "{{ node.%s.ipv4 }}" 
  status: TESTING 
>''' % (item, item)
    f.write(node_cluster)
f.write(vserver)
for item, _ in data_yaml['vserver_entry']['backend'].items():
    backend = '''
  backend: <
    host: <
      fqdn: "{{ vserver_entry.backend.%s.fqdn }}"
      ipv4: "{{ vserver_entry.backend.%s.ipv4 }}"
      status: TESTING
    >
    weight: {{ vserver_entry.backend.%s.weight }}
  >''' % (item, item, item)
    f.write(backend)
f.write(endFile)
f.close()