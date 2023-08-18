AFN_DOT_FILES := $(wildcard AFN/*.dot)
AFN_PNG_FILES := $(patsubst AFN/%.dot,AFNPng/%.png,$(AFN_DOT_FILES))

Tree_DOT_FILES := $(wildcard Tree/*.dot)
Tree_PNG_FILES := $(patsubst Tree/%.dot,TreePng/%.png,$(Tree_DOT_FILES))

all: $(AFN_PNG_FILES) $(Tree_PNG_FILES)

AFNPng/%.png: AFN/%.dot
	dot -Tpng $< -o $@

TreePng/%.png: Tree/%.dot
	dot -Tpng $< -o $@

clean:
	rm -f TreePng/*.png
	rm -f AFNPng/*.png

.PHONY: all clean
