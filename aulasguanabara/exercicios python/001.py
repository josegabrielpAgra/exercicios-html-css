while True:
  a=input('digite seu nome aqui ->')

  if any(char.isdigit() for char in a):
     print('seu nome de usuario não pode ter numeros.')
  
  else:
    break
while True:
    b=input('digite sua senha aqui ->')
    
    if any(char.isdigit() for char in b) and \  
       any(char.isupper() for char in b) and \
       any(char.islower() for char in b):
        print('seu cadastro foi feito com sucesso')  
        break 
    else:
        print('sua senha tem que ter numero,letras minusculas e maiusculas.')   
    