from brownie import ZombieFactory, ZombieFeeding, ZombieHelper, ZombieAttack, ZombieOwnership
from scripts.helpful_scripts import get_account


def deploy_zombie():
    account = get_account()
    zombiefactory = ZombieFactory.deploy({"from": account})
    print("Deployed ZombieFactory!")
    zombiefeeding = ZombieFeeding.deploy({"from": account})
    print("Deployed ZombieFeeding!")
    zombiehelper = ZombieHelper.deploy({"from": account})
    print("Deployed ZombieHelper!")
    zombieownership = ZombieOwnership.deploy({"from": account})
    print("Deployed ZombieOwnership!")

def main():
    deploy_zombie()