import sys
sys.path.append("..") # allow importing from parent dir
from unittest.mock import MagicMock
from src import business

def test_answer():
    business.client.secure = MagicMock()
    business.client.secure.return_value = "secured"
    result = business.submit("testing data")
    assert result == "secured"
    assert business.client.secure.called