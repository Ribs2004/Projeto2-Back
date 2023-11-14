from django.contrib import admin
from django.urls import path, include
from results.views import search_results

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('results.urls')),  # Include your app's urls
    # path('search-results/', SearchResultView.as_view(), name='search_results'),
    path('search-results/', search_results, name='search-results')
]
