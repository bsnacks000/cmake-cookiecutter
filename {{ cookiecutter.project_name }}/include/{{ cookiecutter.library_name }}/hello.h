#ifndef __HELLO__H__
#define __HELLO__H__

#ifdef __cplusplus
extern "C"{
#endif


{% if cookiecutter.create_library == 'y' and cookiecutter.header_only == 'y' %}
char* hello() { return "hello world\n"; };
{% else %}
char* hello();
{% endif %}



#ifdef __cplusplus
}
#endif

#endif  //!__HELLO__H__