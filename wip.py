import smartpy as sp

class Hashlock(sp.Contract):
    def __init__(self, hashed):
            self.init(hashed = sp.chest(hashed), used = False, commits = sp.big_map())

    @sp.entry_point
    def commit(self, params):
        p = sp.bytes(params)
        # p = params
        commit = sp.record(date = sp.timestamp_from_utc_now() ,
                           salted_hash = p)
        self.data.commits[sp.sender] = commit

    # @sp.entry_point
    # def reveal(self, params):
    #     sp.if self.data.used:
    #         sp.failwith("This contract has already been used.")
    #     sender_commit = self.data.commits.get(sp.sender, None)
    #     sp.if ~ sender_commit:
    #         sp.failwith("You have not made a commitment to hash against yet.")
    #     reveal = sp.record(hashable = params.hashable, message = params.message(sp.unit))
    #     sp.transfer(-42, sp.mutez(0), sp.contract(sp.TUnit, sp.address("tz1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"), reveal).open_some())
    #     self.data.unused = False
@sp.add_test(name="hasklock_test")
def test():
    alice = sp.test_account("Alice")
    scenario = sp.test_scenario()
    hashlock = Hashlock(hashed = "0x1234")
    scenario += hashlock
    hashlock.commit("0xf5d3cec5da988edfbee8be85b4919bc7c5a3f7ecebe7a19ac8e0c3f9c3aac5948de9b9dddab88b93c4fee4d094a3a5e48494c0ae80b4ffbcd9a8b7a2c9f3dfc0e2e18082f3d3ceabf9f1a7c8fcd4dec7b7e091a89e83f8a6ab90dea1bdbd95bff9ed8ac89c88ebeecfe5faaeb8f184e5df9298e5aff3bad5bbc1fcefdbb5b2929df9c6ced9aebefbc49decb4d9e085b1a8c39099818d97e0b3dbf287efb99c87c8eeb38f86d9e9c2bdeccec4abb5ce89bce988aba5a0adf59180898697a7e5d1dfa8d5a6aac8f0f5bd87ecb7aeaedec6a4f7f5bfead9e1cbd3a8a88fddcb939198f0ae94cecdc3e9d3d9c2b28ece8ff487a0e983868ef995b3ee90f082adf8aeddbab2efc2b5fcd5aff1a19bb3acff83b08986d0ffa3eec4afabbec280f4d498b1f2e6de01c192a381d3b8c19dd8edb4d6e689cbccb1b5c396c7abda9bc4ed9edf9ecff7c78bab8fadbbd4f4e7d1d289eace839becdfa5e7d1ddc2b0e9e1e88d87a3e3aae8c6dd889cd980e69af8b992d4b5e28cb691de94c0afe0f3fbde8b85e4eced9ec8dcd986d189e4a8bcd3fda2efbce5cde9d68499eef7bda5a782c3adf0cc84abd0c0ec91988b9a81ad819af19e97eefacea9a9b1ffe2d1bcc1e5d8dc87e89d8a92afd3fcf4d4d2e1d9e4f583c5a583ebb6f19dd7abd3f8f5d6a8ee9bf78faa8aedf0d8b0e6a1a6bf95849192b5f8bfef9581deaebef3e6f390ac99ade490e7feb5d0d589cce2e3d4b9ced493e3fac1da83f697e6c0e68f8295ec97f2c0aae7dcaffaedb5fef283d4a5b4f3fdd8e7a0b0f9c4accce9c2f9e9ba8b8391fad3d0db84cbe9f3d003"
        ).run(sender = alice)
    # hashlock.reveal(hashable="da_hashable", message="This is a not so smart contract")
