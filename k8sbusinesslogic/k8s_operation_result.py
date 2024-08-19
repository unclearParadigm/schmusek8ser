class K8sOperationResult(object):
    def __init__(self, operation: str, success: bool, error: str | None=None) -> None:
        self.operation = str(operation)
        self.success = bool(success)
        self.error = str(error) if error is not None else None