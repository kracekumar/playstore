PlayStore
----
Python library to access Android App details from Google Play Store.

Install
----
`pip install playstore`

Usagae
----
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

# App Author
app.author

# App Description 
app.description

# App category
app.category

# Number of stars
app.score

# Total Downloads
app.download_count

# Last updated
app.updated_at

# Size of the app
app.size

# Minimum requirement
app.minimum_requirement

# Current Version
app.current_version

# Content rating
app.content_rating

# Short description
app.short_description()

# Stars counts
app.star_counts()

# Additional information
app.additional_information()
```

