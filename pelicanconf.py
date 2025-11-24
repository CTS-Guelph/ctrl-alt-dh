AUTHOR = 'cmiya'
SITENAME = 'CTRL+ALT+DH'
SITEURL = ""
#https://cts-guelph.github.io/ctrl-alt-dh/
PATH = "content"
ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages']

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Site Theme
THEME="custom-theme"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Contact Us", "ctrlaltdh@gmail.com"),
    ("CTS", "https://www.uoguelph.ca/arts/cts"),
)

# Social widget
SOCIAL = (
    ("Instagram", "@CtrlAltDH"),
    ("GitHub", "https://cmiya.github.io/ctrl-alt-dh/"),
)

DEFAULT_PAGINATION = 10

# Include static files like favicon
STATIC_PATHS = ['static']

# Make sure they’re copied to the root of the output
EXTRA_PATH_METADATA = {
    'static/favicon.ico': {'path': 'favicon.ico'},
    'static/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'static/favicon-16x16.png': {'path': 'favicon-16x16.png'},
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Tags

# Generate tag pages automatically
TAG_SAVE_AS = 'tag/{slug}.html'     # URL for each tag page
TAG_URL = 'tag/{slug}.html'

# Generate a tags index page listing all tags (optional)
TAGS_SAVE_AS = 'tags.html'          # The tags index page URL

# Save pages at the top level instead of /pages/
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Menu

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = [
    ('Issues', [
        ('Issue 0', '/issue-0.html'),
        ('Issue 1: Creating CTRL-ALT-DH', '/issue-1.html'),
        ('Issue 2: Digital Dilemmas', '/issue-2.html')
    ]),
    ('Submissions', [
        ('Guidelines', '/guidelines.html'),
        ('CFP', '/cfp-2025.html')
    ]),
    ('Browse', '/tags.html'),
    ('News', '/category/news.html'),
]


DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives', 'tags', 'news']
