docker run -it \
 --name data-copier --rm \
 --network data-copier-nw \
 -v /Users/chris/documents/python/research/data/retail_db_json:/retail_db_json \
 -e BASE_DIR=/retail_db_json \
 -e DB_HOST=5764ece03b7e \
 -e DB_PORT=5432 \
 -e DB_NAME=retail_db \
 -e DB_USER=retail_user \
 -e DB_PASS=retail_user \
 data-copier python /data-copier/app/app.py departments,categories
