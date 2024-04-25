class ApiCall:
    GET = "GET"
    POST = "POST"

    def __init__(self):
        self._endpoint = None
        self._baseurl = None
        self._method = None
        self._request_params = None
        self._request_body = None
        self._request_headers = None
        self._response_status = None
        self._response_headers = None
        self._response_body = None

    @property
    def endpoint(self):
        return self._endpoint

    @endpoint.setter
    def endpoint(self, value):
        self._endpoint = value

    @property
    def baseurl(self):
        return self._baseurl

    @baseurl.setter
    def baseurl(self, value):
        self._baseurl = value

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value):
        self._method = value

    @property
    def request_params(self):
        return self._request_params

    @request_params.setter
    def request_params(self, value):
        self._request_params = value

    @property
    def request_body(self):
        return self._request_body

    @request_body.setter
    def request_body(self, value):
        self._request_body = value

    @property
    def request_headers(self):
        return self._request_headers

    @request_headers.setter
    def request_headers(self, value):
        self._request_headers = value

    @property
    def response_status(self):
        return self._response_status

    @response_status.setter
    def response_status(self, value):
        self._response_status = value

    @property
    def response_headers(self):
        return self._response_headers

    @response_headers.setter
    def response_headers(self, value):
        self._response_headers = value

    @property
    def response_body(self):
        return self._response_body

    @response_body.setter
    def response_body(self, value):
        self._response_body = value

    def __str__(self):
        return (
            f"Endpoint: {self.endpoint}, "
            f"Base URL: {self.baseurl}, "
            f"Method: {self.method}, "
            f"Request Params: {self.request_params}, "
            f"Request Body: {self.request_body}, "
            f"Request Headers: {self.request_headers}, "
            f"Response Status: {self.response_status}, "
            f"Response Headers: {self.response_headers}, "
            f"Response Body: {self.response_body}"
        )
