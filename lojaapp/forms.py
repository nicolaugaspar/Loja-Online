
from django import forms
from django.db.models.fields import CharField
from.models import Pedido_order, Cliente
from django.forms import ModelForm, TextInput, EmailInput
from django.contrib.auth.models import User


class Checar_PedidoForm(forms.ModelForm):
    required_css_class = 'required-field'

    ordenado_por = forms.CharField(widget=forms.TextInput(attrs={
                    "class":"border border-danger",      
                    'style':'max-with:1200px; ',
                     'placeholder': 'Ordenado por',
                     }))
    endereco_envio = forms.CharField(widget=forms.TextInput(attrs={
                    "class":" border border-danger",      
                    'style':'with:100px;',
                    'placeholder': 'Endereço Para Enviar',
                     }))  

    telefone = forms.CharField(widget=forms.TextInput(attrs={
                    "class":"border border-danger",      
                    'Style':'with:100px; text-right:300px',
                    'placeholder': 'Telefone',
                     }))  

    email = forms.CharField(widget=forms.EmailInput(attrs={
                    "class":"border border-danger",      
                    'Style':'with:100px;',
                    'placeholder': 'Email',
                     }))                                      
                     
    class Meta:
        model = Pedido_order
        fields = ["ordenado_por","endereco_envio","telefone","email","pagamento_method"]




class ClienteRegistarForm(forms.ModelForm):
   required_css_class = 'required-field'

   username = forms.CharField(widget=forms.TextInput(attrs={
                    "class":" form-control border border-danger w-75",      
                    'style':'with:1200px; display:flex;margin-left:100px',
                     'placeholder': 'Nome',
                     }))

                    
   password = forms.CharField(widget=forms.PasswordInput(attrs={
                    "class":"form-control border border-danger w-75",      
                    'style':'with:100px; display:flex; margin-left:100px',
                    'placeholder': 'Senha',
                     }))   

   email = forms.CharField(widget=forms.EmailInput(attrs={
                    "class":" form-control border border-danger w-75",      
                    'style':'with:100px;display:flex;margin-left:100px',
                    'placeholder': 'Email',
                     })) 
                     
   class Meta:
        model = Cliente
        fields = ["username","password","email","nome_completo","endereco"]


   def clean_username(self):
        unome = self.cleaned_data.get("username")
        if User.objects.filter(username = unome).exists():
            raise forms.ValidationError("Este cliente já existe no base de dados")
        return unome    


    
class ClienteEntrarForm(forms.Form):
  
   username = forms.CharField(widget=forms.TextInput(attrs={
                    "class":" form-control border border-danger w-75",      
                    'style':'with:1200px; display:flex;margin-left:100px',
                     'placeholder': 'Nome',
                     }))

                    
   password = forms.CharField(widget=forms.PasswordInput(attrs={
                    "class":"form-control border border-danger w-75",      
                    'style':'with:100px; display:flex; margin-left:100px',
                    'placeholder': 'Senha',
                     }))   
 