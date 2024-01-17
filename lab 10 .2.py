preproinsulin = ''' ORIGIN      
        1 malwmrllpl lallalwgpd paaafvnqhl cgshlvealy lvcgergffy tpktrreaed
       61 lqvgqvelgg gpgagslqpl alegslqkrg iveqcctsic slyqlenycn
//'''

unwanted_elements = ['ORIGIN', '61', '1', '//', ' ', '\n']
for element in unwanted_elements:
    preproinsulin = preproinsulin.replace(element, '')

print(preproinsulin)
print(len(preproinsulin))

lsinsulin = preproinsulin[0:24]
print(lsinsulin)
print(len(lsinsulin))

binsulin = preproinsulin[24:54]
print(binsulin)
print(len(binsulin))

cinsulin = preproinsulin[54:89]
print(cinsulin)
print(len(cinsulin))

ainsulin = preproinsulin[89:110]
print(ainsulin)
print(len(ainsulin))