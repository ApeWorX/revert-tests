# @version 0.3.7

owner: public(address)

@external
def __init__():
	self.owner = msg.sender

@external
def convertNegativeWei(_value: int128) -> uint256:
	return as_wei_value(_value, "ether") # dev: convertNegativeWei caused an error.

