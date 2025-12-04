# CSE2102 Lab 09 – Web Tokens  
**Author:** Filipe Rodrigues  
**Course:** Software Engineering – Prof. Bradford  
**Description:** Final Project Part 1

---

## 1. Overview

This project implements a simple web service running in GitHub Codespaces that accepts a security web-token.  
A Python client running on my local machine sends POST requests to the service, including the token for authentication.

The service validates the token and responds with success, error, or failure depending on the request.

---

## 2. Files Included

### **my-server.py**
A Flask server running on port 3000 inside Codespaces.  
It exposes two routes:

- `/` – returns “Server is running.”
- `/login` – accepts POST requests with:
  - `id`
  - `uuid-token`

Responses from the server:
- **200** – valid token accepted  
- **400** – missing fields  
- **403** – invalid token  

---

### **my-calls.py**
A Python client script that runs on my local computer.  
It sends POST requests to the Codespace public URL, including the correct `id` and `uuid-token`, and prints the status code and JSON response.

---

### **test_server.py**
Unit tests using `pytest` that test the server logic directly (without running the server).  
Includes tests for:

- Successful login  
- Missing fields  
- Invalid token  

All tests pass.

---

### **functional_test.py**
Functional tests that send real HTTP requests to the running Codespace server.

Tests include:
- Valid token test  
- Invalid token test  

---

## 3. Installation (Codespace)

### 1. Install Flask:

```bash
pip3 install flask
```

### 2. Run the server:

```bash
python3 my-server.py
```

The server will output something like:

```
Running on http://0.0.0.0:3000
```

### 3. Make the port public:

In Codespaces → PORTS tab → right-click port **3000** → **Port Visibility → Public**

This gives a URL like:

```
https://xxxxx-3000.app.github.dev
```

This is the URL the client will send requests to.

---

## 4. How to Run the Client (Local Machine)

### 1. Install httpx:

```bash
pip3 install httpx
```

### 2. Run the client:

```bash
python3 my-calls.py
```

### Expected output:

```
Status: 200
Response: {"message":"Token accepted","status":"success"}
```

Make sure the server is still running in Codespaces when running the client.

---

## 5. Running Unit Tests

Inside Codespaces:

```bash
pip3 install pytest
pytest -q
```

Expected output:

```
3 passed in 0.13s
```

---

## 6. Running Functional Tests

Make sure the server is running, then:

```bash
python3 functional_test.py
```

Expected output:

```
Success test: 200 {"message":"Token accepted","status":"success"}
Invalid token test: 403 {"message":"Invalid token","status":"fail"}
```

---

## 7. What Was Submitted

- All Python source files  
- Unit tests + functional tests  
- A working demonstration video  
- README with full instructions  

---

## 8. Summary

This lab demonstrates a basic client-server authentication workflow using Flask, POST requests, and token validation. It also includes testing using both unit tests and real functional HTTP requests.

