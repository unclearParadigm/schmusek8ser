class BaseSink(object):
    def post(self, title: str, message: str) -> None:
        raise NotImplementedError()
