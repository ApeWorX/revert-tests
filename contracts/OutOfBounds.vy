# @version 0.3.7

owner: public(address)

@external
def __init__():
	self.owner = msg.sender

@external
def outOfStaticBounds(_value: int8) -> int8:
	list: int8[5] = empty(int8[5])
	return list[_value] # dev: outOfStaticBounds caused an error.

@external
def outOfDynamicBounds(_value: int8) -> int8:
	list: DynArray[int8, 3] = []
	list.append(0)
	list.append(1)
	list.append(2)
	return list[_value] # dev: outOfDynamicBounds caused an error.

@external
def popEmptyDynArray() -> int8:
	list: DynArray[int8, 1] = []
	return list.pop() # dev: popEmptyDynArray caused an error.
