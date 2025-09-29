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
    ('github', 'https://github.com/SarahRogue81'),
    ('pandora', 'https://pandora.com/profile/SarahRogue81'),
    ('twitter', f'https://x.com/{TWITTER_USERNAME}'),
)
SOCIAL_CARD_NAME = 'social media'

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

ARTICLE_URL = '{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}/index.html'
AVATAR_MESSAGE = 'i\'m a geeky emo🖤 girl'
DEFAULT_CATEGORY = 'other'
EXTRA_PATH_METADATA = {
    'images/favicons/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'images/favicons/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'images/favicons/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'images/favicons/favicon.ico': {'path': 'favicon.ico'},
    'images/favicons/favicon.svg': {'path': 'favicon.svg'},
    'images/favicons/manifest.json': {'path': 'manifest.json'},
}
HIDE_AUTHORS = True
LICENSE = 'Attribution-NonCommercial-NoDerivatives 4.0 International'
LICENSE_URL = 'https://creativecommons.org/licenses/by-nc-nd/4.0/'
META_DESCRIPTION = f'{AUTHOR}\'s tech and gaming blog - with a little dry humour added in'
PLUGIN_PATHS = ['replit/pelican-plugins', 'replit']
PLUGINS = ['asciidoc_reader', 'sitemap']
STATIC_PATHS = ['images', 'src', 'robots.txt']
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
