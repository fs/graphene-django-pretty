from graphql.error.graphql_error import GraphQLError

from graphene_django_pretty.error.types import StatusCode, validate_status_code


class BaseGraphQLError(GraphQLError):
    """Base extended GraphQLError with status code."""

    default_message: str = None
    default_code: StatusCode = None

    def __init__(
        self,
        code: StatusCode = None,
        message: str = None,
        *args,
        **kwargs,
    ):
        """Init overriding for status code and message."""
        if not message:
            message = self.default_message

        self.code = code or self.default_code
        validate_status_code(self.code)

        if self.code:
            extensions = kwargs.get('extentions', {})
            extensions.update({'code': self.code})
            kwargs['extensions'] = extensions

        super().__init__(message=message, *args, **kwargs)
