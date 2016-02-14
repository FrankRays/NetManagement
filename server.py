import socket
import symmetric
import Asymmetric
listenersock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listenersock.bind(("0.0.0.0",15823))
listenersock.listen(-1)
while True:
    c, addr = listenersock.accept()     # Establish connection with client.
    c.send('Hello')
    servers_rsa = Asymmetric.RSAkey0()
    c.send(servers_rsa.export_public())
    clients_private_rsa_exported_encryped = c.recv(2048)
    clients_private_rsa_exported = servers_rsa.decrypt_data(clients_private_rsa_exported_encryped)
    clients_private_rsa = Asymmetric.import_key(clients_private_rsa_exported)
    clients_public_rsa = Asymmetric.generate_public(clients_private_rsa)
    clients_rsa = Asymmetric.RSAkey2(clients_private_rsa,clients_public_rsa)
    clients_symmetric_key_encryptedd = c.recv(2048)
    clients_symmetric_key_encrypted = servers_rsa.decrypt_data(clients_symmetric_key_encrypted)
    clients_symmetric_key = clients_rsa.decrypt_data(clients_symmetric_key_encrypted)
    clients_symmetric_cipher = symmetric.AESCipher(clients_symmetric_key)
    c.send(clients_symmetric_cipher.encrypt("hand shake completed"))
    c.close()