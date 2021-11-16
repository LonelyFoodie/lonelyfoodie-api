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
