import data

from methods.base_methods import BaseMethods


class CourierMethods(BaseMethods):

    def post_create_courier_method(self, credentials):
        response = self.post_method(
            url=data.BASE_URL,
            req_path=data.PATH_COURIER_CREATE,
            req_body=credentials
        )
        return response

    def post_login_courier_method(self, credentials):
        response = self.post_method(
            url=data.BASE_URL,
            req_path=data.PATH_COURIER_LOGIN,
            req_body=credentials
        )
        return response
