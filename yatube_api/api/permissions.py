from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)


class Owner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user)
