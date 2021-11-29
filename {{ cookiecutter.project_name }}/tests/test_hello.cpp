#include<gtest/gtest.h> 
{% if cookiecutter.language == 'c'  and cookiecutter.create_library == 'y' %}
#include <{{ cookiecutter.library_name }}/hello.h>

TEST(HelloTest, Works) {
  char* s = hello();
}
{% elif cookiecutter.language == 'cpp'  and cookiecutter.create_library == 'y' %}
#include <{{ cookiecutter.library_name }}/hello.hpp>
#include <string>  

TEST(HelloTest, Works) {
  std::string s = hello(); 
}
{% else %}
TEST(Smoke, BasicAssertion) {
  ASSERT_EQ(1,1)
}
{% endif %}