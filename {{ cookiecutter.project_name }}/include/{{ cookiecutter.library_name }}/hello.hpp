#ifndef __HELLO__H__
#define __HELLO__H__

#include <string>

{% if cookiecutter.create_library == 'y' and cookiecutter.header_only == 'y' %}
std::string hello() { std::string{"hello world\n"};}
{% else %}
std::string hello();
{% endif %}

#endif  //!__HELLO__H__