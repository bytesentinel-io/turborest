import src.turborest as TurboRest

def main():
    endpoint = "http://localhost:3000/api"
    auth = ("Bearer", "xyz")
    client = TurboRest.Client(format="json", auth=auth)
    client.set_user_agent("TestAgent/1.0.0")
    client.set_success(print)
    res = client.get(endpoint)

    print(res)

if __name__ == "__main__":
    main()