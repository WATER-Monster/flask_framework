# -*- coding: utf-8 -*-
from flask import Blueprint
api = Blueprint('api', __name__)

from controller.api.post_test_controller import *
from controller.api.heart_beat_check import *