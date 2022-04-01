import socket
import ssl


# PROTOCOL_TLS_CLIENT requires valid cert chain and hostname
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
#context.set_ciphers('ALL:@SECLEVEL=1')
context.check_hostname = False
context.load_verify_locations('./ca/ca.crt')
context.verify_mode = ssl.CERT_REQUIRED

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    with context.wrap_socket(sock, server_side=False) as ssock:
        print(ssock.version())
        ssock.connect(('117.50.163.51', 8000))
        msg = "do i connect with server ?".encode("utf-8")
        ssock.send(msg)
        msg = ssock.recv(1024).decode("utf-8")
        print(f"receive msg from server : {msg}")
        ssock.close()
