import pytest


@pytest.fixture()
def emitter_contract(web3_tester, EmitterContract):
    deploy_txn = EmitterContract.deploy()
    deploy_receipt = emitter_contract.eth.getTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    _emitter_contract = EmitterContract(address=deploy_receipt['contractAddress'])
    return _emitter_contract


def test_past_events_with_single_event(emitter_contract):
    event_txn = emitter_contract.transact().logSingle(1234)
    event_receipt = emitter_contract.eth.getTransactionReceipt(deploy_txn)

    assert False
