# Makefile

CC = g++
CFLAGS = -std=c++11
TARGET = my_program

SRCS = main.cpp file_read.cpp data_process.cpp file_write.cpp
OBJS = $(SRCS:.cpp=.o)

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

%.o: %.cpp
	$(CC) $(CFLAGS) -c $< -o $@

run: $(TARGET)
	@./$(TARGET)

clean:
	del $(OBJS) $(TARGET)
