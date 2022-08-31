"""medassist_ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import CategoryController
from . import SubcategoryController

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categoryinterface/', CategoryController.Category_Interface),
    path('subcategoryinterface/', SubcategoryController.Subcategory_Interface),
    path('submitcategory', CategoryController.Submit_Category),
    path('submitsubcategory', SubcategoryController.Submit_Subcategory),
    path('displayallcategories/', CategoryController.Display_All_Categories),
    path('displayallsubcategories/',SubcategoryController.Display_All_Subategories),
    path('editcategory/', CategoryController.Edit_Category),
    path('deletecategory/',CategoryController.Delete_Category),
    path('editsubcategory/', SubcategoryController.Edit_Subcategory),
    path('deletesubcategory/',SubcategoryController.Delete_Subcategory),
    path('editcategoryicon', CategoryController.Edit_CategoryIcon),
]