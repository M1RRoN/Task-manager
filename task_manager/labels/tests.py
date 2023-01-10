import os
import json
from django.test import TestCase


class SetupTestLabels(TestCase):
    fixtures = ['labels.json']
