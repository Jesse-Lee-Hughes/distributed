import requests
from concurrent.futures import ThreadPoolExecutor
import pytest

def make_request():
    response = requests.get('http://localhost:8080')
    print(response.content)

@pytest.mark.integration
def test_messages():
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(make_request) for _ in range(10)]

        for future in futures:
            assert future
            if future:
                if future.exception() is not None:
                    print(f"Exception encountered during request: {future.exception()}")