# Simple user questionnaire

To deploy the web-application on a server:
1. Write IP-address of your server in the deploy/host file
1. Run the following command
  ```bash
  $ ansible-playbook -i deploy/host deploy/main.yml
  ```


Deployed on: 35.183.98.26

Amazon Linux AMI 2018.03.0 (HVM), SSD Volume Type - ami-07423fb63ea0a0930

The Amazon Linux AMI is an EBS-backed, AWS-supported image. The default image includes AWS command line tools, Python, Ruby, Perl, and Java. The repositories include Docker, PHP, MySQL, PostgreSQL, and other packages.