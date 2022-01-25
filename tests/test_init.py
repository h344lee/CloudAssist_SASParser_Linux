from readlogs.read_logs import get_user_log_content
from pytest import mark

@mark.base
def test_initial():
    answer = get_user_log_content("hello", "good")
    assert answer == "good"

