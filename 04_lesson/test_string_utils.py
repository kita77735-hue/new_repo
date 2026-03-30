import pytest
from string_utils import StringUtils

utils = StringUtils()

class TestStringUtils:
    
    def test_capitalize_normal(self):
        assert utils.capitalize("skypro") == "Skypro"

    def test_capitalize_empty(self):
        assert utils.capitalize("") == ""

    def test_capitalize_preserve_case(self):
        assert utils.capitalize("skyPro") == "SkyPro"

    def test_trim_leading_spaces(self):
        assert utils.trim("   skypro") == "skypro"

    def test_trim_no_spaces(self):
        assert utils.trim("skypro") == "skypro"

    def test_trim_trailing_spaces(self):
        assert utils.trim("skypro   ") == "skypro   "

    def test_trim_empty(self):
        assert utils.trim("") == ""

    def test_contains_found(self):
        assert utils.contains("SkyPro", "S") is True

    def test_contains_not_found(self):
        assert utils.contains("SkyPro", "U") is False

    def test_contains_substring(self):
        assert utils.contains("SkyPro", "Pro") is True

    def test_contains_empty_symbol(self):
        assert utils.contains("SkyPro", "") is True

    def test_contains_case_sensitive(self):
        assert utils.contains("SkyPro", "s") is False

    def test_delete_symbol_char(self):
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"

    def test_delete_symbol_substring(self):
        assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

    def test_delete_symbol_not_found(self):
        assert utils.delete_symbol("SkyPro", "Z") == "SkyPro"

    def test_delete_symbol_empty(self):
        assert utils.delete_symbol("", "k") == ""