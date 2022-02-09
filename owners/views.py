import json

from django.http import JsonResponse
from django.views import View
from owners.models import Owner, Dog

class OwnerView(View):
    def get(self, request):

        owners = Owner.objects.all()

        results = []

        for owner in owners:
            results.append(
                {
                    "name" : owner.name,
                    "email" : owner.email,
                    "age" : owner.age
                }
            )

        return JsonResponse({"owners": results}, status=200)

    def post(self, request):
        input_data = json.loads(request.body)
    
        Owner.objects.create(
            name = input_data["name"],
            email = input_data["email"],
            age = input_data["age"]
        )

        # try: 
        #     Owner.objects.create(
        #         name = input_data["name"],
        #         email = input_data["email"],
        #         age = input_data['age']
        #     )
        # except KeyError:
        #     return JsonResponse({'error_message': 'KEY_ERROR'}, status=400)

        return JsonResponse({"message": "SUCCESS"}, status = 201)


class DogView(View):
    def get(self, request):

        dogs = Dog.objects.all()

        results = []

        for dog in dogs:
            results.append(
                {
                    "name" : dog.name,
                    "email" : dog.email,
                    "age" : dog.age,
                    'owner' : {
                        'name' : dog.owner.name,
                        'age' : dog.owner.age
                    }
                }
            )

        return JsonResponse({"dogs": results}, status=200)

    def post(self, request):
        input_data = json.loads(request.body)

        Dog.objects.create(
            name = input_data["name"],
            age = input_data["age"],
            owner_id = input_data["owner_id"]
        )

        return JsonResponse({'message': 'CREATED'}, status=201)