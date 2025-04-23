# test.py

import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
from domain_info import get_domain_details

@patch('domain_info.whois.whois')
def test_get_domain_details(mock_whois):
    # Mock the whois response
    mock_data = MagicMock()
    mock_data.creation_date = datetime(2020, 1, 1)
    mock_data.expiration_date = datetime(2025, 1, 1)
    mock_data.__iter__.return_value = iter({'domain_name': 'example.com'}.items())
    mock_whois.return_value = mock_data

    result = get_domain_details("example.com")
    
    assert result['age'].days == 1827  # 5 years including a leap year (2020 and 2024)
    assert 'domain_name' in result['details']
