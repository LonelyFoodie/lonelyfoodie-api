Lonely Foodie API
=============

1. Install Docker Desktop
2. Run this command
~~~ bash
git clone https://github.com/LonelyFoodie/lonelyfoodie-api.git
cd lonelyfoodie-api
docker-compose up -d --build
~~~
3. Check http://0.0.0.0:5000/api/

If you need migration, run
~~~ bash
docker exec -it lonelyfoodie-api alembic upgrade head
~~~

Kakao Sign up test
check http://localhost:5000/api/oauth
follow the procces sign-up
go to http://0.0.0.0:5000/api/
check /user/ (get)
현재 구현한 방식은 카카오 인증을 거친 후 카카오에서 가져올 수 있는 정보를 넣어
db에 저장하고 나머지 필요한 부분은 db수정 기능을 통해서 입력받는 방식으로 만들어 봤습니다.

