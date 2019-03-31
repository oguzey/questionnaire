# Questionnaire Project

The project is a simple web-page that contains a questionnaire form. A user can fill the form with a name, a favorite color, and choose animals (from two option "cats" or "dogs") that he/she likes the most.

## Technologies
1. Python 3.6, Django framework 2.1.7 (for development the site);
1. uWSGI tool 2.0.18 (for running the site);
1. NGINX web-server 1.14.1 (as additional layer for handling user requests);
1. Ansible 2.6.5 (for deployment the site on a target machine).


## Project Structure
1. The source code of the site is located in the [pyquestionnaire](./pyquestionnaire) directory. Also, there are [manage.py](./manage.py) for debugging the site and [setup.py](./setup.py) for installation the python code as a python library on the target machine.
1. All files needed for deployment are located in the [deploy](./deploy) directory. In addition, there is a bash script [deploy.sh](./deploy.sh) to simplify the deployment process.
1. The script [generate_ssl_data.sh](./generate_ssl_data.sh) is responsible for generating an SSL certificate, an SSL private key, and a Diffie-Hellman parameter which will be used by NGINX web-server to allow HTTPS connection establishing with clients.

## Deployment Details
The ansible tool (ansible-playbook) is used to deploy the site on the target machine. The deployment process starts with running the main playbook file [deploy/site.yml](./deploy/site.yml). Then the different roles are run for doing different deployment tasks.
1. [systemsetup](./deploy/roles/systemsetup) role is responsible for installation packages and configuring a firewall;
1. [webserver](./deploy/roles/webserver) role installs and configures the NGINX web-server;
1. [appserver](./deploy/roles/appserver) role is responsible for creating an environment for the site. It creates a python virtual environment, installs all dependencies, uWSGI tool and starts it.

Also, there is an inventory file [hosts.ini](./deploy/inventories/hosts.ini) which contains a configuration for each target host where the site will be deployed. Moreover, by adding several lines with hosts data to this inventory file, it is easy to deploy the site on several machines.

The script [deploy.sh](./deploy.sh) can be used to start the deployment process.
If it is needed to pass additional arguments to the `ansible-playbook` tool, just add these arguments to the [deploy.sh](./deploy.sh) and it will pass them to the `ansible-playbook` tool.

For example, to execute only deploy tasks it needs to run the script with argument `-t deploy`.
```bash
$ ./deploy.sh -t deploy
```
To enable the verbose mode run the script with `-vvv`:
```bash
$ ./deploy.sh -vvv
```

Currently, only operating systems with `yum` package manager are supported. The deployment process was tested only in Amazon Linux OS.

## How to deploy on your machine
It needs to do the following items to deploy the project on your machine:
1. Write your host(s) data (host IP-address, user name, path to a ssh private key) into [hosts.ini](./deploy/inventories/hosts.ini) inventory file;
2. Run the script [deploy.sh](./deploy.sh) from the project directory.

## Example of Deployed Site
There is an example of [the site](https://35.183.98.26/) deployed on an AWS virtual machine.
To visit the site click [here](https://35.183.98.26/).
The site is running on Amazon Linux OS:
```
Amazon Linux AMI 2018.03.0 (HVM), SSD Volume Type - ami-07423fb63ea0a0930

The Amazon Linux AMI is an EBS-backed, AWS-supported image. The default image includes AWS command
line tools, Python, Ruby, Perl, and Java. The repositories include Docker, PHP, MySQL, PostgreSQL,
and other packages.
````
