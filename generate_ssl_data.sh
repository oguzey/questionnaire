#!/bin/bash -x
set -e

# create separate directory to store all generated data
BASE_DIR="ssl_generated_data"
mkdir -p "$BASE_DIR"
cd "$BASE_DIR"


# create configuration for out certificate
for C in `echo root-ca`; do

  mkdir $C
  cd $C
  mkdir certs crl newcerts private
  cd ..

  echo 1000 > $C/serial
  touch $C/index.txt $C/index.txt.attr

  echo '
[ ca ]
default_ca = CA_default
[ CA_default ]
dir            = '$C'    # Where everything is kept
certs          = $dir/certs                # Where the issued certs are kept
crl_dir        = $dir/crl                # Where the issued crl are kept
database       = $dir/index.txt            # database index file.
new_certs_dir  = $dir/newcerts            # default place for new certs.
certificate    = $dir/cacert.pem                # The CA certificate
serial         = $dir/serial                # The current serial number
crl            = $dir/crl.pem                # The current CRL
private_key    = $dir/private/ca.key.pem       # The private key
RANDFILE       = $dir/.rnd     # private random number file
nameopt        = default_ca
certopt        = default_ca
policy         = policy_match
default_days   = 365
default_md     = sha256

[ policy_match ]
countryName            = optional
stateOrProvinceName    = optional
organizationName       = optional
organizationalUnitName = optional
commonName             = supplied
emailAddress           = optional

[req]
req_extensions = v3_req
distinguished_name = req_distinguished_name

[req_distinguished_name]

[v3_req]
basicConstraints = CA:TRUE
' > $C/openssl.conf
done

# create Root CA certificate and private key
openssl genrsa -out root-ca/private/ca.key 4096
openssl req -config root-ca/openssl.conf -new -x509 -days 3650 -key root-ca/private/ca.key -sha256 -extensions v3_req -out root-ca/certs/ca.crt -subj '/CN=PyQuestionnaire Root CA'

# copy files to base directory
cp root-ca/private/ca.key ./questionnaire_ca.key
cp root-ca/certs/ca.crt ./questionnaire_ca.pem

# generate Diffie-Hellman parameter
openssl dhparam -out ./questionnaire_dhparam.pem 4096

cd ..
