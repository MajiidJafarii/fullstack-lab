from drf_spectacular.extensions import OpenApiAuthenticationExtension



class CookieJWTAuthenticationScheme(
    OpenApiAuthenticationExtension
):

    target_class = (
        "apps.accounts.authentication.CookieJWTAuthentication"
    )

    name = "cookieJWT"


    def get_security_definition(self, auto_schema):

        return {

            "type": "apiKey",

            "in": "cookie",

            "name": "access",

        }
