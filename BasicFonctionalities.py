import socket


def is_connected():  # retrun True if connected, False else
    try:
        # connect and tell us if the host is reachable
        socket.create_connection(‘www.google.com’, 80)
        return True
    except OSError:
        pass
    return False
