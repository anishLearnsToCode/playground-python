class TestDataEmptyArray(object):

    @staticmethod
    def get_array():
        return []


class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        return [0, 1]

    @staticmethod
    def get_expected_result():
        return 0


class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        return [10, 10]

    @staticmethod
    def get_expected_result():
        return 0
