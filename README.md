# SeesawAnsible
# Prepare 
    - Create file templates - cluster.pb by command: 
        python3 create_cluster.py
    - Node's fqdn should be the same hostname
# Create cluster Seesaw
    - ansible-playbook SetupCluster.yaml -i ./hosts