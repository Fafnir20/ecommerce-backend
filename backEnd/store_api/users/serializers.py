from rest_framework import serializers
from .models import Usuario, Funcao, Permissao, Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'


class FuncaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcao
        fields = '__all__'

class PermissaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissao
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    # Campo extra para confirmar a senha
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Usuario
        fields = [
            'id', 'username', 'email', 'password', 'password2', 'funcao',
            # 'endereco_rua', 'endereco_numero', 'endereco_complemento',
            # 'endereco_bairro', 'endereco_cidade', 'endereco_estado',
            # 'endereco_cep', 'endereco_pais',
        ]
        # extra_kwargs = {
        #     'password': {'write_only': True},
        #     'endereco_rua': {'required': False, 'allow_null': True, 'allow_blank': True},
        #     'endereco_numero': {'required': False, 'allow_null': True, 'allow_blank': True},
        #     'endereco_complemento': {'required': False, 'allow_null': True, 'allow_blank': True},
        #     'endereco_bairro': {'required': False, 'allow_null': True, 'allow_blank': True},
        #     'endereco_cidade': {'required': False, 'allow_null': True, 'allow_blank': True},
        #     'endereco_estado': {'required': False, 'allow_null': True, 'allow_blank': True},
        #     'endereco_cep': {'required': False, 'allow_null': True, 'allow_blank': True},
        #     'endereco_pais': {'required': False, 'allow_null': True, 'allow_blank': True},
        # }

    def validate(self, data):
        if data.get('password') != data.get('password2'):
            raise serializers.ValidationError("As senhas nao coincidem")
        return data

    def create(self, validated_data):
        # Remove password2 pois não existe no modelo
        validated_data.pop('password2', None)
        password = validated_data.pop('password', None)
        user = Usuario(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        # Validação de senha
        password = validated_data.pop('password', None)
        validated_data.pop('password2', None)
        # Atualiza campos simples e endereço
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
