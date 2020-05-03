

def remove_tags(s):
    li = list(s)

    try:
        for i in range(len(li)):
            if li[i]=="<":
                a = li.index(">")
                diff = a-i
                while diff>=0:
                    li.pop(i)
                    diff-=1
            else:
                continue
    except IndexError:
        pass
    output = ''.join(li)
    return output
p="<p>The <i>price to earnings ratio (PE Ratio)</i> is the measure of the share price relative to the annual net income earned by the firm per share.</p>"

s = remove_tags(p)
print(s)
