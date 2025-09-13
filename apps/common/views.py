from rest_framework.viewsets import ModelViewSet


class BaseViewSet(ModelViewSet):
    http_method_names = (
        "get",
        "post",
        "patch",
        "delete",
        "head",
        "options",
    )
