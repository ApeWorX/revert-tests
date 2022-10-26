import ape


def test_sample(contract, owner):
    with ape.reverts(dev_message="testing"):
        contract.divOneBy(0, sender=owner)
