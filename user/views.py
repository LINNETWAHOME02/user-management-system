from django.contrib.auth import update_session_auth_hash, authenticate
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from user.forms import UserForm
from user.serializer import *

######################### USER REGISTRATION, LOG IN & LOG IN ##############################
@api_view(['POST'])
def create_user(request):
    try:
        '''New user object from the request data'''
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            #  get the user object
            user = AppUser.objects.get(username=request.data['username'], email = request.data['email'])

            # hash the password
            user.set_password(request.data['password'])

            # update the user object with the hashed password
            user.save()

            # create a token for the user
            token = Token.objects.create(user=user)

            # return the token and user data
            return Response({'token': token.key, 'user': serializer.data}, status=201)
        else:
            return Response(serializer.errors, status=400)
    except Exception as e:
        return Response({'error': str(e)}, status=400)

# Log in
#@csrf_exempt  # To disable CSRF check for this API view
@api_view(['POST'])
def login(request):
    user = get_object_or_404(AppUser, username=request.data.get('username'))

    if not (user.check_password(request.data['password']) or user.password == request.data['password']):
            return Response({'message': 'Invalid credentials'}, status=400)


    token, _ = Token.objects.get_or_create(user=user)

    serializer = UserSerializer(instance=user)
    return Response({'token': token.key, 'user': serializer.data}, status=200)

# Log out
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def logout(request):
    user = request.user

    # Normal functioning
    try:
        # Delete the user's token to log them out
        request.user.auth_token.delete()
        return Response({'message': 'Logged out successfully'}, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=400)

    # # For testing on postman
    # try:
    #     user.auth_token.delete()
    #     return Response({'message': f'User {user.username} logged out successfully'}, status=200)
    # except Exception as e:
    #     return Response({'error': str(e)}, status=400)

########################################## UPDATING USER DETAILS ##########################################
# Update user details
@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def update_details(request, id):
    try:
        user = AppUser.objects.get(pk=id)

        # To prevent users from editing other accounts
        if request.user.id != user.id:
            return Response({'error': 'You can only update your own account.'}, status=403)

        # True if method is PATCH (partial update)
        partial = request.method == 'PATCH'

        serializer = UserSerializer(user, data=request.data, partial=partial)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User updated successfully', 'user': serializer.data})
        else:
            return Response(serializer.errors, status=400)

    except AppUser.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=404)

###################################### DELETE USER #########################################
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def delete_user(request):
    try:
        user = request.user
        user.delete()
        return Response({'message': f'User {user.username} deleted successfully'}, status=204)

    except AppUser.DoesNotExist:
        return Response({'error': 'User does not exist'}, status=400)

########################### DISPLAY ALL USERS ##############################
@api_view(['GET'])
def display_users(request):
    users = AppUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

############################### CHANGE PASSWORD ####################################
@api_view(['POST']) # POST to handle sensitive data since GET send data via the URL, which can be logged in
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def change_password(request):
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')
    confirm_password = request.data.get('confirm_password')

    user = request.user
    print(user)

    # Step 1: Authenticate with old password
    if not user.check_password(old_password):
        return Response({'error': 'Old password is incorrect'}, status=400)

    # Step 2: Validate new password confirmation
    if new_password != confirm_password:
        return Response({'error': 'New password and confirmation do not match'}, status=400)

    # Step 3: Set new password and save
    user.set_password(new_password)
    user.save()

    return Response({'message': 'Password changed successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_auth(request):
    return Response({'message': f'You are authenticated as {request.user.username}'})

