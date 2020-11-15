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
    'brf': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/be_replay.py
        'callback': 'replay_bridge',
=======
        'route': '/resources/lib/channels/be/brf:list_categories',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/be_replay.py
        'label': 'BRF Mediathek',
        'thumb': 'channels/be/brf.png',
        'fanart': 'channels/be/brf_fanart.jpg',
        'enabled': True,
        'order': 1
    },
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/be_replay.py
    'rtl_tvi': {
        'callback': 'replay_bridge',
        'label': 'RTL TVI',
        'thumb': 'channels/be/rtltvi.png',
        'fanart': 'channels/be/rtltvi_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe',
        'enabled': True,
        'order': 2
    },
    'plug_rtl': {
        'callback': 'replay_bridge',
        'label': 'PLUG RTL',
        'thumb': 'channels/be/plugrtl.png',
        'fanart': 'channels/be/plugrtl_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe',
        'enabled': True,
        'order': 3
    },
    'club_rtl': {
        'callback': 'replay_bridge',
        'label': 'CLUB RTL',
        'thumb': 'channels/be/clubrtl.png',
        'fanart': 'channels/be/clubrtl_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe',
        'enabled': True,
        'order': 4
    },
    'vrt': {
        'callback': 'replay_bridge',
=======
    'rtlplay': {
        'route': '/resources/lib/channels/be/rtlplaybe:rtlplay_root',
        'label': 'RTLplay',
        'thumb': 'channels/be/rtlplay.png',
        'fanart': 'channels/be/rtlplay_fanart.jpg',
        'enabled': True,
        'order': 2
    },
    'vrt': {
        'route': '/resources/lib/channels/be/vrt:list_root',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/be_replay.py
        'label': 'VRT NU',
        'thumb': 'channels/be/vrt.png',
        'fanart': 'channels/be/vrt_fanart.jpg',
        'enabled': True,
        'order': 5
    },
    'telemb': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/be_replay.py
        'callback': 'replay_bridge',
=======
        'route': '/resources/lib/channels/be/telemb:list_programs',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/be_replay.py
        'label': 'Télé MB',
        'thumb': 'channels/be/telemb.png',
        'fanart': 'channels/be/telemb_fanart.jpg',
        'enabled': True,
        'order': 6
    },
    'rtc': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/be_replay.py
        'callback': 'replay_bridge',
=======
        'route': '/resources/lib/channels/be/rtc:list_categories',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/be_replay.py
        'label': 'RTC Télé Liège',
        'thumb': 'channels/be/rtc.png',
        'fanart': 'channels/be/rtc_fanart.jpg',
        'enabled': True,
        'order': 7
    },
    'auvio': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/be_replay.py
        'callback': 'replay_bridge',
=======
        'route': '/resources/lib/channels/be/rtbf:list_categories',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/be_replay.py
        'label': 'RTBF Auvio',
        'thumb': 'channels/be/auvio.png',
        'fanart': 'channels/be/auvio_fanart.jpg',
        'enabled': True,
        'order': 8
    },
    'tvlux': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/be_replay.py
        'callback': 'replay_bridge',
=======
        'route': '/resources/lib/channels/be/tvlux:list_categories',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/be_replay.py
        'label': 'TV Lux',
        'thumb': 'channels/be/tvlux.png',
        'fanart': 'channels/be/tvlux_fanart.jpg',
        'enabled': True,
        'order': 9
    },
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/be_replay.py
    'rtl_info': {
        'callback': 'replay_bridge',
        'label': 'RTL INFO',
        'thumb': 'channels/be/rtlinfo.png',
        'fanart': 'channels/be/rtlinfo_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe',
        'enabled': True,
        'order': 10
    },
    'bel_rtl': {
        'callback': 'replay_bridge',
        'label': 'BEL RTL',
        'thumb': 'channels/be/belrtl.png',
        'fanart': 'channels/be/belrtl_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe',
        'enabled': True,
        'order': 11
    },
    'contact': {
        'callback': 'replay_bridge',
        'label': 'Contact',
        'thumb': 'channels/be/contact.png',
        'fanart': 'channels/be/contact_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe',
        'enabled': True,
        'order': 12
    },
    'bx1': {
        'callback': 'replay_bridge',
=======
    'bx1': {
        'route': '/resources/lib/channels/be/bx1:list_programs',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/be_replay.py
        'label': 'BX1',
        'thumb': 'channels/be/bx1.png',
        'fanart': 'channels/be/bx1_fanart.jpg',
        'enabled': True,
        'order': 13
    },
    'nrjhitstvbe': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/be_replay.py
        'callback': 'replay_bridge',
=======
        'route': '/resources/lib/channels/be/nrjhitstvbe:list_videos',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/be_replay.py
        'label': 'NRJ Hits TV',
        'thumb': 'channels/be/nrjhitstvbe.png',
        'fanart': 'channels/be/nrjhitstvbe_fanart.jpg',
        'enabled': True,
        'order': 17
    },
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/be_replay.py
    'rtl_sport': {
        'callback': 'replay_bridge',
        'label': 'RTL Sport',
        'thumb': 'channels/be/rtlsport.png',
        'fanart': 'channels/be/rtlsport_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe',
        'enabled': True,
        'order': 18
    },
    'tvcom': {
        'callback': 'replay_bridge',
=======
    'tvcom': {
        'route': '/resources/lib/channels/be/tvcom:list_categories',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/be_replay.py
        'label': 'TV Com',
        'thumb': 'channels/be/tvcom.png',
        'fanart': 'channels/be/tvcom_fanart.jpg',
        'enabled': True,
        'order': 19
    },
    'canalc': {
<<<<<<< HEAD:plugin.video.catchuptvandmore/resources/lib/skeletons/be_replay.py
        'callback': 'replay_bridge',
        'label': 'Canal C',
        'thumb': 'channels/be/canalc.png',
        'fanart': 'channels/be/canalc_fanart.jpg',
        'module': 'resources.lib.channels.be.canalc',
=======
        'route': '/resources/lib/channels/be/canalc:list_programs',
        'label': 'Canal C',
        'thumb': 'channels/be/canalc.png',
        'fanart': 'channels/be/canalc_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3:resources/lib/skeletons/be_replay.py
        'enabled': True,
        'order': 20
    }
}
