from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of a `Post` to edit it.
    Assumes the view is working with `Post` objects.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the request method is a safe method (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the object belongs to the current user (owner)
        # Adjust this based on how the user is associated with the Post model
        # If the user is stored on the request (like in request.user), you can modify this check accordingly.
        return (
            obj.user == request.user
        )  # Ensure the `Post` object has the `user` field
