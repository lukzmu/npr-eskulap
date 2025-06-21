import os
from datetime import datetime

from babel.dates import format_date

from core.repositories import Repository

# --- Site Data ---
SITEURL = os.getenv("SITEURL", default="https://eskulapbiskupiec.pl")
AUTHOR = "Lukasz Zmudzinski"
SITENAME = "Niepubliczna Przychodnia Rodzinna Eskulap w Biskupcu"
TIMEZONE = "Europe/Warsaw"
DEFAULT_LANG = "pl"
LOCALE = "pl_PL.UTF-8"

# --- Pelican Paths and Settings ---
PATH = "content"
THEME = "themes/core"
THEME_STATIC_DIR = "theme"
DEFAULT_PAGINATION = False
DELETE_OUTPUT_DIRECTORY = True
STATIC_PATHS = ["images", "extra/CNAME"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}

# --- JINJA ---
JINJA_FILTERS = {
    "format_date_localized": lambda date: format_date(date=date, format="long", locale=LOCALE),
}

# --- Feed Generation ---
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# --- Site Data ---
SITE_DATA: dict[str, dict | int] = {
    "year": datetime.now().year,
    "contact": Repository.load_data(data_path="data/contact.yml"),
    "home": Repository.load_data(data_path="data/home.yml"),
}
