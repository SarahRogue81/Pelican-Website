from datetime import datetime

CURRENT_YEAR = datetime.now().year

AUTHOR = 'Sarah Rogue'
SITENAME = 'Sarah\'s Website'
SITESUBTITLE = f'Welcome to the blog of <span class="w3-tag">{AUTHOR}</span>'

PATH = 'content'
OUTPUT_PATH = 'docs'

TIMEZONE = 'America/Indiana/Indianapolis'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

# Blogroll
LINKS = (
    ("GitHub", "https://github.com/SarahRogue81"),
)

TWITTER_USERNAME = 'SarahRogue81'
# Social widget
SOCIAL = (
    ('fa-brands fa-pandora w3-text-blue', 'https://pandora.com/profile/SarahRogue81'),
    ('fa-brands fa-twitter w3-text-blue', f'https://x.com/{TWITTER_USERNAME}'),
)
SOCIAL_WIDGET_NAME = 'social media'

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

ARTICLE_URL = '{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}/index.html'
AVATAR_IMAGE = '/images/avatar.webp'
AVATAR_MESSAGE = 'i\'m a geeky emo🖤 girl'
DEFAULT_CATEGORY = 'other'
EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'}
}
LICENSE = 'Attribution-NonCommercial-NoDerivatives 4.0 International'
LICENSE_URL = 'https://creativecommons.org/licenses/by-nc-nd/4.0/'
PLUGIN_PATHS = ['replit/pelican-plugins', 'replit']
PLUGINS = ['asciidoc_reader', 'sitemap']
PORT = 5000
STATIC_PATHS = ['images', 'LICENSE', 'src', 'robots.txt']
SUMMARY_MAX_PARAGRAPHS = 1
THEME = 'W3.CSS-Template4Pelican'
USE_FOLDER_AS_CATEGORY = False

# for sitemap plugin
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5
    },
    "changefreqs": {
        "articles": "daily",
        "indexes": "daily",
        "pages": "never"
    }
}
