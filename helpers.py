from dataclasses import dataclass


@dataclass
class HarmonicSerie:
    one: int = 1
    two: int = 2
    three: int = 3
    four: int = 4
    five: int = 5
    six: int = 6
    seven: int = 7
    eight: int = 8
    nine: int = 9
    ten: int = 10
    eleven: int = 11
    twelve: int = 12
    thirteen: int = 13
    fourteen: int = 14
    fifteen: int = 15
    sixteen: int = 16

    def get_string_number(self, int_number: int) -> str:
        for string_number in self.__annotations__:
            if self.__getattribute__(string_number) == int_number:
                return string_number
        self._raise_value_error(int_number)

    def get_integer_number(self, str_number: str) -> int:
        if str_number in self.__annotations__:
            return self.__getattribute__(str_number)
        self._raise_value_error(str_number)

    def _raise_value_error(self, str):
        raise ValueError(
            f"{str} does not exist in Harmonic Series! -> [1, 16]")
