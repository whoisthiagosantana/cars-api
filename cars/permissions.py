from rest_framework import permissions

# Regra de negócio que permite que o usuário que criou o carro possa visualizá-lo
class CarOwnerPermission(permissions.BasePermission):

    # se o get for uma listagem ele retorna todos os objetos que o usuário criou
    def has_permission(self, request, view):
        if view.action == 'list':
            view.queryset = view.queryset.filter(user=request.user)
            return True
        return super().has_permission(request, view)
    
    # se for fazer alguma interação a algum objeto, como editar e apagar, verifica se o usuaŕio é o dono do objeto
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user