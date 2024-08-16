class ApiResponse(object):
    def __init__(self, status_code: int, success: bool, payload: None | dict = None, error: None | str = None) -> None:
        self.status_code = int(status_code)
        self.success = bool(success)
        self.payload = payload
        self.error = error

    def to_dict(self) -> dict:
        return {
            'status': self.status_code,
            'success': self.success,
            'error': self.error,
            'payload': self.payload.__dict__
        }
