CC = g++
CFLAGS = -g -Wall
LDFLAGS = 
TARGET = main
SOURCE = main.cpp

all: $(TARGET)

$(TARGET): $(SOURCE)
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

.PHONY: run
run: $(TARGET)
	perf record -e cycles ./$<

.PHONY: report
	perf record -e cycles ./$<

.PHONY: clean
clean:
	rm -f $(TARGET)