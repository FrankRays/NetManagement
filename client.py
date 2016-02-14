import socket
import symmetric
import Asymmetric
s = socket.socket()
host = socket.gethostname()
port = 15823
s.connect((host, port))
print s.recv(1024)
servers_rsa_public_key_exported = s.recv(2048)
servers_rsa_public_key = Asymmetric.import_key(servers_rsa_public_key_exported)
servers_rsa = Asymmetric.RSAkey1(servers_rsa_public_key)
clients_rsa = Asymmetric.RSAkey0()
clients_private_rsa_exported = clients_rsa.export_private()
clients_private_rsa_exported_encrypted = servers_rsa.encrypt_data(clients_private_rsa_exported)
print type(clients_private_rsa_exported_encrypted)
s.send(clients_private_rsa_exported_encrypted)
symmetric_key = "mychiper"
client_symmetric = symmetric.AESCipher(symmetric_key)
clients_symmetric_key_encryptedd = clients_rsa.encrypt_data(symmetric_key)
clients_symmetric_key_encrypted = servers_rsa.encrypt_data(clients_symmetric_key_encryptedd)
s.send(clients_symmetric_key_encrypted)
encryptd_confirmation_message = s.recv(1024)
confirmation_message = client_symmetric.decrypt(encryptd_confirmation_message)
if confirmation_message == "hand shake completed":
    print "connection to manager succssed"


s.close