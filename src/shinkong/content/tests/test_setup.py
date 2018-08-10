# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from shinkong.content.testing import SHINKONG_CONTENT_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that shinkong.content is properly installed."""

    layer = SHINKONG_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if shinkong.content is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'shinkong.content'))

    def test_browserlayer(self):
        """Test that IShinkongContentLayer is registered."""
        from shinkong.content.interfaces import (
            IShinkongContentLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IShinkongContentLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = SHINKONG_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['shinkong.content'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if shinkong.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'shinkong.content'))

    def test_browserlayer_removed(self):
        """Test that IShinkongContentLayer is removed."""
        from shinkong.content.interfaces import \
            IShinkongContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IShinkongContentLayer,
            utils.registered_layers())
