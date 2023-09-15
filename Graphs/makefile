AFN_DOT_FILES := $(wildcard AFN/*.dot)
AFN_PNG_FILES := $(patsubst AFN/%.dot,AFNPng/%.png,$(AFN_DOT_FILES))

Tree_DOT_FILES := $(wildcard Tree/*.dot)
Tree_PNG_FILES := $(patsubst Tree/%.dot,TreePng/%.png,$(Tree_DOT_FILES))


AFD_DOT_FILES := $(wildcard AFD/*.dot)
AFD_PNG_FILES := $(patsubst AFD/%.dot,AFDPng/%.png,$(AFD_DOT_FILES))

AFDSIMPLIFIED_DOT_FILES := $(wildcard SimplifiedAFD/*.dot)
AFDSIMPLIFIED_PNG_FILES := $(patsubst SimplifiedAFD/%.dot,SimplifiedAFDPng/%.png,$(AFDSIMPLIFIED_DOT_FILES))

all: $(AFN_PNG_FILES) $(Tree_PNG_FILES)  $(AFD_PNG_FILES) $(AFDSIMPLIFIED_PNG_FILES)

AFNPng/%.png: AFN/%.dot
	dot -Tpng $< -o $@

TreePng/%.png: Tree/%.dot
	dot -Tpng $< -o $@

AFDPng/%.png: AFD/%.dot
	dot -Tpng $< -o $@

SimplifiedAFDPng/%.png: SimplifiedAFD/%.dot
	dot -Tpng $< -o $@

clean:
	rm -f TreePng/*.png
	rm -f AFNPng/*.png
	rm -f AFDPng/*.png
	rm -f SimplifiedAFDPng/*.png
	rm -f AFD/*.dot
	rm -f AFN/*.dot
	rm -f Tree/*.dot
	rm -f SimplifiedAFD/*.dot
.PHONY: all clean
