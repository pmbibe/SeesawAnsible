seesaw_vip: <
  fqdn: "{{ seesaw_vip.fqdn }}"
  ipv4: "{{ seesaw_vip.ipv4 }}"
  status: TESTING
>
node: <
  fqdn: "{{ node.nodeA.fqdn }}"
  ipv4: "{{ node.nodeA.ipv4 }}"
  status: TESTING
>
#node: <
#  fqdn: "{{ node.nodeB.fqdn }}"
#  ipv4: "{{ node.nodeB.ipv4 }}"
#  status: TESTING
#>
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
  >
  backend: <
    host: <
      fqdn: "{{ vserver_entry.backend.hostA.fqdn }}"
      ipv4: "{{ vserver_entry.backend.hostA.ipv4 }}"
      status: TESTING
    >
    weight: {{ vserver_entry.backend.hostA.weight }}
  >
 # backend: <
 #   host: <
 #     fqdn: "{{ vserver_entry.backend.hostB.fqdn }}"
 #     ipv4: "{{ vserver_entry.backend.hostB.ipv4 }}"
 #     status: TESTING
 #   >
 #   weight: {{ vserver_entry.backend.hostB.weight }}
 # >
>
