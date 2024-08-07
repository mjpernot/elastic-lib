# Configuration file
# Classification (U)
# Unclassified until filled.

# List of elasticsearch nodes in cluster
# Secure Syntax: host = ["https://servername:port", "https://servername2:port"]
# Unsecure Syntax: host = ["http://servername:port", "http://servername2:port"]
# Old Syntax: ["servername", "servername2"]
# NOTE:  If using the old syntax must also set the port and scheme entries.
host = ["https://HOST_NAME1:9200", "https://HOST_NAME2:9200"]
# Elasticsearch port - default is port 9200
# NOTE: Not required if using new syntax for host entry.
port = 9200
# User name
# If no user name is required then use None
user = None
# User pswd
japd = None

# SSL Configuration settings
# If not set will connect to Elasticsearch without using SSL connections.
# File containing the SSL certificate authority.
# Example: ssl_client_ca = "/etc/elasticsearch/certs/ca.pem"
ssl_client_ca = None
# Type of connection when using SSL connection.
# NOTE: Not required if using new syntax for host entry.
scheme = "https"

