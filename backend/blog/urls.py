from django.urls import path, include
from .views import ArticleList, ArticleDetail , TransferList , TransferDetail

app_name = "blog"

urlpatterns = [
	path("article/", ArticleList.as_view(), name="list"),
	path("transfer/", TransferList.as_view(), name="list"),
	path("article/<int:pk>",ArticleDetail.as_view(), name="detail"),
	path("transfer/<int:pk>",TransferDetail.as_view(), name="transfer-detail"),
]