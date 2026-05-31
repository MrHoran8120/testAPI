# Secure News Reader

Secure News Reader is a small command-line Python project for Year 12 Software
Engineering students learning about APIs, API keys, and secure software
development.

The project contains two versions:

- `news_insecure.py` shows an unsafe way to store an API key.
- `news_secure.py` shows a safer way to load an API key from a `.env` file.

Both versions use [NewsAPI](https://newsapi.org/) to request recent articles
from Australian news websites using the `/v2/everything` endpoint.

The request filters by Australian publisher domains such as `abc.net.au`,
`news.com.au`, `smh.com.au`, and `9news.com.au`. This is more reliable for the
classroom lesson than `country=au`, which can sometimes return an empty list.

The code is deliberately kept small so the lesson can focus on the main
concepts: making an API request, using an API key, and keeping secrets out of
source code.

## 1. What Is an API?

An API, or Application Programming Interface, is a way for one program to
communicate with another program or online service.

In this project, our Python program communicates with NewsAPI. Instead of
visiting a news website manually, the Python code sends a web request to NewsAPI
and receives structured data back.

The data comes back as JSON, which is a common format for API responses. JSON
looks similar to Python dictionaries and lists, so Python programs can process
it easily.

## 2. What Is an API Key?

An API key is a secret value used to identify the person or application making
an API request.

NewsAPI uses the key to know which account is making the request. This helps the
service apply usage limits, block misuse, and track which applications are using
the API.

An API key is not the same as a normal password, but it should still be treated
like a secret.

## 3. Why API Keys Should Never Be Committed to GitHub

If you write an API key directly in your source code and push that code to
GitHub, the key may become visible to other people.

This is dangerous because someone else could copy your key and use it as if
they were you. Depending on the service, this could lead to:

- Your free quota being used up.
- Your account being rate limited or blocked.
- Unexpected costs on paid services.
- Your application or account being associated with someone else's misuse.

Even if you delete the key later, Git keeps a history of previous commits. A
secret may still be recoverable from the repository history.

## 4. How Attackers Search GitHub for Exposed Secrets

Attackers do not need to manually read every repository. They can use automated
tools that search GitHub for patterns that look like secrets.

For example, they may search for names such as:

- `API_KEY`
- `SECRET_KEY`
- `ACCESS_TOKEN`
- `NEWS_API_KEY`

They may also search for code that connects to popular online services. If a
real key is found, it can be copied and abused very quickly.

This is why developers should assume that anything committed to a public
repository can be seen by other people.

## 5. How Environment Variables Help Protect Secrets

An environment variable is a value stored outside the source code and made
available to a running program.

The secure version of this project uses a `.env` file to store the API key:

```text
NEWS_API_KEY=your_real_api_key_here
```

The `python-dotenv` package loads this value into the program. The Python code
can then read it using:

```python
os.getenv("NEWS_API_KEY")
```

This is safer because the API key is not written directly in the Python file.
The `.gitignore` file tells Git to ignore `.env`, which helps prevent the real
key from being committed to GitHub.

Important: a `.env` file still contains a secret. Do not share it, upload it, or
send it to other people.

## 6. How to Run the Project

### Step 1: Install Python

Make sure Python is installed. You can check by running:

```bash
python --version
```

On some systems, the command may be:

```bash
python3 --version
```

### Step 2: Install the Required Packages

Install the packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

If your system uses `python3`, you may need:

```bash
python3 -m pip install -r requirements.txt
```

### Step 3: Get a NewsAPI Key

Create an account at:

```text
https://newsapi.org/
```

After signing in, copy your API key.

### Running Version 1: Insecure Example

Open `news_insecure.py` and find this line:

```python
NEWS_API_KEY = "your_api_key_here"
```

For a classroom demonstration only, replace the placeholder with a real key and
run:

```bash
python news_insecure.py
```

This version works, but it is unsafe because the secret is inside the source
code. Do not commit a real key to GitHub.

### Running Version 2: Secure Example

Copy `.env.example` and rename the copy to `.env`.

Edit `.env` so it contains your real key:

```text
NEWS_API_KEY=your_real_api_key_here
```

Then run:

```bash
python news_secure.py
```

The secure version loads the key from `.env` using `python-dotenv`.

## 7. Authentication vs Authorisation

Authentication means proving who you are or which application is making the
request.

In this project, the API key authenticates the request to NewsAPI. It says,
"This request is using this account's key."

Authorisation means deciding what an authenticated user or application is
allowed to do.

For example, NewsAPI may authorise one account to make a certain number of
requests per day, while another paid account may be allowed to make more
requests or access extra features.

In simple terms:

- Authentication asks: "Who are you?"
- Authorisation asks: "What are you allowed to do?"

## Files in This Project

- `news_insecure.py`: Demonstrates the risky hard-coded API key approach.
- `news_secure.py`: Demonstrates loading the key from an environment variable.
- `.env.example`: Shows the format of the local `.env` file.
- `.gitignore`: Prevents `.env` and Python cache files from being committed.
- `requirements.txt`: Lists the Python packages needed by the project.

## Classroom Discussion Questions

1. Why is `news_insecure.py` risky even if the repository is private?
2. Why should `.env` be ignored by Git?
3. What could happen if someone else uses your API key?
4. What is the difference between hiding a key and deleting a leaked key?
5. Which part of this project demonstrates authentication?
