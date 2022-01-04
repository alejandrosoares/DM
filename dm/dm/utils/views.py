from user_information.models import UserInformation

def get_user(cookies):
    
    # 2020251100000 is id of anonymous user
    userid = cookies.get('userid', "2020251100000")
    
    try:
        user = UserInformation.objects.get(userid=userid)
    except UserInformation.DoesNotExist:
        user = UserInformation.objects.get(userid="2020251100000")
        
    return user