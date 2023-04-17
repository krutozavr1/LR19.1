#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import jsonschema
import click
from pedantic import BaseModel, ValidationError, validator
from marshmallow import (
    Schema, validates_schema,
    validates, fields, ValidationError
)


"""
Написать программу, которая считывает текст из файла и выводит на экран сначала
вопросительные, а затем восклицательные предложения.
"""

def compress_to_json(content):
    with open(save_file_name, "w", encoding="utf-8") as fout:
        json.dump(content, fout, ensure_ascii=False, indent=4)

def valid_check(file_to_check):
    with open(save_file_name, "r", encoding="utf-8") as fin:
        schema = json.load(fin)
    with open(file_to_check, "r", encoding="utf-8") as fin:
        jsonschema.validate(json.load(fin), schema = schema)
        validates_schema(json.load(fin))
        empty_check(json.load(fin))

@validates_schema
def validate_scheme(data):
    """marshmellow way"""
    if len(data) == 0:
        raise ValidationError('Not enough sentences')

@validator
def empty_check(content):
    """pydantic way"""
    if len(content) == 0:
        raise ValueError('No sentences found')

if __name__ == "__main__":
    save_file_name = input()
    file_to_check = input()

    divided_sentences = {}
    exclamation_sentences = []
    question_sentences = []

    with open("test_for_Idz1.txt", "r", encoding="utf-8") as f:
        sentences = f.readlines()

    for i in sentences:
        if i.find("!") != -1:
            exclamation_sentences.append(i)
        if i.find("?") != -1:
            question_sentences.append(i)

    divided_sentences["exclamation_sentences"] = exclamation_sentences
    divided_sentences["question_sentences"] = question_sentences

    compress_to_json(divided_sentences)
    valid_check(file_to_check)

