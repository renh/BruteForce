# BruteForce V0.1
BruteForce randomly generate an exercise sheet contains arithmetic practices
for kindergarten or slightly higher grade (in China). Since most the calculations can be easily performed mentally, currently I did not generate the correponding answer sheet.

# Requirements
 * A modern operating system that can run CPython with the following modules...
 * Python (2.7+ or 3.4+)
 * matplotlib (2.0+)
 
# Install
BruteForce is a single file script, you can run it directly by invoking the python interpreter in the directory (say `$BF`) it lies.
```shell
$ cd $BF
$ python BruteForce.py -h
```

I personaly recommend the [Anacoda Python distribution](http://www.continuum.io), which contains most of the modules widely used in the scientific computation community, as well as Intel MKL acceleration with auto parallization via openmp.

# Run an example
```shell
python BruteForce -L 0 -U 99 -p +-x/
```
This command generates an exercise sheet with numbers in the range 0 to 100, with which addition, substraction, multiplication, and division operations are allowed.

  
# TODO
 - Ask my fortunate (??) kid to test it
 - If it really helps, upgrade more fancy functinalities...
  
