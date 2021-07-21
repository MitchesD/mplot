all: install

install:
	sudo cp mplot /usr/local/bin/
	sudo mkdir -p /usr/local/include/mplot
	sudo cp *.py /usr/local/include/mplot/

