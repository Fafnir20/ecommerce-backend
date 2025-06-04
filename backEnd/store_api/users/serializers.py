from rest_framework import serializers
from .models import Usuario, Funcao, Permissao

class FuncaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcao
        fields = '__all__'

class PermissaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissao
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    # Cria um campo extra para confirmar a senha
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Usuario
        # Inclui todos os campos, mas oculta senha na saída
        fields = ['id', 'username', 'email', 'password', 'password2', 'funcao']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("As senhas nao coicidem")
        return data 
    

    def create(self, validated_data):
        validated_data.pop('password2') # remmove a a password2 pois nao e usada no models
        password = validated_data.pop('password')  # remove e guarda a senha
        user = Usuario(**validated_data)           # cria o objeto sem a senha ainda
        user.set_password(password)                # define a senha criptografada
        user.save()
        return user