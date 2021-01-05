import httpx

client = httpx.Client(timeout=10.0)
resp = client.get("https://google.com")
print(resp)
print(resp.status_code)
print(resp.text)
