#!/usr/bin/env python3
"""Defines insert_school function"""


def insert_school(mongo_collection, **kwargs):
    """Inserts doc into collection based on kwargs"""
    return mongo_collection.insert_one(kwargs).inserted_id
