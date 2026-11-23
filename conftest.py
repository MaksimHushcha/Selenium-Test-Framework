import dotenv

dotenv.load_dotenv()

# conftest.py
pytest_plugins = [
    "fixtures.browser",      # driver + pytest_runtest_makereport
    "fixtures.pages_fixtures",        # all Page Object fixtures
    "fixtures.localization", # pytest_addoption + pytest_generate_tests
    "fixtures.api_seeding"
]
