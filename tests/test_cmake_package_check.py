from cmake_package_check.cmake_package_check import cmake_package_check

def test_threads():
    # If CMake works fine and the platform is a "regular" one, find_package(Threads REQUIRED) should always return true,
    # see https://cmake.org/cmake/help/latest/module/FindThreads.html
    assert cmake_package_check(["Threads"])

def test_threads_target():
    # If CMake works fine and the platform is a "regular" one, find_package(Threads REQUIRED) should always return true,
    # see https://cmake.org/cmake/help/latest/module/FindThreads.html
    assert cmake_package_check(["Threads"], targets=["Threads::Threads"])

def test_package_exists_but_target_not():
    assert not cmake_package_check(["Threads"], targets=["Threads::ThisIsNotARealTargetAndWillNeverExists"])

def test_non_existing_package():
    assert not cmake_package_check(["ThisIsNotACMakePackageName"])
