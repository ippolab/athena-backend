from rest_framework import HTTP_HEADER_ENCODING
from rest_framework_simplejwt.authentication import JWTAuthentication


class AthenaAuthenticationBackend(JWTAuthentication):
    def get_header(self, request):
        header = request.META.get("HTTP_AUTHORIZATION")
        if header is None:
            header = request.META.get("HTTP_X_ATHENA_AUTHORIZATION")

        if isinstance(header, str):
            # Work around django test client oddness
            header = header.encode(HTTP_HEADER_ENCODING)

        return header
