import os

crr_path = os.getcwd()
main_path= ''.join(i for i in os.listdir(crr_path) if i == '01_deeplabv3plus_with_dropout_0o6_and_0o7_Adam')
sub_dir= os.listdir(main_path)
def make_dir():
    i = input('Enter Index:')
    new_path = f'{i}{main_path[2:]}'
    os.makedirs(new_path)
    for path in sub_dir:
        new_crr_path = os.path.join(crr_path,new_path)
        os.makedirs(os.path.join(new_crr_path,path))

make_dir()
