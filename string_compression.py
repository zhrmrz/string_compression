class Sol:
    def string_compression(self,list):
        l=len(list)
        cur_char=list[0]
        count=0
        for i in range(l+1):
            if cur_char!=list[i]:
                list.append(cur_char)
                list.append(count)
                count=1
                cur_char = list[i]
            else:
                count+=1
        list.reverse()
        for i in range(l):
            list.pop()
        list.reverse()
        return list


if __name__ == '__main__':
    p1=Sol()
    print(p1.string_compression(['a','a','b','b','b','c']))
