from src.auth.schemas import UserCreateModel




auth_prefix = f"/api/v1/auth"



def test_user_creation(fake_session,fake_user_service,test_client):
    signup_data = {
        "username":"amala",
        "email":"amalajerin@gmail.com",
        "first_name":"amala",
        "last_name":"jerin",
        "password":"amalajerin"
    }
    response = test_client.post(
        url=f"{auth_prefix}/signup",
        json=signup_data,
    )
    user_data = UserCreateModel(**signup_data)

    fake_user_service.user_exists.assert_called_once()
    fake_user_service.user_exists.assert_called_once_with(signup_data["email"],fake_session)
    
    fake_user_service.create_user.assert_called_once()
    fake_user_service.create_user.assert_called_once_with(user_data,fake_session)





def test_user_creation():
    pass 

