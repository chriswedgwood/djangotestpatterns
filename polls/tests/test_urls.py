import pytest
from django.urls import resolve, reverse


def test_index():
    assert reverse("polls:index") == f"/"


def test_detail():
    assert reverse("polls:detail", args=[1]) == f"/1/"
