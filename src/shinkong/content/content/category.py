# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from shinkong.content import _
from plone.namedfile.field import NamedBlobImage


class ICategory(model.Schema):
    image1 = NamedBlobImage(
        title=_(u"Product Image1"),
        required=False,
    )

    image2 = NamedBlobImage(
        title=_(u"Product Image2"),
        required=False,
    )
    image3 = NamedBlobImage(
        title=_(u"Product Image3"),
        required=False,
    )




@implementer(ICategory)
class Category(Container):
    """
    """
