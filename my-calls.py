import httpx

# Your Codespace public URL
url = "https://musical-giggle-wrj4w9jxrjvp25w5p-3000.app.github.dev"

authData = {
    "id": "phillip.bradford@uconn.edu",
    "uuid-token": "925a4dfa-86b7-4c06-8f3e-fdccb0a748b2"
}

response = httpx.post(
    url + "/login",
    data=authData,
    headers={"Content-Type": "application/x-www-form-urlencoded"}
)

print("Status:", response.status_code)
print("Response:", response.text)