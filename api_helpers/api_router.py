import os
import requests
from dotenv import load_dotenv
from typing import Any
load_dotenv()

class ApiRequest:

    def __init__(self):
        self.base_url = os.getenv("API_BASE_URL")
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('API_TOKEN')}"
        })

    def _request(self, method, endpoint, **kwargs):
        full_url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.request(method, full_url, **kwargs)
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Error: {e}")
        response.raise_for_status()
        return ApiResponse(response)

    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)
    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)
    def put(self, endpoint, **kwargs):
        return self._request("PUT", endpoint, **kwargs)
    def patch(self, endpoint, **kwargs):
        return self._request("PATCH", endpoint, **kwargs)
    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)
    def query(self, endpoint, **kwargs):
        return self._request("QUERY", endpoint, **kwargs)


class ApiResponse:
    def __init__(self, response):
        self.raw_response = response
        self.status_code = response.status_code
        self.json_data: dict[str, Any] | list[Any] | None = None
        try:
            self.json_data = response.json()
        except ValueError:
            self.json_data = None