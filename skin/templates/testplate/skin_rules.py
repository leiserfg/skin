#here you can use this functions or import whatever you nit
#it's is yust python
#prompt, prompt_bool, echo_off_prompt, rm, call


class_name = prompt('class name: ')
class_hidenner = []
for c in class_name:
    if c.isupper():
        class_hidenner.append('_' + c)
    else:
        class_hidenner.append(c.upper())
class_hidenner = ''.join(class_hidenner) + '_H_'


file_name = class_name.lower()
class_hidenner = class_hidenner



#this function is for make some magic you want after rendering
#def post_render():
#   call(['me', '--maybe'])

