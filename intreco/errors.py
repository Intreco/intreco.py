class IntrecoAPIException(Exception):
    pass

class HTTPException(IntrecoAPIException):
    pass

class NotAuthorized(HTTPException):
    pass