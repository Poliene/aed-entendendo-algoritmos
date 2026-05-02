def kth_to_last(head, k):
    if head is None or k <= 0:
        return -1

    p1 = head
    p2 = head

    # anda p2 k passos
    for _ in range(k):
        if p2 is None:
            return -1
        p2 = p2.next

    # anda os dois juntos
    while p2 is not None:
        p1 = p1.next
        p2 = p2.next

    return p1.value