import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import Drink, Category
class ProductListView(View):
    def get(self, request):
        # Client의 요청을 처리할 수 있는 Logic
        """""
        함수의 목적: client의 상품 정보 요청에 맞게 database에 상품 정보 호출 및 가공 후 상품 데이터 반환

        삼풍 정보 생성

        1. Input: http -v GET http://127.0.0.1:8000/products 에서 마지막 products
            

        2. Output: 상품 목록
            result = [
                {
                    "id" : 1,
                    "description": "test",
                    "english_name": "test",
                    "korean_name": "나이트로 바닐라 크림",
                    "category": {
                        "id" : 1,
                        "name" : "콜드브루"
                    }
                },
                {
                    "id" : 2,
                    "description": "test",
                    "english_name": "test",
                   "korean_name": "나이트로 바닐라 크림",
                    "category": {
                        "id" : 1,
                        "name" : "콜드브루"
                    }
                }
            ]

        3. How: Product 테이블의 모든 상품 데이터 조회

        python manage.py shell에서 데이터들을 조회하면 from product.models import Drink --> Drink.objects.all()
        <QuerySet [<Drink: Drink object (1)>, <Drink: Drink object (2)>, <Drink: Drink object (3)>, <Drink: Drink object (4)>, <Drink: Drink object (5)>, <Drink: Drink object (6)>, <Drink: Drink object (7)>, <Drink: Drink object (8)>, <Drink: Drink object (9)>, <Drink: Drink object (10)>]>
        이런식으로 받아옴. 이 데이터를 가공해야함
        Drink Instance 들을 python의 native한 data type인 dictionary로 변환해줘야한다.

        """

        # (3)번 과정 바로 
        drinks = Drink.objects.all()

        results = []

        for drink in drinks:
            # category = Category.objects.get(drink__id = drink.id)
            results.append(
                {
                    "id" : drink.id,
                    "description" : drink.description,
                    "english_name" : drink.english_name,
                    "korean_name" : drink.korean_name,
                    "category" : {
                        "id" : drink.category.id,
                        "name" : drink.category.name 
                    }
                }
            )

        return JsonResponse({"drinks": results }, status=200)
        

    def post(self, request):
        """""
        함수의 목적: client의 상품 등록 요청에 맞게 database에
        삼풍 정보 생성

        1. Input: Product 데이터(json)
            

        2. Output: 상품의 등록 여부 {"message": "SUCCESS"}

        3. How: Input으로 들어온 상품 데이터를 ORM을
        이용해서 twinny_practice database의 Product
        테이블에 Data 저장.
            (1) json data --> python dictionary 변환
            {
              "category_id": 1,
              "description": "test",
              "english_name": "test",
             "korean_name": "나이트로 바닐라 크림"
            }

            (2) Product.object.create(Input 데이터)

            (3) return {"message": "SUCCESS"} (dictionary) --> json data 변환 후 반환 
        """

        print(f"request.body :: {request.body}")
        # (1)번 과정
        input_data = json.loads(request.body)
        # print(f"json_loaded input_body :: {input_data}")

        # (2)번 과정
        Category.objects.create(name = input_data["category_name"])


        Drink.objects.create(
            korean_name = input_data["korean_name"],
            english_name = input_data["english_name"],
            description = input_data["description"],
            category_id = input_data["category_id"]
        )

        print(f"json_loaded input_body :: {input_data}")
        return JsonResponse({"message": "SUCCESS"}, status = 201)