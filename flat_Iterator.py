class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.main_list_cursor = 0
        self.nest_list_cursor = -1
        return self

    def __next__(self):

        self.nest_list_cursor += 1
        if self.nest_list_cursor >= len(self.list_of_list[self.main_list_cursor]):
            self.main_list_cursor += 1
            self.nest_list_cursor = 0
            if self.main_list_cursor >= len(self.list_of_list):
                raise StopIteration
        return self.list_of_list[self.main_list_cursor][self.nest_list_cursor]


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    #print(list(FlatIterator(list_of_lists_1)))

if __name__ == '__main__':
    test_1()

