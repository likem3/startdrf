from rest_framework.permissions import BasePermission

class IsMerchant(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated or not request.user.merchant:
            return False

        return True