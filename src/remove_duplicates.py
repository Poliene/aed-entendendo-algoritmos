def remove_duplicates(head):
    current = head

    while current is not None:
        runner = current

        while runner.next is not None:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next

        current = current.next

    return head