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
from email.mime.text import MIMEText
import re



class DebugView(BrowserView):
    def __call__(self):
        request = self.request
        context = self.context
        portal = api.portal.get()
        import pdb; pdb.set_trace()


class SendMail(BrowserView):
    def __call__(self):
        body_str ="test test"
        mime_text = MIMEText(body_str, 'html', 'utf-8')
        api.portal.send_email(
            recipient="ah13441673@gmail.com",
            sender="henry@mingtak.com.tw",
            subject="test",
            body=mime_text.as_string(),
        )


class SearchPolyesterView(BrowserView):
    template = ViewPageTemplateFile('templates/search_polyester_view.pt')
    def __call__(self):
        return self.template()


class SearchPolyesterResult(BrowserView):
    template = ViewPageTemplateFile('templates/search_polyester_result.pt')
    def __call__(self):
        request = self.request
        subject = request.get('subject')
        query = {
            'portal_type': 'polyester',
            'review_state': 'published',
            'SearchableText': '%s*' %subject
        }
        self.result = api.content.find(**query)

        return self.template()


class SearchProductView(BrowserView):
    template = ViewPageTemplateFile('templates/search_product_view.pt')
    def __call__(self):
        portal = api.portal.get()

        productBrains = api.content.find(context=portal['products'], depth=1, portal_type='product')
        denierDict = {}
        for item in productBrains:
            obj = item.getObject()
            denier = obj.denier
            filament = obj.filament
            if denierDict.has_key(denier):
                denierDict[denier].append(filament)
            else:
                denierDict[denier] = [filament]

        self.denierDict = denierDict
        self.application = api.content.find(context=portal['application'], depth=1)
        return self.template()


class SearchProductResult(BrowserView):
    template = ViewPageTemplateFile('templates/search_product_result.pt')
    category = ViewPageTemplateFile('templates/search_category_result.pt')
    def __call__(self):
        request = self.request
        portal = api.portal.get()

        denier = request.get('denier')
        filament = request.get('filament')
        high_tenacity = request.get('high_tenacity')
        elongation = request.get('elongation')
        has2 = request.get('has2')

        data = {}
        uid = request.get('uid')
        if uid:
            self.result = api.content.get(UID=uid)
            return self.category()
        else:
            filament = float(filament)
            denier = float(denier)
            query = {
                'context': portal['products'],
                'portal_type': 'product', 
                'index_filament' : filament, 
                'index_denier' : denier
            }
            if high_tenacity:
                high_tenacity = float(high_tenacity)
                query['index_ht_min'] = {'query': high_tenacity, 'range': 'max'}
                query['index_ht_max'] = {'query': high_tenacity, 'range': 'min'}
            if has2:
                has2 = float(has2)
                query['index_h2_min'] = {'query': has2, 'range': 'max'}
                query['index_h2_max'] = {'query': has2, 'range': 'min'}
            if elongation:
                elongation = float(elongation)            
                query['index_el_min'] = {'query': elongation, 'range': 'max'}
                query['index_el_max'] = {'query': elongation, 'range': 'min'}
            filterProduct = api.content.find(**query)
            for item in filterProduct:
                obj = item.getObject()
                productUrl = obj.absolute_url()
                productName = obj.title
                data[productName] = productUrl
            self.data = data if data else False
            return self.template()
