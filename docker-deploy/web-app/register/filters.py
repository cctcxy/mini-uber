import django_filters
from django_filters import DateFilter, NumberFilter

from .models import *

class requestFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="arrival_time", lookup_expr='gte')
    end_date = DateFilter(field_name="arrival_time", lookup_expr='lte')
    sharer_num = NumberFilter(field_name="number_be_shared", lookup_expr="gte")
    class Meta:
        model = ride_request
        fields = ['destination']
