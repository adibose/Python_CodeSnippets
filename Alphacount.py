def alphabet_count(s):
    output = ""

    if len(s) == 0 or s.isspace():
        output = None
    else:
        op = []
        curr = s[0]
        count = 0
        for i in s:
            if curr.lower() == i.lower():
                count += 1
            else:
                op.append(curr)
                op.append(str(count))
                curr = i
                count = 1
        op.append(curr)
        op.append(str(count))
        output = ''.join(op)

    # write your solution here

    return output

print(alphabet_count(""))