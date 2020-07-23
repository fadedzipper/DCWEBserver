from rest_framework.permissions import BasePermission


class ModelPermission(BasePermission):

    massage = "权限验证失败，没有对应权限"

    def has_permission(self, request, view):

        user = request.user
        # print(user)
        if not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        if hasattr(view,'get_model_perms_conf'):

            perms = view.get_model_perms_conf()
        else:
            perms = ()

        # print(perms)
        # print(user.get_all_permissions())
        # print(user.has_perms(perms))

        return user.has_perms(perms)


class ObjectPermission(BasePermission):

    def has_object_permission(self, request, view, obj):

        return