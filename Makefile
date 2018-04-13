default:
	@make clean
	@make run
install:
	@sudo pip install pil
run:
	@python app.py
clean:
	@clear