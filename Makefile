clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*-instr' -delete
	find . -type f -name '*.gcda' -delete
	find . -type f -name '*.gcno' -delete
	find . -type f -name '*.gcov' -delete
