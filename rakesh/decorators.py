from django.http import HttpResponse


def allowed_users(allowed_user=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            rk = None
            if request.user.username == 'rakesh124':
                rk = request.user.username
            if rk in allowed_user:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('you are not authorized to view this page')

        return wrapper_func

    return decorator
