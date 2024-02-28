userBD="hidrotech123"
passwordBD="admin123*"

print('Software tech hidroituango')
print('**************************')
userName=input('Digita tu usuario: ')
userPassword=input('Digita tu contraseña: ')

if(userBD==userName):
    print("Exito en su usuario")
else:
    print('Fallaste')


'''print("Exito en su usuario") if userBD==userName and 
passwordBD==userPassword else print('Fallaste')'''
