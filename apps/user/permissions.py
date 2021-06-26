from rest_framework.permissions import BasePermission


class IsAgentUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_agent_user)

    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj)


class IsPortalUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated and request.user.is_portal_user)

    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj)


class IsAdminPortalUser(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and
            request.user.is_portal_user and
            request.user.portaluser.role.name == 'Admin'
        )


class IsResearcherPortalUser(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and
            request.user.is_portal_user and
            request.user.portaluser.role.name == 'Researcher'
        )
