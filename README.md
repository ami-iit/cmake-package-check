# cmake-package-check

Command line utility to check if a CMake package exists.

## Installation

### From conda-forge

`cmake-package-check` is avalable in conda-forge, so it can be installed simply with:
~~~
conda install -c conda-forge cmake-package-check
~~~

### From source

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cmake-package-check.

```bash
python -m pip install git+https://github.com/ami-iit/cmake-package-check
```

The package assumes that the following tools used by CMake are already installed in the system, i.e.:
* C and C++ compiler
* CMake
* Ninja
* pkg-config


## Usage

### Check if a package exists

To check if the CMake package `fmt` is installed and can be found by the CMake, run:
```bash
cmake-package-check fmt
```

The command output will end with `cmake-package-check: SUCCESS.` if the package can be found (i.e. `find_package(fmt REQUIRED)` is successful), and with `cmake-package-check: FAILURE.` . In case of success the return value of the command will be 0, while it will be 1 if the package can't be found. This permits to use the command in the context of continuous integration scripts.

**Note: on Windows, the command needs to run in Developer Command Prompt or Developer Powershell.**

### Check if a multiple packages exist

You can also check if multiple packages can be found at once, for example to check if both `fmt` and `Eigen3` can be found you can run:

~~~bash
cmake-package-check fmt Eigen3
~~~

### Use to test in conda recipes if a CMake package is installed

`cmake-package-check` can be used to quickly check in the test section of a conda recipe if a given CMake package is installed. 
For example, if you have a package that installs a CMake package called `CMakePackage`, you can check if the CMake package can be correctly found by adding to your recipe:
~~~yaml
test:
  commands:
    - cmake-package-check CMakePackage
  requires:
    - cmake-package-check
    - {{ compiler('c') }}
    - {{ compiler('cxx') }}
~~~

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html)
