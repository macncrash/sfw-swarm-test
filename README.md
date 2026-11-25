# sfw-swarm-test

A small text toolkit, built by several agents at once to try
[sfw](https://github.com/macncrash/sfw)'s shared-work flow: a coordination issue,
claims, findings, a branch and pull request per item, and a merge round.

Work is split in issue #1. Claim an item before starting (`claiming: ID`), post what
others should know (`finding: ...`), and name the item in your pull request.

Run the tests with `python3 -m unittest -v` (standard library only).
