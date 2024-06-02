# Function Based
def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("On Request")

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        print("On Return")

        return response

    return middleware


# Class based, it is most commonly used almost every one
class ExampleMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.num_exceptions = 0
        self.context_responce = {
            "msg": {"warning": "There is no more ink in the printer"}
        }
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Logic executed before a call to view
        # Gives access to the view itself & arguments
        print(
            f"View Name: {view_func.__name__}"
        )  # print name of the url underlying view
        return None

    def process_exception(self, request, exception):
        # Logic executed if an exception/error occurs in the view
        self.num_exceptions += 1
        print(
            f"Expection count:{self.num_exceptions}"
        )  # print number of exceptions occured

    def process_template_response(self, request, response):
        # Logic executed after the view is called,
        # ONLY IF view response is TemplateResponse, see listing 2-24
        response.context_data["new_data"] = (
            self.context_responce
        )  # used to insert come data into template
        return response
