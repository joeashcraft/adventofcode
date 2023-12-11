.PHONY: new help check-vars solution test input
YEAR=2023
export YEAR := $(YEAR)

help: 
	@echo "Commands:"
	@echo " - help: 	show this help"
	@echo " - new:		create a new file for today"

check-vars:
ifndef DAY
	$(error DAY is undefined)
endif

solution:
	envsubst < template.py.sh > day$(DAY).py
	#cp template.py day$(DAY).py

test:
	envsubst < template_test.py.sh > day$(DAY)_test.py
	#cp template_test.py day$(DAY)_test.py

input:
ifndef SESSION
	$(error SESSION is undefined)
endif
	wget --header "Cookie: session=$(SESSION)" --output-document=day$(DAY)-input.txt 'https://adventofcode.com/$(YEAR)/day/$(DAY)/input'

new: check-vars  solution  test
#	input
