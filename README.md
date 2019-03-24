# Simple user questionnaire

To deploy the web-application on a server:
1. Write IP-address of your server in the deploy/host file
1. Run the following command
  ```bash
  $ ansible-playbook -i deploy/host deploy/main.yml
  ```
