class RoleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        # one-time configuration and initialization

    def __call__(self, request):
        """
        code to be executed for each request before the
        view is called
        """
        response = self.get_response(request)

        # code to be exicuted for each request / reponse after
        # view is called

        return response

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """
          called just before django  calls the view .
        return either none or Httpresponse
        """

    # request.role = None
    # group = request.user.group.all()
    # if groups:
    #      request.role = groups[0].name

    def process_exception(self, request, exception):
        """
        called for the response if exception is raised by view .
        :return either none or HttpResponse

        """

    def process_template_response(self, request, response):
        # request - HttpRequest object
        # response - templateResponse object
        #
        # return templateresponse
        # use this for changing template or context if it is needed.
        pass
