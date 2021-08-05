from django.test import TestCase
import os

# These basic tests are to be used as an example for running tests in S2I
# and OpenShift when building an application image.
class PageViewModelTest(TestCase):
    def test_viewpage_model(self):
        self.assertEqual(1,1)