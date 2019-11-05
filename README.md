Create shared directory with for cpp files with inside the bigint directory:
g++ -c -fPIC bigint.cpp -o bigint.o
g++ -shared -Wl,-soname,libbigint.so -o libbigint.so bigint.o


This project has several algorithms for calculating fibonacci:
* Using python ints
* Using a bigint struct in cpp (called from python - reason for shared library)
* Using python strings (really slow)


Conclusion:
Python performed the best. At around 100,000,000 Python's FibCassini matrix style surpases Python's FibMatrix style. 