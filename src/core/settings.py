import os

# --- Site Data ---
SITEURL = os.getenv("SITEURL", default="https://eskulapbiskupiec.pl")
AUTHOR = "Lukasz Zmudzinski"
SITENAME = "Niepubliczna Przychodnia Rodzinna w Biskupcu"
TIMEZONE = "Europe/Warsaw"
DEFAULT_LANG = "pl"

# --- Pelican Paths and Settings ---
PATH = "content"
# THEME = "themes/core"
# THEME_STATIC_DIR = "theme"
DEFAULT_PAGINATION = False
DELETE_OUTPUT_DIRECTORY = True
STATIC_PATHS = ["images", "extra/CNAME"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
}

# --- Feed Generation ---
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# --- Site Data ---
SITE_DATA = {}
