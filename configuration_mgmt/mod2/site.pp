# Google IT Automation with Python
# Configuration Management and the Cloud
# Setting up Puppet Clients and Servers

node webserver.example.com {
    class {'apache':}
}

node default{}