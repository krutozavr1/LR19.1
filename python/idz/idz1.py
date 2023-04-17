#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import click
from marshmallow import (
    Schema, validates_schema,
    validates, fields, ValidationError
)
from pedantic import BaseModel, ValidationError, validator

"""
Написать программу, которая считывает текст из файла и выводит на экран сначала
вопросительные, а затем восклицательные предложения.
"""

def compress_to_json(content):
    validate_scheme(content)
    empty_check(content)
    with open("data.json", "w", encoding="utf-8") as fout:
        json.dump(content, fout, ensure_ascii=False, indent=4)

def print_sentences_in_cmd(sentences):
    for s in sentences:
        click.echo(s)

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
    divided_sentences = sys.argv[1:]
    exclamation_sentences = []
    question_sentences = []

    for i in divided_sentences:
        if i.find("!") != -1:
            exclamation_sentences.append(i)
        if i.find("?") != -1:
            question_sentences.append(i)


    compress_to_json(exclamation_sentences)
    compress_to_json(question_sentences)

    print_sentences_in_cmd(exclamation_sentences)
    print_sentences_in_cmd(question_sentences)
