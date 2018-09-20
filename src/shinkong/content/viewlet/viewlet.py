# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import common as base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
from zope.component import queryUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer
from Products.CMFPlone.utils import getSiteLogo


class CoverIndustry(base.ViewletBase):
    def update(self):
        context = self.context
        self.industry = context.industry


class CoverPolyester(base.ViewletBase):
    def update(self):
        context = self.context
        self.polyester = context.polyester


class CoverYoutube(base.ViewletBase):
    def update(self):
        context = self.context
        self.youtubeList = context.getChildNodes()


class NewFooter(base.ViewletBase):
    def update(self):
        context = self.context
        self.logo = getSiteLogo()

class SKHeader(base.ViewletBase):
    """  """
