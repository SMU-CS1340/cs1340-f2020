SLIDES := $(patsubst %.md,%.md.slides.pdf,$(wildcard *.md))
HANDOUTS := $(patsubst %.md,%.md.handout.pdf,$(wildcard *.md))

all : $(SLIDES) $(HANDOUTS)

%.md.slides.pdf : %.md
	pandoc $^ -t beamer -V mainfont="Linux Libertine O" -V monofont="DejaVu Sans Mono" --slide-level 2 --include-in-header font.tex --pdf-engine=xelatex -F ./filter_pandoc_run_py.py -o $@
	#pandoc $^ -t beamer --slide-level 2 --pdf-engine=xelatex --include-in-header font.tex -o $@

%.md.handout.pdf : %.md
	pandoc $^ -t beamer --slide-level 2 -V mainfont="Linux Libertine O" -V monofont="DejaVu Sans Mono" --pdf-engine=xelatex --include-in-header font.tex -V handout -F ./filter_pandoc_run_py.py -o $@ 
	#pandoc $^ -t beamer --slide-level 2 --pdf-engine=xelatex -V handout --include-in-header font.tex  -o $@ 
	pdfnup $@ --nup 1x2 --no-landscape --keepinfo \
		--paper letterpaper --frame true --scale 0.9 \
		--suffix "nup"
	mv $*.md.handout-nup.pdf $@
		

clobber : 
	rm -f $(SLIDES)
	rm -f $(HANDOUTS)

