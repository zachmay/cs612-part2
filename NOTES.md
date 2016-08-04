### Notes/

http://randomthoughts.greyhats.it/2015/02/fast-coverage-analysis-for-binary.html

Clang: dump CFG

`clang -fsyntax-only -Xclang -analyze -Xclang -analyzer-checker=debug.DumpCFG test.c`
`clang -fsyntax-only -Xclang -analyze -Xclang -analyzer-checker=debug.DumpDominators test.c`

Basic blocks

Coverage Mapping: http://llvm.org/docs/CoverageMappingFormat.html

- CDG via forward dominance: https://www.cs.colorado.edu/~kena/classes/5828/s00/lectures/lecture15.pdf
- http://www.cc.gatech.edu/~harrold/6340/cs6340_fall2009/Slides/BasicAnalysis4.pdf
- http://logan.tw/posts/2015/04/28/check-code-coverage-with-clang-and-lcov/
- http://lowlevelbits.org/getting-started-with-llvm/clang-on-os-x/
