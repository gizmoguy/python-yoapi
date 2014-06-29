====================
Python YoApi Library
====================

YoApi docs - https://medium.com/@YoAppStatus/yo-developers-api-e7f2f0ec5c3c

You will need a YoApi API key to use this library, obtain one here - http://yoapi.justyo.co/

Usage
=====

Usage is simple::

    #!/usr/bin/env python

    from yoapi import yo

    yo = yo.api(API_KEY)
    yo.yoall()
