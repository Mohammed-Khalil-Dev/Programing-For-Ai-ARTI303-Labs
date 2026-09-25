"""Tests for src/text_utils.py"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import src.text_utils as text_utils


def test_clean_name_whitespace():
    assert text_utils.clean_name("   Happy   Me  ") == "Happy Me"


def test_clean_name_capitalisation():
    assert text_utils.clean_name("haPpy mE") == "Happy Me"
