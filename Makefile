LATEXMK ?= latexmk

TEX_DIR := tex
ACADEMIC_MAIN := $(TEX_DIR)/academic/main_academic.tex
MEMETIC_MAIN := $(TEX_DIR)/memetic/main_memetic.tex

.PHONY: all academic memetic clean

all: academic memetic

academic:
	$(LATEXMK) -cd -pdf $(ACADEMIC_MAIN)

memetic:
	$(LATEXMK) -cd -pdf $(MEMETIC_MAIN)

clean:
	$(LATEXMK) -cd -C $(ACADEMIC_MAIN)
	$(LATEXMK) -cd -C $(MEMETIC_MAIN)

