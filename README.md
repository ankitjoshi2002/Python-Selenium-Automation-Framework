# Selenium Pytest Automation Framework

![Selenium Tests](https://github.com/ankitjoshi2002/Python-Selenium-Automation-Framework/actions/workflows/selenium-tests.yml/badge.svg)

A UI test automation framework for a login page, built with **Python, Selenium and Pytest** using the **Page Object Model (POM)**. Tests run locally, inside **Docker**, and automatically on every push through **GitHub Actions**.

**Application under test:** https://practicetestautomation.com/practice-test-login/

## Tech stack

- Python 3.12
- Selenium WebDriver
- Pytest and pytest-html
- Docker
- GitHub Actions (CI)

## Project structure

```
LoginScript/
├── base/
│   └── base_page.py        # Common Selenium actions (click, type, wait, read text)
├── pages/
│   └── login_page.py       # Login page actions and assertions
├── locator/
│   └── login_locator.py    # Element locators for the login page
├── tests/
│   └── test_login.py       # Login test cases
├── utils/
│   ├── config_reader.py    # Reads values from config.ini
│   └── logger.py           # File logger
├── .github/workflows/
│   └── selenium-tests.yml  # CI pipeline
├── config.ini              # Base URL and test credentials
├── conftest.py             # Driver fixture and report settings
├── pytest.ini              # Pytest options
├── requirements.txt
├── Dockerfile
└── .dockerignore
```

## Design

- **Page Object Model:** locators, page actions and tests are kept in separate layers, so a UI change is fixed in one place.
- **BasePage:** shared wait-and-act helpers built on explicit waits, which avoids fixed sleeps.
- **Configuration:** the URL and credentials come from `config.ini`, not from the test code.
- **Logging:** every page action is written to `logs/test_run.log`.
- **Reporting:** each run produces a timestamped, self-contained HTML report in `reports/`.
- **Headless mode:** setting `HEADLESS=true` runs Chrome without a window, which is how it runs in Docker and CI.

## Run locally

Requirements: Python 3.12 and Google Chrome.

```bash
git clone https://github.com/ankitjoshi2002/Python-Selenium-Automation-Framework.git
cd Python-Selenium-Automation-Framework
pip install -r requirements.txt
pytest
```

The HTML report appears in `reports/` and the log in `logs/`.

## Run with Docker

Requirement: Docker Desktop.

```bash
docker build -t selenium-tests .
docker run --rm selenium-tests
```

To save the reports and logs on your machine:

```bash
docker run --rm -v "${PWD}/reports:/app/reports" -v "${PWD}/logs:/app/logs" selenium-tests
```

## CI/CD pipeline

The workflow in `.github/workflows/selenium-tests.yml` runs on every push to `main` and on every pull request into `main`:

1. Checks out the code
2. Builds the Docker image
3. Runs the tests in the container
4. Uploads the HTML report and logs as a downloadable artifact named `test-results`

To view a report, open the run in the **Actions** tab and download `test-results` from the **Artifacts** section.

## Author

Ankit Joshi
GitHub: [ankitjoshi2002](https://github.com/ankitjoshi2002)