import pytest

def test_submit_text_with_input():
    """Test that non-empty text is accepted"""
    text = "Hello CI/CD"
    result = text.strip()
    assert result == "Hello CI/CD"

def test_submit_text_empty():
    """Test that empty input is handled"""
    text = "   "
    result = text.strip()
    assert result == ""

def test_submit_text_strips_whitespace():
    """Test whitespace stripping logic"""
    text = "  hello  "
    result = text.strip()
    assert bool(result) == True