from django.urls import path

from owners.views import OwnerView, DogView


urlpatterns = [
	
	path("owners", OwnerView.as_view()),
	path("dogs", DogView.as_view())
]

'''
Owners
http -v POST 127.0.0.1:8000/owners name='홍길동' email='abc123@naver.com' age=25
http -v GET 127.0.0.1:8000/owners
Dogs
http -v POST 127.0.0.1:8000/dogs name='아롱' age=25 owner_id=1
http -v GET 127.0.0.1:8000/dogs
'''