from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.account import Account
from ..serializers import AccountSerializer

# Create your views here.
class AccountsView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = AccountSerializer
    def get(self, request):
        """Index request"""
        # Get all the accounts:
        # accounts = Account.objects.all()
        # Filter the accounts by owner, so you can only see your owned accounts
        accounts = Account.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = AccountSerializer(accounts, many=True).data
        return Response({ 'accounts': data })

    def post(self, request):
        """Create request"""
        print('request ', request.data)
        # Add user to request data object
        request.data['account']['owner'] = request.user.id
        # Serialize/create account
        account = AccountSerializer(data=request.data['account'])
        # If the account data is valid according to our serializer...
        if account.is_valid():
            # Save the created account & send a response
            account.save()
            return Response({ 'account': account.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(account.errors, status=status.HTTP_400_BAD_REQUEST)

class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the account to show
        account = get_object_or_404(Account, pk=pk)
        # Only want to show owned accounts?
        if request.user != account.owner:
            raise PermissionDenied('Unauthorized, you do not own this account')

        # Run the data through the serializer so it's formatted
        data = AccountSerializer(account).data
        return Response({ 'account': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate account to delete
        account = get_object_or_404(Account, pk=pk)
        # Check the account's owner against the user making this request
        if request.user != account.owner:
            raise PermissionDenied('Unauthorized, you do not own this account')
        # Only delete if the user owns the  account
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Account
        # get_object_or_404 returns a object representation of our Account
        account = get_object_or_404(Account, pk=pk)
        # Check the account's owner against the user making this request
        if request.user != account.owner:
            raise PermissionDenied('Unauthorized, you do not own this account')

        # Ensure the owner field is set to the current user's ID
        request.data['account']['owner'] = request.user.id
        # Validate updates with serializer
        data = AccountSerializer(account, data=request.data['account'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
