from setuptools import setup, find_packages
import sys, os

version = '0.1.1'

setup(name='playstore',
      version=version,
      description="Python library to access Android App details from Google Play Store.",
      long_description="""\
      ```
from playstore import PlayStore
app = PlayStore()
# Fetch the HTML and set appropriate attributes
app.fetch_details(url='https://play.google.com/store/apps/details?id=com.instagram.android&hl=en')
```
or

```
from playstore import PlayStore
app = PlayStore(url='https://play.google.com/store/apps/details?id=com.instagram.android&hl=en')
# Fetch the HTML and set appropriate attributes
app.fetch_details()
```

Some of the attributes and methods

```
# App Name
app.name
# u'Instagram'

# App Author
app.author
# u'Instagram'

# App Description 
app.description
"""
u"Over 130 million users love Instagram!It's a simple way to capture and share the world's moments on your Android.Customize your photos and videos with one of several gorgeous and custom built filter effects. Transform everyday #moments into works of art you'll want to share with friends and family.Share your photos and video in a simple photo stream with friends to see - and follow your friends' photos with the click of a single button. Every day you open up Instagram, you'll see new photos from your closest friends, and creative people from around the world.Features\u2022 100% free custom designed filters: XPro-II, Earlybird, Rise, Amaro, Hudson, Lo-fi, Sutro, Toaster, Brannan, Inkwell, Walden, Hefe, Nashville, 1977, and others.\u2022 Linear and Radial Tilt-Shift blur effects for extra depth of field.\u2022 Instant sharing to Facebook, Twitter, Flickr, Tumblr and Foursquare\u2022 Unlimited uploads\u2022 Interact with friends through giving & receiving likes and comments\u2022 Works with Android versions 2.2 and above that support OpenGL ES 2\u2022 And much much more\u2026"
"""

# App category
app.category
# [u'Social']

# Number of stars
app.score
# 4.6

# Total Downloads
app.download_count
# 5860284

# Last updated
app.updated_at
# u'August 7, 2013'

# Size of the app
app.size
# u'16M'

# Minimum requirement
app.minimum_requirement
# u'2.2 and up'

# Current Version
app.current_version
# u'4.1.2'

# Content rating
app.content_rating
# u'Medium Maturity'

# Short description
app.short_description()
# u"Over 130 million users love Instagram!It's a simple way to capture and share the world's moments on your Android"

# Stars counts
app.star_counts()
# {1: 128622, 2: 67410, 3: 275395, 4: 1064291, 5: 4324566}

# Additional information
app.additional_information()
"""
{u' Contact Developer ': [{u"Visit Developer's Website": 'https://www.google.com/url?q=http://help.instagram.com/&sa=D&usg=AFQjCNHo-YuLmFli_JMEA_Z1aBJ2MiAtwA'},
  {u'Email Developer': 'mailto:android-support@instagram.com'},
  {u'Privacy Policy': 'https://www.google.com/url?q=http://instagram.com/legal/privacy/&sa=D&usg=AFQjCNFXcazflEOJDJqTIDBU0IqYmMSDUw'}],
 u'Content Rating': u'Medium Maturity',
 u'Current Version': u'4.1.2',
 u'Installs': u'100,000,000 - 500,000,000',
 u'Requires Android': u'2.2 and up',
 u'Size': u'16M',
 u'Updated': u'August 7, 2013'}
"""

# Thumbnails url
app.thumbnails_url()
"""
['https://lh4.ggpht.com/fc3aCOb6CPdISEl6YQbX0XtoJB2O5INjz5DcItUwj7v2wXauITvSDOE3CQV9ddpyIgc=h310',
 'https://lh6.ggpht.com/iwQ2FwqiTfCdSmEd7pEwiY9LmuJUGlCQxMWutOgIeR3FyrijAkChlCav1YcxG-dARg=h310',
 'https://lh3.ggpht.com/UHNye24rgfNkMp7WqwynUmVj0yrI343TaKt8rDzsqkUVBE9uJzSAW477J_5aUUen9Vc=h310',
 'https://lh4.ggpht.com/qN0SxQXKA_vZzsDGqFlGBXp34LbXAQbJqNI02IZtLQL19jt1YcS9ta8qC3owCnqsns0=h310',
 'https://lh3.ggpht.com/YM8j0yXpE9462iPPBTHiRvu2773qIISoq9s45dXeb63LN5fx7LuGb1sz488LhBbMlqQ=h310',
 'https://lh6.ggpht.com/BOXSriRyAuc4FwRmVGcWoK4a8sk2cLv-2iW5yJHg9PyHD7HXCFqfOA6qRqRU2-3Ofvw=h310']
"""

# Cover image url
app.coverimage_url()
# 'https://lh3.ggpht.com/vFpQP39LB60dli3n-rJnVvTM07dsvIzxrCL5xMiy1V4GV4unC1ifXkUExQ4N-DBCKwI=w300'

# Thumbnails content and details
app.thumbnails()

"""
[
      {
            u'content': '...', # image content is discarded
            u'src': 'https://lh4.ggpht.com/fc3aCOb6CPdISEl6YQbX0XtoJB2O5INjz5DcItUwj7v2wXauITvSDOE3CQV9ddpyIgc=h310',
            u'content-length': '24576',
            u'content-type': 'image/jpeg',
            u'name': 'full-screenshot-0'
      }
]
"""

# cover image
app.coverimage()
"""
{
      u'content': '...', # image content is discarded
      u'content-length': '149221',
      u'content-type': 'image/png',
      u'name': 'cover-image',
      u'src': 'https://lh3.ggpht.com/vFpQP39LB60dli3n-rJnVvTM07dsvIzxrCL5xMiy1V4GV4unC1ifXkUExQ4N-DBCKwI=w300'
}
"""
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords=['Android', 'playstore'],
      author='Kracekumar',
      author_email='me@kracekumar.com',
      url='https://github.com/kracekumar/playstore',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
          'requests == 1.2.3',
          'beautifulsoup4'
      ],
      download_url = 'https://github.com/kracekumar/playstore/tarball/0.1.1',
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
