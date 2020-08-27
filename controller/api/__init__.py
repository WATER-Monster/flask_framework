# -*- coding: utf-8 -*-
from flask import Blueprint
api = Blueprint('api', __name__)

from controller.api.api_test_controller import *