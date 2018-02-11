# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class Roles(ApiHandler):

    def get(self):
        print(self.args)

        return [], 200, None

    def post(self):
        print(self.json)

        return {'created_at': 'something', 'label': {}, 'requires_2fa': False, 'id': 9573, 'updated_at': 'something'}, 201, None