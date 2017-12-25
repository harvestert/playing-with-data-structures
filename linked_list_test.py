from linked_list import LinkedList


def test_empty_list():
    # Given - An empty list
    lst = LinkedList()

    # Then - list is empty
    assert lst.size() == 0
    assert lst.head is None


def test_add_one_item():
    # Given - An empty list
    lst = LinkedList()

    # When - Adding one item
    lst.add(5)

    # Then - Item is added to list
    assert lst.size() == 1
    head_node = lst.head
    assert head_node.value == 5
    assert head_node.next is None


def test_add_multiple_items():
    # Given - An empty list
    lst = LinkedList()

    # When - Adding multiple items
    lst.add(5)
    lst.add("zigi3")
    lst.add(234)

    assert lst.size() == 3

    node = lst.head

    assert node.value == 5
    node = node.next
    assert node.value == "zigi3"
    node = node.next
    assert node.value == 234


def test_add_duplicate_items():
    # Given - An empty list
    lst = LinkedList()

    # When - Adding multiple items
    lst.add(5)
    lst.add(5)

    # Then - Both items were added
    assert lst.size() == 2
    node = lst.head
    assert node.value == 5
    node = node.next
    assert node.value == 5


def test_delete_from_empty_list():
    # Given - An empty list
    lst = LinkedList()
    assert lst.size() == 0

    # When - Deleting object that does not exist
    lst.delete(3)

    # Then - List size is still 0
    assert lst.size() == 0


def test_delete_none_existing():
    # Given - A list with five items
    lst = LinkedList()
    lst.add(324)
    lst.add("A")
    lst.add(3221)
    lst.add(333)
    lst.add(433)
    assert lst.size() == 5

    # When - Deleting object that does not exist
    lst.delete(3)

    # Then - List size is still 5
    assert lst.size() == 5


def test_delete_from_head():
    # Given - A list with one item
    lst = LinkedList()
    lst.add(324)
    assert lst.size() == 1

    # When - Deleting object that exist in list
    lst.delete(324)

    # Then - List size is reduced to 0
    assert lst.size() == 0


def test_delete_existing_from_middle():
    # Given - A list with one item
    lst = LinkedList()
    lst.add("zig")
    lst.add(453)
    lst.add(324)
    lst.add(432)
    assert lst.size() == 4

    # When - Deleting object that exist in list
    lst.delete(324)

    # Then - List size is reduced to 3
    assert lst.size() == 3


def test_delete_existing_from_end():
    # Given - A list with one item
    lst = LinkedList()
    lst.add("zig")
    lst.add(453)
    lst.add(324)
    assert lst.size() == 3

    # When - Deleting object that exist in list
    lst.delete(324)

    # Then - List size is reduced to 2
    assert lst.size() == 2


def test_one_item_of_multiple_duplicates():
    # Given - A list with multiple duplicate items
    lst = LinkedList()
    lst.add(123)
    lst.add(123)
    lst.add(123)
    assert lst.size() == 3

    # When - Deleting object that exist in list
    lst.delete(123)

    # Then - List size is reduced to 2
    assert lst.size() == 2
