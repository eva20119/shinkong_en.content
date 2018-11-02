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
from plone.namedfile.field import NamedBlobImage, NamedBlobFile, NamedImage


class IProduct(model.Schema):

    title = schema.TextLine(
        title=_(u'title'),
        required=True
    )
    high_tenacity = schema.Float(
        title=_(u'High Tenacity'),
        default=0.0,
        required=True
    )
    high_tenacity_difference = schema.Float(
        title=_(u'High Tenacity Difference'),
        default=0.0,
        required=True
    )
    elongation = schema.Float(
        title=_(u'Elongation'),
        default=0.0,
        required=True
    )
    elongation_difference = schema.Float(
        title=_(u'Elongation Difference'),
        default=0.0,
        required=True
    )
    has2 = schema.Float(
        title=_(u'H.A.S(2)'),
        default=0.0,
        required=True
    )
    has2_difference = schema.Float(
        title=_(u'H.A.S(2) Difference'),
        default=0.0,
        required=True
    )
    denier = schema.Int(
        title=_(u'denier'),
        required=True
    )
    filament = schema.Int(
        title=_(u'filament'),
        required=True
    )
    easl_remark = schema.TextLine(
        title=_(u'EASL Remark'),
        required=False
    )
    easl = schema.TextLine(
        title=_(u'EASL'),
        required=False
    )
    ptl = schema.TextLine(
        title=_(u'Paper Tube Length(mm)'),
        required=False
    )
    aayarn = schema.Bool(
        title=_(u'aayarn'),
        default=False,
        required=False
    )
    type_remark = schema.TextLine(
        title=_(u'Type Remark'),
        required=False
    )


@implementer(IProduct)
class Product(Item):
    """
    """
