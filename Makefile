CC = g++
CFLAGS = -g -Wall
LDFLAGS = 
TARGET = main
SOURCE = main.cpp
DIR_COUNT = $(shell find ./profile/ex2 -maxdepth 1 -type d | wc -l)

all: $(TARGET)
$(TARGET): $(SOURCE)
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

.PHONY: run
run: $(TARGET) 
	perf stat -e duration_time ./$<
	rm -f ./$<

.PHONY: report
	perf record -e cycles ./$<

.PHONY: clean
clean:
	$(eval DIR_COUNT := $(shell expr $(shell find ./profile/ex2 -maxdepth 1 -type d | wc -l) - 1))	
	@if [ -d "profile/ex2/record$(DIR_COUNT)" ]; then \
		rm -r profile/ex2/record$(DIR_COUNT); \
	fi
	rm -f $(TARGET)
	rm -f perf.data
	@if [ -f "perf.data.old" ]; then \
		rm -f perf.data.old; \
	fi