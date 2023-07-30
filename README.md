# cmake-package-check

Command line utility to check if a CMake package exists.

## Installation

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

~~~
cmake-package-check fmt Eigen3
~~~




## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html)
