### Python Setup

Using Python version 2.7.10

[Set up virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/#virtualenvironments-ref)

With `pip` and `virtualenv` installed, create a virtual environment in the current directory called `virt` and
enable it.

```
$ virtualenv virt
$ source virt/bin/activat
```

Now, use the virtual environment's version of `pip` to intall the package dependencies:

```
$ virt/bin/pip install -r dependencies.txt
```



### References

http://randomthoughts.greyhats.it/2015/02/fast-coverage-analysis-for-binary.html
