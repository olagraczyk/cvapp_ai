# 📄 CVApp AI — Google Docs Reader (Part of a Bigger Project)

This is a foundational component of a larger AI-powered application that assists in generating customized CVs based on personal experience and job descriptions.  
Currently, this part focuses on:
- **Securely reading content from a private Google Doc**
- **Scraping job descriptions from external job boards**

> This is still **in development** and only covers experience extraction for now.

---

## ✅ What I’ve Learned So Far

- How to use the Google Docs API with Python
- How to authenticate using OAuth (with refresh tokens)
- How to manage secrets securely using `.env` files
- How to structure a clean project with good practices (like `.gitignore` and token caching)
- How to scrape websites using `requests` and `BeautifulSoup`
- How to extract relevant job offer content and save it for later use
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

---
### Web Scraping Job Descriptions
You can run  `web_scraper.py` to extract the main content from a job posting page.

Currently:
- The script takes a hardcoded URL (will be updated for dynamic input later in a Streamlit App).
- It saves the job title and main content into job_description.txt.

In the Jupyter notebook prototype, you can enter a job link as input and run the scraping function. This will update the job description for the CV logic later.

### 🛠 To Be Continued...

----

## Author: Ola Graczyk
