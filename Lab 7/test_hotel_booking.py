
from hypothesis import given, strategies as st
from hotel_booking import nights_stayed, room_floor, booking_label


# Test nights_stayed with random strings and None
@given(st.text() | st.none())
def test_nights_stayed_no_crash(s):
    nights_stayed(s)


# Test room_floor with random strings and None
@given(st.text() | st.none())
def test_room_floor_no_crash(s):
    room_floor(s)


# Test booking_label with random strings and None
@given(st.text() | st.none())
def test_booking_label_no_crash(s):
    booking_label(s)
