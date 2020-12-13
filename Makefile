dev:
	cd app && poetry run uvicorn main:app --reload

test:
	poetry run pytest

create-items:
	curl -X POST localhost:8000/foo/item/   --data '{"description":"some item description", "public":false}' && echo
	curl -X POST localhost:8000/foo/item/   --data '{"description":"some item description", "public":true}'

get-items:
	curl -X GET localhost:8000/foo/item/1 && echo
	curl -X GET localhost:8000/foo/item/2