#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Tests for PlayStore """

import unittest
from playstore import PlayStore


class PlayStoreTestCase(unittest.TestCase):
    def setUp(self):
        self.app = PlayStore(url=u"https://play.google.com/store/apps/details?id=com.instagram.android&reviewId=Z3A6QU9xcFRPR01raGRERmE2U2xmRi1ReGltZWFvbTdaYmRkV0hnWmxiWEEtRHZsYkZjSGh6WndUeHFNOU5RZjUzRDlKQW9kUTU3OFBjbnVnLVlBa2xMbFE&hl=en")
        self.app.fetch_details()

    def test_attributes(self):
        # name
        self.assertMultiLineEqual(self.app.name, u'Instagram')
        desc = u"Over 130 million users love Instagram!It's a simple way to capture and share the world's moments on your Android.Customize your photos and videos with one of several gorgeous and custom built filter effects. Transform everyday moments into works of art you'll want to share with friends and family.Share your photos and video in a simple photo stream with friends to see - and follow your friends' photos with the click of a single button. Every day you open up Instagram, you'll see new photos from your closest friends, and creative people from around the world.Features\u2022 100% free custom designed filters: XPro-II, Earlybird, Rise, Amaro, Hudson, Lo-fi, Sutro, Toaster, Brannan, Inkwell, Walden, Hefe, Nashville, 1977, and others.\u2022 Linear and Radial Tilt-Shift blur effects for extra depth of field.\u2022 Instant sharing to Facebook, Twitter, Flickr, Tumblr and Foursquare\u2022 Unlimited uploads\u2022 Interact with friends through giving & receiving likes and comments\u2022 Works with Android versions 2.2 and above that support OpenGL ES 2\u2022 And much much more\u2026"
        # description
        self.assertMultiLineEqual(self.app.description, desc)
        # category
        self.assertEquals(self.app.category, [u'Social'])
        # Author
        self.assertMultiLineEqual(self.app.author, u'Instagram')
        # score
        self.assertGreaterEqual(self.app.score, 4.6)
        # Download count
        self.assertGreaterEqual(self.app.download_count, 5858841)
        # Size
        self.assertIsNotNone(self.app.size)
        # Updated at
        self.assertIsNotNone(self.app.updated_at)
        # current version
        self.assertIsNotNone(self.app.current_version)
        # Minimum requirement
        self.assertIsNotNone(self.app.minimum_requirement)
        # Content rating
        self.assertIsNotNone(self.app.content_rating)

    def test_short_description(self):
        self.assertLessEqual(len(self.app.description), self.app.short_description())

    def test_star_counts(self):
        d = self.app.star_counts()
        self.assertGreaterEqual(d[5], 1)

    def test_additional_information(self):
        d = self.app.additional_information()
        self.assertIsNotNone(d[u"Size"])

    def test_thumbnails_url(self):
        l = self.app.thumbnails_url()
        self.assertGreaterEqual(len(l), 1)

    def test_coverimage_url(self):
        url = self.app.coverimage_url()
        self.assertEquals(url[0:5], u'https')

    def test_thumbnails(self):
        l = self.app.thumbnails()
        self.assertGreaterEqual(len(l), 1)

    def test_coverimage(self):
        d = self.app.coverimage()
        self.assertEquals(d[u"name"], u"cover-image")
