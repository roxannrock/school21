import random
p = 23
g = 19   

def mod_func(number, stepen, module):
    return pow(number, stepen, module)

def generate_keys( p , g):
    private_key = random.randint(2 , p - 2)
    public_key = mod_func(g , private_key , p)
    return private_key , public_key

def computer_shared_secret(private_key , public_key, p):
    return mod_func(public_key , private_key , p)

alice_private , alice_public = generate_keys(p , g)
bob_private , bob_public = generate_keys(p , g)

alice_secret = computer_shared_secret(alice_private , bob_public , p)
bob_secret = computer_shared_secret(bob_private , alice_public , p)

print(alice_secret == bob_secret)