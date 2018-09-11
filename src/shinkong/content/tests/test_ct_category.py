# -*- coding: utf-8 -*-
from shinkong.content.content.category import ICategory  # NOQA E501
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


class CategoryIntegrationTest(unittest.TestCase):

    layer = SHINKONG_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_category_schema(self):
        fti = queryUtility(IDexterityFTI, name='category')
        schema = fti.lookupSchema()
        self.assertEqual(ICategory, schema)

    def test_ct_category_fti(self):
        fti = queryUtility(IDexterityFTI, name='category')
        self.assertTrue(fti)

    def test_ct_category_factory(self):
        fti = queryUtility(IDexterityFTI, name='category')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ICategory.providedBy(obj),
            u'ICategory not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_category_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='category',
            id='category',
        )

        self.assertTrue(
            ICategory.providedBy(obj),
            u'ICategory not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_category_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='category')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_category_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='category')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'category_id',
            title='category container',
         )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type='Document',
            title='My Content',
        )
        self.assertTrue(
            obj,
            u'Cannot add {0} to {1} container!'.format(obj.id, fti.id)
        )
