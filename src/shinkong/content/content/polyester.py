# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.autoform import directives
from plone.dexterity.content import Item
from plone.namedfile import field as namedfile
from plone.supermodel import model
from plone.supermodel.directives import fieldset
from z3c.form.browser.radio import RadioFieldWidget
from zope import schema
from zope.interface import implementer
from shinkong.content import _


class IPolyester(model.Schema):
    """ Marker interface and Dexterity Python Schema for Polyester
    """
    cover = namedfile.NamedBlobImage(
        title=_(u'Cover'),
        required=True,
    )
    dm = namedfile.NamedBlobImage(
        title=_(u'Dm'),
        required=True,
    )


@implementer(IPolyester)
class Polyester(Item):
    """
    """
