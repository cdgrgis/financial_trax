from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.fund_info import FundInfo
from ..serializers import FundInfoSerializer, FundInfoReadSerializer


class AccountFundInfosView(generics.ListCreateAPIView):
  def get(self, request, pk):
    fund_infos = FundInfo.objects.filter(account=pk)
    data=FundInfoReadSerializer(fund_infos, many=True).data
    return Response({ 'fund_infos': data })


class FundInfosView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = FundInfoSerializer
    def get(self, request):
        """Index request"""
        print('request ', request.data)
        fund_infos = FundInfo.objects
        # Run the data through the serializer
        data = FundInfoSerializer(fund_infos, many=True).data
        return Response({ 'fund_infos': data })

    def post(self, request):
        """Create request"""
        print('request ', request.data)
        # Add user to request data object
        request.data['fund_info']['owner'] = request.user.id
        # Serialize/create fund
        fund_info = FundInfoSerializer(data=request.data['fund_info'])
        # If the fund data is valid according to our serializer...
        if fund_info.is_valid():
            # Save the created fund & send a response
            fund_info.save()
            return Response({ 'fund_info': fund_info.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(fund_info.errors, status=status.HTTP_400_BAD_REQUEST)

class FundInfoDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the fund to show
        fund_info = get_object_or_404(FundInfo, pk=pk)
        # Only want to show owned funds?
        if request.user != fund_info.owner:
            raise PermissionDenied('Unauthorized, you do not own this fund')

        # Run the data through the serializer so it's formatted
        data = FundInfoSerializer(fund_info).data
        return Response({ 'fund_info': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate fund to delete
        fund_info = get_object_or_404(FundInfo, pk=pk)
        # Check the fund's owner against the user making this request
        if request.user != fund_info.owner:
            raise PermissionDenied('Unauthorized, you do not own this fund_info')
        # Only delete if the user owns the  fund
        fund_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Fund
        # get_object_or_404 returns a object representation of our Fund
        fund_info = get_object_or_404(FundInfo, pk=pk)
        # Check the fund's owner against the user making this request
        if request.user != fund_info.owner:
            raise PermissionDenied('Unauthorized, you do not own this fund_info')

        # Ensure the owner field is set to the current user's ID
        request.data['fund_info']['owner'] = request.user.id
        # Validate updates with serializer
        data = FundInfoSerializer(fund_info, data=request.data['fund_info'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
