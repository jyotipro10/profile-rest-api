from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """User to edit their own profiles only"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to make changes to others profiles"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
