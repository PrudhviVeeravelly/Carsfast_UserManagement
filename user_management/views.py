from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.views.generic import ProtectedResourceView
from user_management.models import UserData
from django.contrib.auth.decorators import login_required


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        print(f"debug:POST_DATA: {request.POST}")
        username = request.POST.get('username')
        password = request.POST.get('password')
        print (f"debug = username = {username}, password = {password}")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Logged in successfully'})
        else:
            return JsonResponse({'message': 'Login failed'})
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)  # Return appropriate HTTP status


class ProtectedAPI(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'This is a protected resource accessible only with a valid OAuth2 token.'})


@csrf_exempt
#@login_required
def download_user_data(request):
    if request.method == 'GET':
        user = request.user  # Assuming you have implemented proper authentication
        try:
            user_data = UserData.objects.get(user=user)
            # You can customize the data format and content for download
            data = {
                'username': user_data.user.username,
                #'pii_data': user_data.pii_data,
                # Include other relevant data fields
            }
            return JsonResponse(data)
        except UserData.DoesNotExist:
            return JsonResponse({'error': 'User data not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def delete_user_data(request):
    if request.method == 'POST':
        user = request.user  # Assuming you have implemented proper authentication
        try:
            user_data = UserData.objects.get(user=user)
            user_data.delete()
            return JsonResponse({'message': 'User data deleted successfully'})
        except UserData.DoesNotExist:
            return JsonResponse({'error': 'User data not found'}, status=404)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
