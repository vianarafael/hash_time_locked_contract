import smartpy as sp

class Hashlock(sp.Contract):
    def __init__(self, hashed, unused, commits):
        self.init(hashed = hashed, unused = unused, commits = commits)

    @sp.entry_point
    def commit(self, params):
        p = sp.bytes.from_hex(params)
        commit = sp.record(date = sp.timestamp_from_utc_now() + sp.timestamp_from_seconds(86400),
                           salted_hash = p)
        self.data.commits[sp.sender] = commit

    @sp.entry_point
    def reveal(self, params):
        if not self.data.unused:
            sp.failwith("This contract has already been used.")
        sender_commit = self.data.commits.get(sp.sender, None)
        if not sender_commit:
            sp.failwith("You have not made a commitment to hash against yet.")
        reveal = sp.record(hashable = params.hashable, message = params.message(sp.unit))
        sp.transfer(sp.mutez(0), sp.contract(sp.TUnit, sp.address("tz1zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"), reveal).open_some())
        self.data.unused = False
