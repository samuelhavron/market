.PHONY: github post
MSG=small edit
github:
	git add -A 
	git commit -m "${MSG}"
	git push

post:
	python api-posts.py > err.html && google-chrome err.html