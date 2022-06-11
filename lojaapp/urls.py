from django.urls import path
from .views import *



app_name ="lojaapp"
urlpatterns =[
path("", HomeView.as_view(), name="home"),
path("todos-produtos/", TodosProdutosView.as_view(), name="todosprodutos"),
path("produto/<slug:slug>/",ProdutoDetalhesView.as_view(), name="produtodetalhe"),
path("addcarro-/<int:pro_id>/",AddCarroView.as_view(), name="addcarro"),
path("meu-carro/",MeuCarroView.as_view(), name="meucarro"),
path("manipular-carro/<int:cp_id>",ManipularCarroView.as_view(), name="manipularcarro"),
path("limpar-carro/",LimparCarroView.as_view(), name="limparcarro"),
path("checkout/",CheckoutView.as_view(), name="checkout"),
path("registar/",ClienteRegistarView.as_view(), name="clienteregistar"),
path("sair/",ClienteSairView.as_view(), name="clientesair"),
path("entrar/",ClienteEntrarView.as_view(), name="clienteentrar"),
path("perfil/",ClientePerfilView.as_view(), name="clienteperfil"),
path("perfil/pedido-<int:pk>/",ClientePedidoDetalheView.as_view(), name="clientepedidodetalhe"),
path("admin-login/",AdminLoginView.as_view(), name="adminlogin"),
path("admin-home/",AdminHomeView.as_view(), name="adminhome"),
path("admin-pedido/<int:pk>/",AdminPedidoDetalheView.as_view(), name="adminpedidodetalhe"),
path("admin-todos-pedidos/",AdminPedidoListaView.as_view(), name="adminpedidolista"),
path("admin-pedido-<int:pk>-mudar/",AdminPedidoMudarStatusView.as_view(), name="adminpedidomudar"),
path("pesquisa/",PesquisaView.as_view(), name="pesquisar"),
path("pagamento/",PagamentotView.as_view(), name="pagamento"),

]