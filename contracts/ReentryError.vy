# @version 0.3.7

owner: public(address)

@external
def __init__():
	self.owner = msg.sender

@internal
@nonreentrant('lock')
def _reentrant(): # dev: nonreentrantFunction caused an error.
	pass

@external
@nonreentrant('lock')
def nonreentrantFunction():
	self._reentrant()

@internal
@nonreentrant('lock')
def _nestThree(): # dev: nestedNonreentrantFunction caused an error.
	pass

@internal
def _nestTwo():
	self._nestThree()

@internal
def _nestOne():
	self._nestTwo()

@external
@nonreentrant('lock')
def nestedNonreentrantFunction():
	self._nestOne()
