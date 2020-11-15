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
<<<<<<< HEAD
    - callback: Callback function to run once this item is selected
    - thumb: Item thumb path relative to "media" folder
    - fanart: Item fanart path relative to "meia" folder
    - module: Item module to load in order to work (like 6play.py)
=======
    - route (folder)/resolver (playable URL): Callback function to run once this item is selected
    - thumb: Item thumb path relative to "media" folder
    - fanart: Item fanart path relative to "meia" folder
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
"""

menu = {
    'ectv': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'ECTV',
        'thumb': 'channels/et/ectv.png',
        'fanart': 'channels/et/ectv_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'ECTV',
        'thumb': 'channels/et/ectv.png',
        'fanart': 'channels/et/ectv_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 1
    },
    'amma': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'Amhara TV',
        'thumb': 'channels/et/amma.png',
        'fanart': 'channels/et/amma_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'Amhara TV',
        'thumb': 'channels/et/amma.png',
        'fanart': 'channels/et/amma_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 2
    },
    'fbctv': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'Fana TV',
        'thumb': 'channels/et/fbctv.png',
        'fanart': 'channels/et/fbctv_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'Fana TV',
        'thumb': 'channels/et/fbctv.png',
        'fanart': 'channels/et/fbctv_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 3
    },
    'walta': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'Walta TV',
        'thumb': 'channels/et/walta.png',
        'fanart': 'channels/et/walta_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'Walta TV',
        'thumb': 'channels/et/walta.png',
        'fanart': 'channels/et/walta_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 4
    },
    'etvz': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'EBC ZENA',
        'thumb': 'channels/et/etvz.png',
        'fanart': 'channels/et/etvz_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'EBC ZENA',
        'thumb': 'channels/et/etvz.png',
        'fanart': 'channels/et/etvz_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 5
    },
    'etvm': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'EBC MEZINAGNA',
        'thumb': 'channels/et/etvm.png',
        'fanart': 'channels/et/etvz_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'EBC MEZINAGNA',
        'thumb': 'channels/et/etvm.png',
        'fanart': 'channels/et/etvz_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 6
    },
    'etvq': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'EBC QUANQUAWOCH',
        'thumb': 'channels/et/etvq.png',
        'fanart': 'channels/et/etvq_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'EBC QUANQUAWOCH',
        'thumb': 'channels/et/etvq.png',
        'fanart': 'channels/et/etvq_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 7
    },
    'ltv': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'LTV',
        'thumb': 'channels/et/ltv.png',
        'fanart': 'channels/et/ltv_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'LTV',
        'thumb': 'channels/et/ltv.png',
        'fanart': 'channels/et/ltv_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 8
    },
    'arts': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'ARTS TV',
        'thumb': 'channels/et/arts.png',
        'fanart': 'channels/et/arts_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'ARTS TV',
        'thumb': 'channels/et/arts.png',
        'fanart': 'channels/et/arts_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 9
    },
    'moe': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'MoE',
        'thumb': 'channels/et/moe.png',
        'fanart': 'channels/et/moe_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'MoE',
        'thumb': 'channels/et/moe.png',
        'fanart': 'channels/et/moe_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 10
    },
    'nahoo': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'Nahoo TV',
        'thumb': 'channels/et/nahoo.png',
        'fanart': 'channels/et/nahoo_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'Nahoo TV',
        'thumb': 'channels/et/nahoo.png',
        'fanart': 'channels/et/nahoo_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 11
    },
    'obn': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'OBN',
        'thumb': 'channels/et/obn.png',
        'fanart': 'channels/et/obn_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'OBN',
        'thumb': 'channels/et/obn.png',
        'fanart': 'channels/et/obn_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 12
    },
    'obs': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'OBS',
        'thumb': 'channels/et/obs.png',
        'fanart': 'channels/et/obs_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'OBS',
        'thumb': 'channels/et/obs.png',
        'fanart': 'channels/et/obs_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 13
    },
    'tigrai': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'Tigrai TV',
        'thumb': 'channels/et/tigrai.png',
        'fanart': 'channels/et/tigrai_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'Tigrai TV',
        'thumb': 'channels/et/tigrai.png',
        'fanart': 'channels/et/tigrai_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 14
    },
    'jtv': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'JTV ETHIOPIA',
        'thumb': 'channels/et/jtv.png',
        'fanart': 'channels/et/jtv_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'JTV ETHIOPIA',
        'thumb': 'channels/et/jtv.png',
        'fanart': 'channels/et/jtv_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 15
    },
    'esat': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'ESAT',
        'thumb': 'channels/et/esat.png',
        'fanart': 'channels/et/esat_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'ESAT',
        'thumb': 'channels/et/esat.png',
        'fanart': 'channels/et/esat_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 16
    },
    'omn': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'OMN',
        'thumb': 'channels/et/omn.png',
        'fanart': 'channels/et/omn_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'OMN',
        'thumb': 'channels/et/omn.png',
        'fanart': 'channels/et/omn_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 17
    },
    'aleph': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'Aleph TV',
        'thumb': 'channels/et/aleph.png',
        'fanart': 'channels/et/aleph_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'Aleph TV',
        'thumb': 'channels/et/aleph.png',
        'fanart': 'channels/et/aleph_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 18
    },
    'bisrat': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'Bisrat TV',
        'thumb': 'channels/et/bisrat.png',
        'fanart': 'channels/et/bisrat_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'Bisrat TV',
        'thumb': 'channels/et/bisrat.png',
        'fanart': 'channels/et/bisrat_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 19
    },
    'onn': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'ONN TV',
        'thumb': 'channels/et/onn.png',
        'fanart': 'channels/et/onn_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'ONN TV',
        'thumb': 'channels/et/onn.png',
        'fanart': 'channels/et/onn_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 20
    },
    'dws': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'DW TV',
        'thumb': 'channels/et/dws.png',
        'fanart': 'channels/et/dws_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'DW TV',
        'thumb': 'channels/et/dws.png',
        'fanart': 'channels/et/dws_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 21
    },
    'adis': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'Addis TV',
        'thumb': 'channels/et/adis.png',
        'fanart': 'channels/et/adis_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'Addis TV',
        'thumb': 'channels/et/adis.png',
        'fanart': 'channels/et/adis_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 22
    },
    'estv': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'ES TV',
        'thumb': 'channels/et/estv.png',
        'fanart': 'channels/et/estv_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'ES TV',
        'thumb': 'channels/et/estv.png',
        'fanart': 'channels/et/estv_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 23
    },
    'south': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'Southern TV',
        'thumb': 'channels/et/south.png',
        'fanart': 'channels/et/south_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'Southern TV',
        'thumb': 'channels/et/south.png',
        'fanart': 'channels/et/south_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 24
    },
    'eritr': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'Eritrea TV',
        'thumb': 'channels/et/eritr.png',
        'fanart': 'channels/et/eritr_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'Eritrea TV',
        'thumb': 'channels/et/eritr.png',
        'fanart': 'channels/et/eritr_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 25
    },
    'afri': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'Afrihealth',
        'thumb': 'channels/et/afri.png',
        'fanart': 'channels/et/afri_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'Afrihealth',
        'thumb': 'channels/et/afri.png',
        'fanart': 'channels/et/afri_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 26
    },
    'asham': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'Asham TV',
        'thumb': 'channels/et/asham.png',
        'fanart': 'channels/et/asham_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'Asham TV',
        'thumb': 'channels/et/asham.png',
        'fanart': 'channels/et/asham_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 27
    },
    'ahadu': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'Ahadu TV',
        'thumb': 'channels/et/ahadu.png',
        'fanart': 'channels/et/ahadu_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'Ahadu TV',
        'thumb': 'channels/et/ahadu.png',
        'fanart': 'channels/et/ahadu_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 28
    },
    'balage': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'Balageru',
        'thumb': 'channels/et/balage.png',
        'fanart': 'channels/et/balage_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'Balageru',
        'thumb': 'channels/et/balage.png',
        'fanart': 'channels/et/balage_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 29
    },
    'ava': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'AVA TV',
        'thumb': 'channels/et/ava.png',
        'fanart': 'channels/et/ava_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'AVA TV',
        'thumb': 'channels/et/ava.png',
        'fanart': 'channels/et/ava_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 30
    },
    'asrat': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'ASRAT MEDIA',
        'thumb': 'channels/et/asrat.png',
        'fanart': 'channels/et/asrat_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'ASRAT MEDIA',
        'thumb': 'channels/et/asrat.png',
        'fanart': 'channels/et/asrat_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 31
    },
    'holys': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'Holy Spirit TV',
        'thumb': 'channels/et/holys.png',
        'fanart': 'channels/et/holys_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'Holy Spirit TV',
        'thumb': 'channels/et/holys.png',
        'fanart': 'channels/et/holys_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 32
    },
    'gloryg': {
<<<<<<< HEAD
        'callback': 'live_bridge',
        'label': 'Glory of GOD TV',
        'thumb': 'channels/et/gloryg.png',
        'fanart': 'channels/et/gloryg_fanart.jpg',
        'module': 'resources.lib.channels.et.video2b',
=======
        'resolver': '/resources/lib/channels/et/video2b:get_live_url',
        'label': 'Glory of GOD TV',
        'thumb': 'channels/et/gloryg.png',
        'fanart': 'channels/et/gloryg_fanart.jpg',
>>>>>>> cf69920d1ba10a4558544c5d79d7c35f56d3e2c3
        'enabled': True,
        'order': 33
    }
}
