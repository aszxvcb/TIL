def solution(phone_book):
    answer = True

    phone_book.sort()

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if( p2.startswith(p1) ):
            return False

    return answer


if __name__ == "__main__":

    phone_book = ["12","123","1235","567","88"]
    ret = solution(phone_book)
    print(ret)