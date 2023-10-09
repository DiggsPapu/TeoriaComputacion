CC = g++
CFLAGS = -g -Wall
LDFLAGS = 
TARGET = main
SOURCE = main.cpp
DIR_COUNT = $(shell find ./profile/ex3 -maxdepth 1 -type d | wc -l)

all: $(TARGET)
$(TARGET): $(SOURCE)
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

.PHONY: run
run: $(TARGET) 
	$(eval DIR_COUNT := $(shell find ./profile/ex3 -maxdepth 1 -type d | wc -l))
	mkdir ./profile/ex3/record${DIR_COUNT}
	mkdir ./profile/ex3/record${DIR_COUNT}/normal
	mkdir ./profile/ex3/record${DIR_COUNT}/cycles
	perf record ./$<
	sudo cp perf.data ./profile/ex3/record${DIR_COUNT}/normal/perf.data
	perf record -e cycles ./$<
	sudo cp perf.data ./profile/ex3/record${DIR_COUNT}/cycles/perf.data
	rm -f $(TARGET)

.PHONY: report
	perf record -e cycles ./$<

.PHONY: clean
clean:
	$(eval DIR_COUNT := $(shell expr $(shell find ./profile/ex3 -maxdepth 1 -type d | wc -l) - 1))	
	@if [ -d "profile/ex3/record$(DIR_COUNT)" ]; then \
		rm -r profile/ex3/record$(DIR_COUNT); \
	fi
	rm -f $(TARGET)
	rm -f perf.data
	@if [ -f "perf.data.old" ]; then \
		rm -f perf.data.old; \
	fi