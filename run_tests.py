#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, 'lib')

from lib.testing.book_test import TestBook
from lib.testing.shoe_test import TestShoe

def run_test(test_func, name):
    try:
        test_func()
        print(f"✓ {name}")
        return True
    except Exception as e:
        print(f"✗ {name}: {e}")
        return False

print("Running tests...")
book_test = TestBook()
shoe_test = TestShoe()

passed = 0
passed += run_test(book_test.test_has_title_and_page_count, "Book: has title and page count")
passed += run_test(book_test.test_requires_int_page_count, "Book: requires int page count")
passed += run_test(book_test.test_can_turn_page, "Book: can turn page")
passed += run_test(shoe_test.test_has_brand_and_size, "Shoe: has brand and size")
passed += run_test(shoe_test.test_requires_int_size, "Shoe: requires int size")
passed += run_test(shoe_test.test_can_cobble, "Shoe: can cobble")
passed += run_test(shoe_test.test_cobble_makes_new, "Shoe: cobble makes new")

print(f"\n{passed}/7 tests passed")