cmake_minimum_required(VERSION 3.17)

set(PROJECT_NAME {{ cookiecutter.project_name }})

project(${PROJECT_NAME} VERSION 0.1.0 LANGUAGES C CXX)
find_package(Threads REQUIRED)

# ---------------------------------------------------------------------------------------
# Set default build to release
# ---------------------------------------------------------------------------------------
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "Release" CACHE STRING "Choose Release or Debug" FORCE)
endif()
set(CMAKE_CXX_STANDARD 17) 
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_C_STANDARD 11)  
set(CMAKE_C_STANDARD_REQUIRED ON)


{% if cookiecutter.create_library  == 'y' and cookiecutter.header_only != 'y' %}
# ---------------------------------------------------------------------------------------
# Library {{ cookiecutter.library_name}}
# ---------------------------------------------------------------------------------------

{% if cookiecutter.library_name == 'default'% }
set(LIBRARY_NAME ${PROJECT_NAME})
{% else %}
set(LIBRARY_NAME {{ cookiecutter.library_name }})
{% endif%}

{% if cookiecutter.language == 'c' %} 
set(LIBSOURCES 
    src/hello.c
    # ----> Add more sources here
)
{% else %}
set(LIBSOURCES 
    src/hello.cpp
    # ----> Add more sources here
)
{% endif %}
add_library(${LIBRARY_NAME} STATIC ${LIBSOURCES})
target_include_directories(${LIBRARY_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
{% endif %}

{% if cookiecutter.create_application == 'y' %}

{% if cookiecutter.application_name != 'default' %}
set(APPLICATION_NAME ${PROJECT_NAME})
{% else %}
set(APPLICATION_NAME {{ cookiecutter.application_name }})
{% endif %}

{% if cookiecutter.language == 'c' %}
set(APPSOURCES 
    app/app.c
    # ----> Add more sources here
)
{% else %}
set(APPSOURCES 
    app/app.cpp
    # ----> Add more sources here
)
{% endif %}

add_executable(${APPLICATION_NAME} ${APPSOURCES})


{% if cookiecutter.create_library  == 'y' and cookiecutter.header_only != 'y' %}
target_link_libraries(${APPLICATION_NAME} PRIVATE 
    ${LIBRARY_NAME}
)
{% elif cookiecutter.create_library  == 'y' and cookiecutter.header_only == 'y' %}
target_include_directories(${APPLICATION_NAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
{% endif %}
{% endif %}

{% if cookiecutter.add_gtest == 'y' %}
# Unittests with gtest
set(TESTNAME ${PROJECT_NAME}_tests)

include(FetchContent)
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG e2239ee6043f73722e7aa812a459f54a28552929 # release-1.11
)
FetchContent_MakeAvailable(googletest)

enable_testing()
add_executable(${TESTNAME}
    tests/test_hello.cpp
)

target_link_libraries(${TESTNAME} PRIVATE 
{% if cookiecutter.create_library  == 'y' and cookiecutter.header_only != 'y' %}
${LIBRARY_NAME} 
{% endif %}
gtest_main
)

{% if cookiecutter.create_library == 'y' and cookiecutter.header_only == 'y' %}
target_include_directories(${TESTNAME} PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
{% endif %}

include(GoogleTest)
gtest_discover_tests(${TESTNAME})
{% endif %}

