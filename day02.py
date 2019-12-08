# take the file input, split it by lines to remove trailing \n
# take the first part of the list cos we know that's where our values are -___-
# then split it by , into a list of items
# then apply (map) to each item the int() to make each item an integer

txt = open("day02_input")

code = list(map(int, txt.read().splitlines()[0].split(',')))
txt.close()

i = 0 
while i+3 < len(code):
    opscode = code[i]
    input1Pos = code[i+1]
    input2Pos = code[i+2]
    outputPos = code[i+3]

    if opscode == 1:
        code[outputPos] = code[input1Pos] + code[input2Pos]
    elif opscode == 2:
        code[outputPos] = code[input1Pos] * code[input2Pos]
    elif opscode == 99:
        break
    else:
        pass
    i = i + 4

print(code[0])



