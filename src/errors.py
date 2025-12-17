
""""


class BooklyException(Exception):
    """This is the base class for all bookly errors"""

    pass

class InvalidToken(BooklyException):
    """"User has provided an invalid or expired token""""
    pass
class RevokedToken(BooklyException):
    """User has provided a token that has been revoked"""
    pass

class AccessTokenRequired(BooklyException)"""