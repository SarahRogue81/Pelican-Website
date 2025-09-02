from datetime import datetime

CURRENT_YEAR = datetime.now().year
 
AUTHOR = 'Sarah Rogue'
SITENAME = 'Sarah\'s Website'
SITESUBTITLE = f'Welcome to the blog of <span class="w3-tag">{AUTHOR}</span>'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'docs'

TIMEZONE = 'America/Indiana/Indianapolis'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("GitHub", "https://github.com/SarahRogue81"),
)

TWITTER_USERNAME = 'SarahRogue81'
# Social widget
SOCIAL = (
    ('fa-brands fa-twitter w3-text-blue', f'https://x.com/{TWITTER_USERNAME}'),
)
SOCIAL_WIDGET_NAME = 'social media'

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

AVATAR_IMAGE = '/images/avatar.webp'
AVATAR_MESSAGE = 'i\'m a geek emo🖤 girl'
DEFAULT_CATEGORY = 'other'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
EXTRA_PATH_METADATA = {
    'images/favicon.ico': {'path': 'favicon.ico'}
}
LICENSE = 'Attribution-NonCommercial-NoDerivatives 4.0 International'
LICENSE_URL = 'https://creativecommons.org/licenses/by-nc-nd/4.0/'
MENUITEMS = (
        ('about', '/about.html'),
)
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['asciidoc_reader']
PORT = 1313
STATIC_PATHS = ['images', 'LICENSE']
SUMMARY_MAX_PARAGRAPHS = 1
THEME = 'W3.CSS-Template4Pelican'
USE_FOLDER_AS_CATEGORY = False

