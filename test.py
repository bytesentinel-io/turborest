import src.turborest as TurboRest

def main():
    endpoint = "https://reguse.net"
    logger = TurboRest.HTTPLogger("test.log", "test")
    client = TurboRest.Client(logger=logger)
    client.set_auth(auth=("bbenouarets", "test"), type="basic")
    print(client.headers)
    res = client.get(endpoint)
    print(client.html(res))

if __name__ == "__main__":
    main()