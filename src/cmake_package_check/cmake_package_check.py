import os
import sys
import subprocess
import tempfile
from jinja2 import Template, Environment, PackageLoader
import argparse

def cmake_package_check(CMakePackageNames):
    temp_dir = tempfile.mkdtemp()

    try:
        # Prepare context for Jinja2 template
        context = {
            'CMakePackageNames': CMakePackageNames
        }

        # Render CMakeLists.txt from the Jinja2 template
        environment = Environment(loader=PackageLoader("cmake_package_check"))
        template = environment.get_template("CMakeLists.txt.in")
        cmake_content = template.render(context)

        # Write the rendered CMakeLists.txt to the temporary directory
        os.chdir(temp_dir)
        with open('CMakeLists.txt', 'w') as f:
            f.write(cmake_content)

        print("===================================")
        print("=== Generated CMakeLists.txt file: ")
        print("===================================")
        print(cmake_content)

        # Run CMake in the temporary directory
        print("===================================")
        print("=== CMake configure output:        ")
        print("===================================")
        subprocess.run(['cmake','-jNinja','-S.', '-B.'], cwd=temp_dir, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        return False

    # If all is ok, return true
    return True


def main():
    parser = argparse.ArgumentParser(description="Utility to check if a CMake package exists.")
    parser.add_argument("CMakePackageNames", metavar="CMakePackageNames", type=str, nargs="+", help="Names of the cmake packages to check the existence")

    args = parser.parse_args()
    result = cmake_package_check(args.CMakePackageNames)

    print("===================================")
    print("=== Result:")
    print("===================================")

    if(result):
        print("cmake-package-check: SUCCESS.")
        sys.exit(0)
    else:
        print("cmake-package-check: FAILURE.")
        sys.exit(1)

if __name__ == "__main__":
    main()
