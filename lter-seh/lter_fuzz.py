from boofuzz import *

host = "192.168.1.35"
port = 9999

def main():
    session = Session(target = Target(connection = SocketConnection(host, port, proto='tcp')))

    s_initialize("Request")

    s_string("LTER", fuzzable = False)
    s_delim(" ", fuzzable = False, name = 'space-1')
    s_string("fuzzme")

    session.connect(s_get("Request"))
    session.fuzz()

if __name__ == "__main__":
    main()