from turtle import title
import django_filters
from .models import blog
class postFilter(django_filters.FilterSet):
    title=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = blog
        fields = ['title','category']