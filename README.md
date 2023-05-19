# Part 3: Setting up Monitoring Stackr
## 3.0 Connecting to EC2 instances (Nabeel_EC2_client01 & Nabeel_EC2_server01):
### 3.0.1 EC2 instances already created/launched and in running state:

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/30e1d865-7db4-458e-adfb-83297d179972)

### 3.0.2 Accessing/Connecting to EC2 instances using Putty:

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/59f04351-50c0-431a-9473-67ff2de3c9e0)

Connected to Server EC2 instance:

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/5b3a896f-c226-4060-b822-0a4791b32a71)

Connected to Client EC2 instance:

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/5ed9091e-f973-4dd7-8e16-7354180d77ec)

## 3.1 Setting up a monitoring stack on each EC2 instance using Docker Compose:
Files present in “montering_stack: directory:

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/115042cb-6159-46f0-88b8-ac1b9c003302)

### 3.1.1 Creating separate directory for monitoring stack setup on server instance:

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/2f1e881f-ad4a-456d-a00b-8bbdaf47b9d4)

### 3.1.2 Creating separate directory for monitoring stack setup on client instance:

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/b6e00aff-5271-4e18-8e24-5958e622c4dd)

### 3.1.3 Setting a “docker-compose.yml” & “prometheus.yml” YAML files in each EC2 instance/VM:
This YAML file will define the services needed for our monitoring stack. The configuration sets up Grafana on port 3020, Prometheus on port 9090, and Node Exporter on port 9100.

“docker-compose.yml” in server EC2 instance: 

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/e80ad473-b867-49ae-8e44-af65cc0b52d6)

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/05a50ba4-98ae-4671-be0e-ab5fb1a48658)

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/0f304945-8a98-428e-9d44-3570fa803122)

“prometheus.yml” in server EC2 instance: 

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/0117e9ed-6468-4a73-bc96-57684f3e2187)

“docker-compose.yml” in client EC2 instance: 

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/37784d7c-77f8-41a4-b9d2-b2a208262364)

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/d717f8ac-7369-4a08-bea9-32741a141c5d)

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/60b53f1f-3c6e-4702-a133-6439ce5d43bc)

“prometheus.yml” in client EC2 instance:

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/d3697b25-f289-4cbd-bec1-7b76d096b298)

### 3.1.4 Starting the monitoring stack on both VMs using Docker Compose:
Using the “docker-compose up -d” command on each VM, which starts with the Grafana, Prometheus, and Node Exporter containers in the background.

Monitoring Stack started in server EC2 instance:

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/8147e98f-8b5c-49b9-abaf-79d9781f16a3)

Monitoring Stack started in client EC2 instance:

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/85d0f754-bf45-40aa-8568-9fde49a3cf08)

## 3.2 Setting up Grafana dashboards:
### 3.2.1 Accessing Grafana using the public IP of each EC2 instance, followed by port 3020. And then logging in to Grafana using the default credentials (username: admin, password: admin).

Grafana access for server instance (http://server-ip:3020):

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/8d2262e9-f8f1-48d9-97ac-2b2e7412fdee)

Logged in to Grafana:

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/0214722e-ff80-4191-8ce9-fc62ee54f056)

Grafana access for client instance (http://client-ip:3020):

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/1e2ba8af-b97f-4187-b7a8-a9f2fd47b7fb)

Logged in to Grafana:

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/ea2f9b42-fcfb-4b4d-9089-2d3e08ba3f39)

### 3.2.2 Configuring a data source for Prometheus by adding a new data source in Grafana's settings (For Server Instance):

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/05bcf73e-f62f-4a70-b082-c83b82a308a5)

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/157e0434-72fc-41e3-bcd3-f61541d5bd17)

### 3.2.3 Successfully added the Prometheus data source (For Server Instance):

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/a3feff12-e59c-4c83-a582-5d0c3a19185b)

We can now start creating dashboards and panels in Grafana that utilize the data from Prometheus. 

### 3.2.4 Configuring a data source for Prometheus by adding a new data source in Grafana's settings (For Client Instance):

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/405e3dbc-ce04-4107-bb20-8d34d1f41664)

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/7305d332-0aa5-4574-b61e-e6e27dbbf1a7)

### 3.2.5 Successfully added the Prometheus data source (For Client Instance):

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/0a82327c-39b6-410f-8c5d-76aed422a2ea)

### 3.2.6 Running client & server containers for checking/testing monitoring stack:

#### Server Container:

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/13469b3c-5e10-4cf6-b4e2-aa561c818434)

Changed the port for server container from 8080 to 8181 so that it doesn’t overlap with cadvisor container.

#### Client Container:
Changing sever ip and port according to server instance/container updates:

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/bc301ff4-22b3-4037-80b0-d2b2b747f8ba)

Client application contianer started and successfully running:

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/64b69cbb-4eef-4cd7-9735-95fbff1121f4)

### 3.2.7 Importing dashboard from Grafana official website:
#### Dashboard imported for Server EC2 instance:

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/65a31ad3-1c93-4fe2-afc4-64adf1964989)

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/245afff9-06b1-4bda-ad0f-b7ef91284464)

Dashboard imported successfully:

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/79eec14f-cef2-4ea7-a315-d8f3643d9fe3)

#### Dashboard imported for Client EC2 instance:

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/efb632c3-3885-407a-a157-2689b00c7ca7)

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/0c99cc5f-2043-4be3-aa94-c0b20698f309)

Dashboard imported successfully:

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/3b0cda5b-6046-465a-8837-0dbc66f71ebc)


### 3.2.8 Viewing dashboard for Server EC2 instance:

#### Dashboard of Host System Metrics (Server):

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/6f23ac43-9c37-4c99-b51c-ebea8ff104b3)

#### Dashboard of Container Metrics (Server):

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/75e493da-1ae0-4963-8798-be6c56a8ed3b)

### 3.2.9 Viewing dashboard for Client EC2 instance:

#### Dashboard of Host System Metrics (Client):

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/64301499-0b54-4183-9786-416d14ad4980)

#### Dashboard of Container Metrics (Client):

![image](https://github.com/nab1999/project1_part3_server/assets/126570628/7a0d02e3-08f7-4e63-a80a-c7608c48bf6a)
