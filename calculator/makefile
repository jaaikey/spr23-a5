CFLAGS = -g -Wall -Wextra

default: calculator

calculator: addition.o subtraction.o multiplication.o division.o main.o
	cc $(CFLAGS) -o calculator addition.o subtraction.o multiplication.o division.o main.c

addition.o: addition.c operations.h
	cc $(CFLAGS) -c addition.c

subtraction.o: subtraction.c operations.h
	cc $(CFLAGS) -c subtraction.c

multiplication.o: multiplication.c operations.h
	cc $(CFLAGS) -c multiplication.c

division.o: division.c operations.h
	cc $(CFLAGS) -c division.c

main.o: main.c operations.h
	cc $(CFLAGS) -c main.c

clean:
	$(RM) calculator *.o *~
