from rest_framework.permissions import BasePermission

class IsAdminOrOwner(BasePermission):
    """
    - Admin peut tout faire
    - Élève ne peut voir/éditer que ses propres données
    """

    def has_object_permission(self, request, view, obj):
        # Admin a tous les droits
        if request.user.role == "admin":
            return True

        # Vérifier si l’objet a un champ "user"
        if hasattr(obj, "user"):
            return obj.user == request.user

        # Vérifier si l’objet est lié à Student → student.user
        if hasattr(obj, "student") and obj.student.user == request.user:
            return True

        return False

    def has_permission(self, request, view):
        # Admin → accès complet
        if request.user.role == "admin":
            return True

        # Élève → interdit d’accéder à la liste générale
        if view.action == "list":
            return False

        return True