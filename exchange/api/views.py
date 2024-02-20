from api.models import Currency
from api.serializers import CurrencySerializer
from django.shortcuts import get_list_or_404
from rest_framework import viewsets


class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CurrencySerializer

    def get_queryset(self):
        charcode = self.request.query_params.get("charcode")
        date = self.request.query_params.get("date")
        queryset = get_list_or_404(Currency, charcode=charcode, date=date)
        # queryset = Currency.objects.filter(charcode=charcode, date=date)
        return queryset

    # def list(self, request):
    #     charcode = request.query_params.get("charcode", None)
    #     date = request.query_params.get("date", None)
    #     if charcode and date:
    #         queryset = Currency.objects.filter(charcode=charcode, date=date)
    #         serializer = CurrencySerializer(queryset, many=True)
    #         if queryset:
    #         return Response(serializer.data)
    #     return Response(
    #         status=400,
    #         data={"message": "Provide both charcode and date parameters."},
    #     )
