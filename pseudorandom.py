import nacl.utils

def pseudorand():

    rand = nacl.utils.random(128)
    rand_str = ""

    for i in rand:
        rand_str += hex(i)[2:] + " "
    return rand_str

pseudo  = pseudorand()
print(pseudo)