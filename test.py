import src.turborest as TurboRest

endpoint = "http://localhost:3000/api/orgs"
client = TurboRest.Client(format="json", auth=("Bearer", "xyz"))
res = client.get("http://localhost:3000/api/orgs")
print(res)