from django.urls import path, include
from . import views
urlpatterns = [

    # Existing HTML endpoints
    path('', views.employee_form, name="employee_insert"),  #get and post req. for insert operation    localhost
    path('<int:id>/', views.employee_form, name="employee_update"),  #get and post req. for update operations
    path('delete/<int:id>/',views.employee_delete, name="employee_delete"),    #delete operation. delete req. to delete a record by id.
    path('list/', views.employee_list, name="employee_list"),  #route for employee list. get req. to retrieve and display all records.
]
