from datetime import datetime

CURRENT_YEAR = datetime.now().year

AUTHOR = 'Sarah Rogue'
SITENAME = 'Sarah\'s Website'

PATH = 'content'
OUTPUT_PATH = 'docs'

TIMEZONE = 'America/Indiana/Indianapolis'

DEFAULT_LANG = 'en-GB'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

DEFAULT_PAGINATION = 1

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

ARTICLE_URL = '{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{slug}/index.html'
DEFAULT_CATEGORY = 'other'
EXTRA_PATH_METADATA = {
    'images/favicons/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'images/favicons/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'images/favicons/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'images/favicons/favicon.ico': {'path': 'favicon.ico'},
    'images/favicons/favicon.svg': {'path': 'favicon.svg'},
    'images/favicons/manifest.json': {'path': 'manifest.json'},
}
FONT_AWESOME = 9208356911
HOSTING_PROVIDER = 'Cloudflare'
HOSTING_PROVIDER_URL = 'https://www.cloudflare.com/'
LICENSE = 'Attribution-NonCommercial-NoDerivatives 4.0 International'
LICENSE_URL = 'https://creativecommons.org/licenses/by-nc-nd/4.0/'
OVERRIDE_CSS = 'styles.css'
PLUGIN_PATHS = ['replit']
PLUGINS = ['asciidoc_reader', 'sitemap']
STATIC_PATHS = ['images', 'src', 'robots.txt', 'css']
SUMMARY_MAX_PARAGRAPHS = 1
THEME = 'WhatsTheScoop'
TWITTER_USERNAME = 'SarahRogue81'
USE_FOLDER_AS_CATEGORY = False

# for sitemap plugin
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'never',
    }
}
