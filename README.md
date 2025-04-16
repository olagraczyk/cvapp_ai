# 📄 CVApp AI — Google Docs Reader (Part of a Bigger Project)

This is a foundational component of a larger AI-powered application that assists in generating customized CVs based on personal experience and job descriptions.  
Currently, this part focuses on **securely reading content from a private Google Doc**.

> This is still **in development** and only covers experience extraction for now.

---

## ✅ What I’ve Learned So Far

- How to use the Google Docs API with Python
- How to authenticate using OAuth (with refresh tokens)
- How to manage secrets securely using `.env` files
- How to structure a clean project with good practices (like `.gitignore` and token caching)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/olagraczyk/cvapp_ai.git
cd cvapp_ai
```

### 2. Google Cloud Setup
1. Go to Google Cloud Console
2. Create a new project
3. Enable the Google Docs API
4. Go to APIs & Services > Credentials
5. Create OAuth client ID credentials (select Desktop App)
6. Download the client_secret.json file

### 3. Project Folder Structure
Place your credentials as follows:

```
cvapp_ai/
├── auth/
│   └── client_secret.json  ← Put it here
├── .env                    ← Your environment variables
├── main_app.ipynb
...

```

In `.env` file paste 
```
GOOGLE_DOC_ID=your_google_doc_id_here
```
Google Doc Id is placed in the url of the doc. You can find which one it is easly on the Internet

Update the `.gitignore` file if you don't want your secrets and tokens to be tracked by Git.

```
.env
auth/client_secret.json
auth/token.json
```

### 4. Install Dependencies
In terminal 
```
pip install -r requirements.txt
```

### 5. 🛠 To Be Continued...

----

## Author: Ola Graczyk