from socket import gethostbyname, gethostname, gaierror


def get_ipv4() -> str:
    try:
        return gethostbyname(gethostname())
    except gaierror:
        return 'localhost'