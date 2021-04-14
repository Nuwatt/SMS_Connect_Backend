from django.conf.urls import url
from WebPortal import views

from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from .views import UserSignupView,LoginView
urlpatterns=[

    # url(r'^questionnaires/$',views.questionnairesApi),
    # url(r'^questionnaires/([0-9]+)$',views.questionnairesApi),

    # url(r'^questionnaireType/$',views.questionnaireTypeApi),
    # url(r'^questionnaireType/([0-9]+)$',views.questionnaireTypeApi),

    # url(r'^questions/$',views.questionsApi),
    # url(r'^questions/([0-9]+)$',views.questionsApi),

    # url(r'^questionOptions/$',views.questionOptionsApi),
    # url(r'^questionOptions/([0-9]+)$',views.questionOptionsApi),

    # # url(r'^survey/$',views.surveyApi),
    # # url(r'^survey/([0-9]+)$',views.surveyApi),

    # url(r'^surveyActivity/$',views.surveyActivityApi),
    # url(r'^surveyActivity/([0-9]+)$',views.surveyActivityApi),

    # url(r'^answers/$',views.answerApi),
    # url(r'^answers/([0-9]+)$',views.answerApi),

    # url(r'^country/$',views.countryApi),
    # url(r'^country/([0-9]+)$',views.countryApi),

    # url(r'^city/$',views.cityApi),
    # url(r'^city/([0-9]+)$',views.cityApi),

    # url(r'^area/$',views.areaApi),
    # url(r'^area/([0-9]+)$',views.areaApi),

    # url(r'^retailer/$',views.retailerApi),
    # url(r'^retailer/([0-9]+)$',views.retailerApi),

    # url(r'^store/$',views.storeApi),
    # url(r'^store/([0-9]+)$',views.storeApi),

    # url(r'^category/$',views.categoryApi),
    # url(r'^category/([0-9]+)$',views.categoryApi),

    # url(r'^brand/$',views.brandApi),
    # url(r'^brand/([0-9]+)$',views.brandApi),

    # url(r'^sku/$',views.skuApi),
    # url(r'^sku/([0-9]+)$',views.skuApi),

    url(r'^role/$',views.rolesApi),
    url(r'^role/([0-9]+)$',views.rolesApi),

    url(r'^signup', UserSignupView.as_view(), name='signup'),
    url(r'^login', LoginView.as_view(), name='login'),
  
]