"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730288863"


class Simpy:
    values: list[float]

    def __provide__(self, values: list[float]): 
        """Provides a list of floats as the arguement."""
        self.values = values
    
    def __repr__(self) -> str:
        """Way to represent object as string."""
        return f"{self.values}"
    
    def fill(self, filler: float, numfill: int) -> None:
        """Changes values list and fills in with new values.""" 
        self.values.clear()
        self.values.extend([filler] * numfill)
    
    def arange(self, start: float, stop: float, step: float) -> None:
        """Fills in the values in a range between start and step, step is 1."""
        assert step != 0.0 
        self.values.clear()
        while start != stop:
            self.values.append(start)
            start += step
    
    def sum(self) -> float:
        """Creates sum of list values."""
        summation: float = sum(self.values)
        return summation
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Increse list of values by another value or list of values."""
        if isinstance(rhs, float):
            result: list[float] = []
            for item in self.values:
                result.append(item + rhs)
            return Simpy(result)
        else: 
            assert len(self.values) == len(rhs.values)
            result: list[float] = []
            for i in range(len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
            return Simpy(result)
        
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raise a list of values by another value or list of values."""
        if isinstance(rhs, float):
            result: list[float] = []
            for item in self.values: 
                result.append(item ** rhs)
            return Simpy(result)
        else:
            assert len(self.values) == len(rhs.values)
            result: list[float] = []
            for i in range(len(self.values)):
                result.append(self.values[i] % rhs.values[i])
            return Simpy(result)
    
    def __mod__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Calculates difference between a list of values and another value or list of values."""
        if isinstance(rhs, float):
            result: list[float] = []
            for item in self.values:
                result.append(item % rhs)
            return Simpy(result)
        else:
            assert len(self.values) == len(rhs.values)
            result: list[float] = []
            for i in range(len(self.values)):
                result.append(self.values[i] % rhs.values[i])
            return Simpy(result)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Calcualtes if list of values equals another value or list of values."""
        if isinstance(rhs, float):
            result: list[float] = []
            for item in self.values:
                if item == rhs:
                    result.append(True)
                else:
                    result.append(False)
            return Simpy(result)
        else:
            result: list[float] = []
            for i in range(len(self.values)):
                if self.values[i] == rhs[i]:
                    result.append(True)
                else:
                    result.append(False)
            return Simpy(result)

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Calculates if list of values is greater than another value or list of values."""
        if isinstance(rhs, float):
            result: list[float] = []
            for item in self.values:
                if item > rhs:
                    result.append(True)
                else:
                    result.append(False)
            return Simpy(result)
        else:
            result: list[float] = []
            for i in range(len(self.values)):
                if self.values[i] > rhs[i]:
                    result.append(True)
                else:
                    result.append(False)
            return Simpy(result)

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overloads subscription notation for Simpy."""
        if isinstance(rhs, int):
            num: float = 0
            while num < len(self.values):
                if rhs == num:
                    return self.values[num]
                else:
                    num += 1
        else:
            result: list[float] = []
            for i in range(len(self.values)):
                if rhs[i] == True:
                    result.append(self.values[i])
            return Simpy(result)
