# -*- coding: utf-8 -*-
from shinkong.content.content.cover import ICover  # NOQA E501
from shinkong.content.testing import SHINKONG_CONTENT_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName


class CoverIntegrationTest(unittest.TestCase):

    layer = SHINKONG_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_cover_schema(self):
        fti = queryUtility(IDexterityFTI, name='cover')
        schema = fti.lookupSchema()
        self.assertEqual(ICover, schema)

    def test_ct_cover_fti(self):
        fti = queryUtility(IDexterityFTI, name='cover')
        self.assertTrue(fti)

    def test_ct_cover_factory(self):
        fti = queryUtility(IDexterityFTI, name='cover')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ICover.providedBy(obj),
            u'ICover not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_cover_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='cover',
            id='cover',
        )

        self.assertTrue(
            ICover.providedBy(obj),
            u'ICover not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_cover_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='cover')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
