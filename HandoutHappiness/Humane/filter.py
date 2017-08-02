import django_filters
from Humane.models import *

class GoodsFilter(django_filters.FilterSet):
    class Meta:
        model = GoodsDetail
        fields = ('is_good_satisfied','goods_id',)
