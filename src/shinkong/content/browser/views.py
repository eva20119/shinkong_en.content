# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.contenttypes.browser.folder import FolderView
from shinkong.content import _
from zope.interface import alsoProvides
from plone.protect.interfaces import IDisableCSRFProtection
from email.mime.text import MIMEText
import json
import datetime


class SearchProductView(BrowserView):
    template = ViewPageTemplateFile('templates/search_product_view.pt')
    def __call__(self):
        return self.template()


class SearchProductResult(BrowserView):
    template = ViewPageTemplateFile('templates/search_product_result.pt')
    def __call__(self):
        request = self.request
        portal = api.portal.get()

        select_type = request.get('select_type')
        high_tenacity = float(request.get('high_tenacity'))
        elongation = float(request.get('elongation'))
        has2 = float(request.get('has2'))
        productBrains = api.content.find(context=portal['products'], depth=1, portal_type='product')
        data = {}
        for product in productBrains:
            obj = product.getObject()

            ht = obj.high_tenacity
            htd = obj.high_tenacity_difference
            el = obj.elongation
            eld = obj.elongation_difference
            h2 = obj.has2
            h2d = obj.has2_difference
            if ht - htd <= high_tenacity and ht + htd >= high_tenacity and \
               el - eld <= elongation and el + eld >= elongation and \
               h2 - h2d <= has2 and h2 + h2d >= has2:
                productUrl = obj.absolute_url()
                productName = obj.title
                data[productName] = productUrl

        self.data = data if data else False

        return self.template()
