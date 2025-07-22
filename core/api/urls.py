from django.urls import path

from myapp.views import PredictImage

urlpatterns = [
    path('Predict_Image/', PredictImage.as_view())
]

