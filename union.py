from LinkedList import SLinked_List

def union(p1, p2):
    answer = []
    while p1 and p2:
        if p1.getData() == p2.getData():
            answer.append(p1.getData())
            p1 = p1.getNext()
            p2 = p2.getNext()
        elif p1.getData() < p2.getData():
            answer.append(p1.getData())
            p1 = p1.getNext()
        else:
            answer.append(p2.getData())
            p2 = p2.getNext()
    while p1:
        answer.append(p1.getData())
        p1 = p1.getNext()

    while p2:
        answer.append(p2.getData())
        p2 = p2.getNext()

    return answer

def main():

    brutus = SLinked_List()
    calpurnia = SLinked_List()
    for doc_id in [1,2,4,11,31,45,173,174]:
        brutus.append(doc_id)

    for doc_id in [2,31,54,101]:
        calpurnia.append(doc_id)

    answer = union(brutus.getHead(), calpurnia.getHead())
    print(answer)


main()
