from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.fund import Fund
from ..serializers import FundSerializer

# Create your views here.
class FundsView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = FundSerializer
    def get(self, request):
        """Index request"""
        # Get all the funds:
        # funds = Fund.objects.all()
        # Filter the funds by owner, so you can only see your owned funds
        funds = Fund.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = FundSerializer(funds, many=True).data
        return Response({ 'funds': data })

    def post(self, request):
        """Create request"""
        print('request ', request.data)
        # Add user to request data object
        request.data['fund']['owner'] = request.user.id
        # Serialize/create fund
        fund = FundSerializer(data=request.data['fund'])
        # If the fund data is valid according to our serializer...
        if fund.is_valid():
            # Save the created fund & send a response
            fund.save()
            return Response({ 'fund': fund.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(fund.errors, status=status.HTTP_400_BAD_REQUEST)

class FundDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the fund to show
        fund = get_object_or_404(Fund, pk=pk)
        # Only want to show owned funds?
        if request.user != fund.owner:
            raise PermissionDenied('Unauthorized, you do not own this fund')

        # Run the data through the serializer so it's formatted
        data = FundSerializer(fund).data
        return Response({ 'fund': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate fund to delete
        fund = get_object_or_404(Fund, pk=pk)
        # Check the fund's owner against the user making this request
        if request.user != fund.owner:
            raise PermissionDenied('Unauthorized, you do not own this fund')
        # Only delete if the user owns the  fund
        fund.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Fund
        # get_object_or_404 returns a object representation of our Fund
        fund = get_object_or_404(Fund, pk=pk)
        # Check the fund's owner against the user making this request
        if request.user != fund.owner:
            raise PermissionDenied('Unauthorized, you do not own this fund')

        # Ensure the owner field is set to the current user's ID
        request.data['fund']['owner'] = request.user.id
        # Validate updates with serializer
        data = FundSerializer(fund, data=request.data['fund'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
