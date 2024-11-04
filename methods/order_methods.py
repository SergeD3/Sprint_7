import data
from methods.base_methods import BaseMethods


class OrderMethods(BaseMethods):

    def post_create_order_method(self, req_body):
        response = self.post_method(
            url=data.BASE_URL,
            req_path=data.PATH_ORDER_CREATE,
            req_json=req_body
        )
        return response
