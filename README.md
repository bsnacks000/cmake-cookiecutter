# cmake-cookiecutter 
-----------------

A cookicutter for small/medium size C/C++ projects with Cmake and an opinionated project structure. I tried to design this to give you just enough to get started on a small project similar to something like `cargo new` or `go mod init` in those languages.

* Sets up structured boiler for either C/C++ library and/or application. Library option can be linked or header only. 
* Option to include `googletest` from github in the project source tree.

## Usage 
-------

1. Install cookiecutter with pip `$ pip install cookiecutter` and make sure you can call it from your path. 
2. In the parent directory run `cookiecutter https://github.com/bsnacks000/cmake-cookiecutter` 
3. Follow the prompts 
    * `project_name`: The name of the project root folder. Will be created for you in the current directory. It will also be used to create the test target and as the defaults for `library_name` and `application_name`. 
    * `full_name`: Your name will land in the license.
    * `short_project_description`: Will land on your README.md 
    * `language`: Choose C++ or C as the project language. C headers will be linked via `extern C` so you can use `gtest` out of the box. 
    * `create_library`: Whether to create a `src` and `include` folders with source code and public headers. This will build a static library by default (`myrpoject.a`) but can be changed after project generation.
    * `library_name`: The name for your library (Ignore if not applicable)
    * `header_only`: If you want to make a header only library this will completely remove the `src` directory and use `target_include_directories` instead of `target_link_libraries` to link any targets. 
    * `create_application`: Whether to create an `app` folder with an executable. Note that the app will not link your library (you'll have to do that yourself).
    * `application_name`: What to name your binary (Ignore if not applicable)
    * `add_gtest`: Whether to add gtest to the project. Recommended if you are taking the thing you're working on seriously to any degree. The test target is called ${PROJECT_NAME}_tests
    * `open_source_license`: What license to use for the project.  
    * `git_init`: Whether to initialize a git repository after build with the default .gitignore

Note that I default cmake to use c++17 and c11 since that is what I use for projects. Change this afterwards if you wish... 

The folder structure looks like this: 
```
project/ 
    /app                         # seperate application directory. If you chose library will be automatically linked...
        - app.c or app.cpp 
    /include
        /library_name            # public header folder... use like #include <mylibname/myheader.hpp>
            - hello.hpp or hello.h    
        README.md
    /src 
        - hello.cpp or hello.c    # source files (duh)
    /tests 
        - test_hello.cpp          # gtest source files 
    .gitignroe 
    CMakeLists.txt 
    LICENSE 
    README.md 
```

After the project is created (assuming your project is called `myproject`) do standard `cmake` things:
```bash 
$ cd myproject
$ mkdir build && cd build 
$ cmake .. 
``` 
...should create the build system for your project. If you selected `gtest`, when you build the test target, cmake will use `FetchContent_Declare` to reach out and grab a commit from the `googletest` github and build it in the project source tree. Note the default script just grabs gtest and does not check if its on your system. If you have also chosen to create a library it will be linked with gtest by default or if the library is header only it will point to `include/`. 

Note that this isn't some comprehensive, super pro build setup nor does it integrate with package managers like `conan` or contain any scripts for CI/CD. While these can easily be added to this boiler after its generated and your project grows, chances are if that is what you need then you probably don't need this utility! 

ok byee.