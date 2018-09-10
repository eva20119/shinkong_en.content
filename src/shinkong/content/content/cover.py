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
from z3c.relationfield.schema import RelationList, RelationChoice
from plone.app.vocabularies.catalog import CatalogSource


class ICover(model.Schema):
    title = schema.TextLine(
        title=_(u"Cover"),
        required=True
    )
    industry = RelationList(
        title=_(u"industry relation list"),
        required=False,
        value_type=RelationChoice(
            title=_(u"industry"),
            source=CatalogSource(Type='product'),
        )
    )





@implementer(ICover)
class Cover(Item):
    """
    """
