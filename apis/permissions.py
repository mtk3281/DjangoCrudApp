from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    #! Authenticated users only can see list view
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False
    
    #! # Read permissions are allowed to any request so we'll always
    #! allow GET, HEAD, or OPTIONS requests
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user