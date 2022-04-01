import socket
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
#context.set_ciphers('ALL:@SECLEVEL=2')
context.load_cert_chain('./server/server.crt', './server/server.key')
context.load_verify_locations('./ca/ca.crt')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind(('0.0.0.0', 8000))
    sock.listen(5)
    with context.wrap_socket(sock, server_side=True) as ssock:
        while True:
            try:
                conn, addr = ssock.accept()
                msg = conn.recv(1024).decode("utf-8")
                print(f"receive msg from client {addr}：{msg}")
                msg = f"yes , you have client_socketect with server.\r\n".encode("utf-8")
                conn.send(msg)
                conn.close()
            except Exception as ex:
                print(ex)


