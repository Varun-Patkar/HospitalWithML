from django.urls import path
from . import views

app_name="core"
urlpatterns = [
	path("",views.HomeView.as_view(),name="home"),
	# path("register-doctor/",views.RegisterDoctorView.as_view(),name="register-doctor"),
	# path("register-patient/",views.RegisterPatientView.as_view(),name="register-patient"),
	# path("login-doctor/",views.LoginDoctorView.as_view(),name="login-doctor"),
	# path("login-patient/",views.LoginPatientView.as_view(),name="login-patient"),
]