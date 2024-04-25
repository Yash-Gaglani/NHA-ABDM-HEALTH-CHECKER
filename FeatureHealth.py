from typing import List
from ApiCall import ApiCall


class FeatureHealth:

    FAILING = "FAILING"
    PASSING = "PASSING"

    def __init__(self):
        self._feature = None
        self._status = None
        self._api_calls = []

    @property
    def feature(self):
        return self._feature

    @feature.setter
    def feature(self, value):
        self._feature = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def api_calls(self):
        return self._api_calls

    @api_calls.setter
    def api_calls(self, value: List[ApiCall]):
        self._api_calls = value

    def add_api_call(self, api_call: ApiCall):
        if not isinstance(api_call, ApiCall):
            raise TypeError("Item must be a ApiCall")
        if self._api_calls is None:
            self._api_calls = []
        self._api_calls.append(api_call)

    def __str__(self):
        api_calls_str = "\n ".join(str(obj) for obj in self._api_calls)
        return f"Feature: {self.feature}, Status: {self.status}, \nAPI Calls:\n {api_calls_str}"

