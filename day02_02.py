# take the file input, split it by lines to remove trailing \n
# take the first part of the list cos we know that's where our values are -___-
# then split it by , into a list of items
# then apply (map) to each item the int() to make each item an integer

def output (code):
    pointer = 0
    outputPos = pointer + 3
    opscode = 0
    seek = 4

    while pointer + 3 < len(code):
        opscode = code[pointer]
        inputPos1 = code[pointer+1]
        inputPos2 = code[pointer+2]
        outputPos = code[pointer+3]

        if opscode == 1:
            code[outputPos] = code[inputPos1] + code[inputPos2]
        elif opscode == 2:
            code[outputPos] = code[inputPos1] * code[inputPos2]
        elif opscode == 99:
            break
        else:
            pass
        pointer += seek
    
    return code[0]



txt = open("day02_input")

code_original = list(map(int, txt.read().splitlines()[0].split(',')))

txt.close()

noun = 0
verb = 0

for noun in range(100):
    for verb in range(100):
        code = code_original.copy()
        code[1] = noun
        code[2] = verb

        if noun >= len(code) or verb >= len(code):
            break

        test_output = output(code)
        if (test_output == 19690720): # 19690720):
            print(100 * noun + verb)
        break
    else:
        continue
    break



#
#   which addresses in the list lead to
#   code[0] == 19690720
#   2 numbers added together = 19690720
#   2 numbers multiplied together = 19690720
#   
#   do I need to move through the list backwards? 
#   recursion ? 