default:
	@make clean
	@make run
install:
	@sudo pip install pil
	@sudo pip install numpy
	@sudo pip install scipy
run:
	@python app.py
clean:
	@clear