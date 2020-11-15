# -*- coding: utf-8 -*-
"""
    Catch-up TV & More
    Copyright (C) 2016  SylvainCecchetto

    This file is part of Catch-up TV & More.

    Catch-up TV & More is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    Catch-up TV & More is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with Catch-up TV & More; if not, write to the Free Software Foundation,
    Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

# The unicode_literals import only has
# an effect on Python 2.
# It makes string literals as unicode like in Python 3
from __future__ import unicode_literals
from codequick import Script
"""
The following dictionaries describe
the addon's tree architecture.
* Key: item id
* Value: item infos
    - route (folder)/resolver (playable URL): Callback function to run once this item is selected
    - thumb: Item thumb path relative to "media" folder
    - fanart: Item fanart path relative to "meia" folder
"""

menu = {
    'allocine': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/websites.py
        'callback': 'website_bridge',
=======
        'route': '/resources/lib/websites/allocine:website_root',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/websites.py
        'label': 'Allociné',
        'thumb': 'websites/allocine.png',
        'fanart': 'websites/allocine_fanart.jpg',
        'enabled': True,
        'order': 1
    },
    'tetesaclaques': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/websites.py
        'callback': 'website_bridge',
=======
        'route': '/resources/lib/websites/tetesaclaques:website_root',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/websites.py
        'label': 'Au pays des Têtes à claques',
        'thumb': 'websites/tetesaclaques.png',
        'fanart': 'websites/tetesaclaques_fanart.jpg',
        'enabled': True,
        'order': 2
    },
    'taratata': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/websites.py
        'callback': 'website_bridge',
=======
        'route': '/resources/lib/websites/taratata:website_root',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/websites.py
        'label': 'Taratata',
        'thumb': 'websites/taratata.png',
        'fanart': 'websites/taratata_fanart.jpg',
        'enabled': True,
        'order': 3
    },
    'noob': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/websites.py
        'callback': 'website_bridge',
=======
        'route': '/resources/lib/websites/noob:website_root',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/websites.py
        'label': 'Noob TV',
        'thumb': 'websites/noob.png',
        'fanart': 'websites/noob_fanart.jpg',
        'enabled': True,
        'order': 4
    },
    'culturepub': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/websites.py
        'callback': 'website_bridge',
=======
        'route': '/resources/lib/websites/culturepub:website_root',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/websites.py
        'label': 'Culturepub',
        'thumb': 'websites/culturepub.png',
        'fanart': 'websites/culturepub_fanart.jpg',
        'enabled': True,
        'order': 5
    },
    'autoplus': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/websites.py
        'callback': 'website_bridge',
=======
        'route': '/resources/lib/websites/autoplus:website_root',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/websites.py
        'label': 'Auto Plus',
        'thumb': 'websites/autoplus.png',
        'fanart': 'websites/autoplus_fanart.jpg',
        'enabled': True,
        'order': 6
    },
    'notrehistoirech': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/websites.py
        'callback': 'website_bridge',
=======
        'route': '/resources/lib/websites/notrehistoirech:website_root',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/websites.py
        'label': 'Notre Histoire',
        'thumb': 'websites/notrehistoirech.png',
        'fanart': 'websites/notrehistoirech_fanart.jpg',
        'enabled': True,
        'order': 7
    },
    '30millionsdamis': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/websites.py
        'callback': 'website_bridge',
=======
        'route': '/resources/lib/websites/30millionsdamis:website_root',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/websites.py
        'label': '30 Millions d\'Amis',
        'thumb': 'websites/30millionsdamis.png',
        'fanart': 'websites/30millionsdamis_fanart.jpg',
        'enabled': True,
        'order': 8
    },
    'elle': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/websites.py
        'callback': 'website_bridge',
=======
        'route': '/resources/lib/websites/elle:website_root',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/websites.py
        'label': 'Elle',
        'thumb': 'websites/elle.png',
        'fanart': 'websites/elle_fanart.jpg',
        'enabled': True,
        'order': 9
    },
    'nytimes': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/websites.py
        'callback': 'website_bridge',
=======
        'route': '/resources/lib/websites/nytimes:website_root',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/websites.py
        'label': 'New York Times',
        'thumb': 'websites/nytimes.png',
        'fanart': 'websites/nytimes_fanart.jpg',
        'enabled': True,
        'order': 10
    },
    'fosdem': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/websites.py
        'callback': 'website_bridge',
=======
        'route': '/resources/lib/websites/fosdem:website_root',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/websites.py
        'label': 'Fosdem',
        'thumb': 'websites/fosdem.png',
        'fanart': 'websites/fosdem_fanart.jpg',
        'enabled': True,
        'order': 11
    },
    'ina': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/websites.py
        'callback': 'website_bridge',
=======
        'route': '/resources/lib/websites/ina:website_root',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/websites.py
        'label': 'Ina',
        'thumb': 'websites/ina.png',
        'fanart': 'websites/ina_fanart.jpg',
        'enabled': True,
        'order': 12
    },
    'onf': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/websites.py
        'callback': 'website_bridge',
=======
        'route': '/resources/lib/websites/onf:website_root',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/websites.py
        'label': 'Office National du Film du Canada',
        'thumb': 'websites/onf.png',
        'fanart': 'websites/onf_fanart.jpg',
        'enabled': True,
        'order': 13
    },
    'nfb': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/websites.py
        'callback': 'website_bridge',
=======
        'route': '/resources/lib/websites/nfb:website_root',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/websites.py
        'label': 'National Film Board Of Canada',
        'thumb': 'websites/nfb.png',
        'fanart': 'websites/nfb_fanart.jpg',
        'enabled': True,
        'order': 14
    },
    'marmiton': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/websites.py
        'callback': 'website_bridge',
=======
        'route': '/resources/lib/websites/marmiton:website_root',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/websites.py
        'label': 'Marmiton',
        'thumb': 'websites/marmiton.png',
        'fanart': 'websites/marmiton_fanart.jpg',
        'enabled': True,
        'order': 15
    },
    'lesargonautes': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/websites.py
        'callback': 'website_bridge',
=======
        'route': '/resources/lib/websites/lesargonautes:website_root',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/websites.py
        'label': 'Les Argonautes',
        'thumb': 'websites/lesargonautes.png',
        'fanart': 'websites/lesargonautes_fanart.jpg',
        'enabled': True,
        'order': 16
    },
    'nationalfff': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/websites.py
        'callback': 'website_bridge',
=======
        'route': '/resources/lib/websites/nationalfff:website_root',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/websites.py
        'label': 'National FFF',
        'thumb': 'websites/nationalfff.png',
        'fanart': 'websites/nationalfff_fanart.jpg',
        'enabled': True,
        'order': 17
    },
    'philharmoniedeparis': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/websites.py
        'callback': 'website_bridge',
=======
        'route': '/resources/lib/websites/philharmoniedeparis:website_root',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/websites.py
        'label': 'Philharmonie de Paris',
        'thumb': 'websites/philharmoniedeparis.png',
        'fanart': 'websites/philharmoniedeparis_fanart.jpg',
        'enabled': True,
        'order': 18
    }
}
