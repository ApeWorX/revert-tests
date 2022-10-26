# @version 0.3.4

owner: public(address)

@external
def __init__():
	self.owner = msg.sender

@external
def causeError(_value: bool):
	assert not _value # dev: testing

@external
def causeRaise():
	raise # dev: testing

@internal
@nonreentrant('lock')
def _reentrant():
	pass

@external
@nonreentrant('lock')
def reentrant():
	self._reentrant()

@external
def divOneBy(_value: int8) -> int8:
	return 1 / _value # dev: testing
