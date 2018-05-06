default:
	@make clean
	@make run
install:
	@sudo pip install pil
	@sudo pip install numpy
	@sudo pip install scipy
gray:
	@python grey.py
sobel:
	@python sobelFilter.py
prewitt:
	@python prewittFilter.py
clean:
	@clear