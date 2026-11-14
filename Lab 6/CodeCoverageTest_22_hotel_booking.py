
import pytest
from hotel_booking import booking_cost, cancellation_refund, room_upgrade


# BOOKING COST TESTS

def test_standard_two_nights():
    assert booking_cost("standard", 2, 2, False) == 4000


def test_unknown_room():
    with pytest.raises(ValueError):
        booking_cost("premium", 2, 2, False)


def test_invalid_nights():
    with pytest.raises(ValueError):
        booking_cost("standard", 0, 2, False)


def test_peak_season():
    assert booking_cost("deluxe", 2, 2, True) == 8750


def test_extra_guests():
    assert booking_cost("standard", 2, 4, False) == 6000


def test_weekly_discount():
    assert booking_cost("suite", 7, 2, False) == 37800


# CANCELLATION REFUND TESTS

def test_full_refund():
    assert cancellation_refund(1000, 10, False) == 1000


def test_partial_refund_with_membership():
    assert cancellation_refund(1000, 5, True) == 750


def test_no_refund():
    assert cancellation_refund(1000, 1, False) == 0


# ROOM UPGRADE TESTS

def test_no_rooms_available():
    assert room_upgrade("standard", True, 0) == "standard"


def test_standard_member_upgrade():
    assert room_upgrade("standard", True, 1) == "deluxe"


def test_deluxe_member_upgrade():
    assert room_upgrade("deluxe", True, 1) == "suite"


def test_no_upgrade_for_non_member():
    assert room_upgrade("standard", False, 1) == "standard"
