#!/usr/bin/python
# -*- coding: utf-8 -*-

from plone.indexer.decorator import indexer
from shinkong.content.content.product import IProduct

@indexer(IProduct)
def index_denier(obj):
    return obj.denier

@indexer(IProduct)
def index_filament(obj):
    return obj.filament

@indexer(IProduct)
def index_ht_max(obj):
    return obj.high_tenacity + obj.high_tenacity_difference

@indexer(IProduct)
def index_ht_min(obj):
    return obj.high_tenacity - obj.high_tenacity_difference

@indexer(IProduct)
def index_el_max(obj):
    return obj.elongation + obj.elongation_difference

@indexer(IProduct)
def index_el_min(obj):
    return obj.elongation - obj.elongation_difference

@indexer(IProduct)
def index_h2_max(obj):
    return obj.has2 + obj.has2_difference

@indexer(IProduct)
def index_h2_min(obj):
    return obj.has2 - obj.has2_difference




