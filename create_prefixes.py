
genders = 'masculine feminine neuter plural'.split()
cases = 'nominative accusative dative genitive'.split()

prefixes = [f'{gender}_{case_}_' for gender in genders for case_ in cases]

for prefix in prefixes:
    print(prefix)

# OUT: masculine_nominative_
# OUT: masculine_accusative_
# OUT: masculine_dative_
# OUT: masculine_genitive_
# OUT: feminine_nominative_
# OUT: feminine_accusative_
# OUT: feminine_dative_
# OUT: feminine_genitive_
# OUT: neuter_nominative_
# OUT: neuter_accusative_
# OUT: neuter_dative_
# OUT: neuter_genitive_
# OUT: plural_nominative_
# OUT: plural_accusative_
# OUT: plural_dative_
# OUT: plural_genitive_

prefixes = [f'{case_}_{gender}_' for case_ in cases for gender in genders]
### 