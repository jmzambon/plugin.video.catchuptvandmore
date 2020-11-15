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
from codequick import Script, utils
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
    'tv5mondeafrique': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/wo_replay.py
        'callback': 'replay_bridge',
=======
        'route': '/resources/lib/channels/wo/tv5mondeafrique:list_categories',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/wo_replay.py
        'label': 'TV5Monde Afrique',
        'thumb': 'channels/wo/tv5mondeafrique.png',
        'fanart': 'channels/wo/tv5mondeafrique_fanart.jpg',
        'enabled': True,
        'order': 1
    },
    'arte': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/wo_replay.py
        'callback': 'replay_bridge',
=======
        'route': '/resources/lib/channels/wo/arte:list_categories',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/wo_replay.py
        'label': 'Arte (' + utils.ensure_unicode(Script.setting['arte.language']) + ')',
        'thumb': 'channels/wo/arte.png',
        'fanart': 'channels/wo/arte_fanart.jpg',
        'enabled': True,
        'order': 3
    },
    'france24': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/wo_replay.py
        'callback': 'replay_bridge',
=======
        'route': '/resources/lib/channels/wo/france24:root_catchup_tv',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/wo_replay.py
        'label': 'France 24 (' + utils.ensure_unicode(Script.setting['france24.language']) + ')',
        'thumb': 'channels/wo/france24.png',
        'fanart': 'channels/wo/france24_fanart.jpg',
        'enabled': True,
        'order': 4
    },
    'nhkworld': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/wo_replay.py
        'callback': 'replay_bridge',
=======
        'route': '/resources/lib/channels/wo/nhkworld:list_categories',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/wo_replay.py
        'label': 'NHK World (' + utils.ensure_unicode(Script.setting['nhkworld.language']) + ')',
        'thumb': 'channels/wo/nhkworld.png',
        'fanart': 'channels/wo/nhkworld_fanart.jpg',
        'enabled': True,
        'order': 5
    },
    'tv5monde': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/wo_replay.py
        'callback': 'replay_bridge',
=======
        'route': '/resources/lib/channels/wo/tv5monde:list_categories',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/wo_replay.py
        'label': 'TV5Monde',
        'thumb': 'channels/wo/tv5monde.png',
        'fanart': 'channels/wo/tv5monde_fanart.jpg',
        'enabled': True,
        'order': 6
    },
    'tivi5monde': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/wo_replay.py
        'callback': 'replay_bridge',
=======
        'route': '/resources/lib/channels/wo/tivi5monde:list_categories',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/wo_replay.py
        'label': 'Tivi 5Monde',
        'thumb': 'channels/wo/tivi5monde.png',
        'fanart': 'channels/wo/tivi5monde_fanart.jpg',
        'enabled': True,
        'order': 7
    },
    'bvn': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/wo_replay.py
        'callback': 'replay_bridge',
=======
        'route': '/resources/lib/channels/wo/bvn:list_days',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/wo_replay.py
        'label': 'BVN',
        'thumb': 'channels/wo/bvn.png',
        'fanart': 'channels/wo/bvn_fanart.jpg',
        'enabled': True,
        'order': 8
    },
    'arirang': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/wo_replay.py
        'callback': 'replay_bridge',
=======
        'route': '/resources/lib/channels/wo/arirang:list_categories',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/wo_replay.py
        'label': 'Arirang (아리랑)',
        'thumb': 'channels/wo/arirang.png',
        'fanart': 'channels/wo/arirang_fanart.jpg',
        'enabled': True,
        'order': 11
    },
    'beinsports': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/wo_replay.py
        'callback': 'replay_bridge',
=======
        'route': '/resources/lib/channels/wo/beinsports:list_sites',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/wo_replay.py
        'label': 'Bein Sports',
        'thumb': 'channels/wo/beinsports.png',
        'fanart': 'channels/wo/beinsports_fanart.jpg',
        'enabled': True,
        'order': 13
    },
    'afriquemedia': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/wo_replay.py
        'callback': 'replay_bridge',
=======
        'route': '/resources/lib/channels/wo/afriquemedia:list_categories',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/wo_replay.py
        'label': 'Afrique Media',
        'thumb': 'channels/wo/afriquemedia.png',
        'fanart': 'channels/wo/afriquemedia_fanart.jpg',
        'enabled': True,
        'order': 20
    },
    'channelnewsasia': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/wo_replay.py
        'callback': 'replay_bridge',
=======
        'route': '/resources/lib/channels/wo/channelnewsasia:list_categories',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/wo_replay.py
        'label': 'Channel NewsAsia',
        'thumb': 'channels/wo/channelnewsasia.png',
        'fanart': 'channels/wo/channelnewsasia_fanart.jpg',
        'enabled': True,
        'order': 23
    },
    'rt': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/wo_replay.py
        'callback': 'replay_bridge',
=======
        'route': '/resources/lib/channels/wo/rt:list_categories',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/wo_replay.py
        'label': 'RT (' + utils.ensure_unicode(Script.setting['rt.language']) + ')',
        'thumb': 'channels/wo/rt.png',
        'fanart': 'channels/wo/rt_fanart.jpg',
        'available_languages': ['FR', 'EN'],
        'enabled': True,
        'order': 24
    },
    'africa24': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/wo_replay.py
        'callback': 'replay_bridge',
=======
        'route': '/resources/lib/channels/wo/africa24:list_categories',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/wo_replay.py
        'label': 'Africa 24',
        'thumb': 'channels/wo/africa24.png',
        'fanart': 'channels/wo/africa24_fanart.jpg',
        'enabled': True,
        'order': 25
    },
    'tv5mondeplus': {
        'route': '/resources/lib/channels/wo/tv5mondeplus:list_categories',
        'label': 'TV5Monde Plus',
        'thumb': 'channels/wo/tv5mondeplus.png',
        'fanart': 'channels/wo/tv5mondeplus_fanart.jpg',
        'enabled': False,
        'order': 26
    }
}
