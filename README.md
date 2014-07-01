atlas_tools
===========

This repository  provides a collection of command line tools for the RIPE Atlas
network.  In particular, the tools allow you to:

1. Create measurements.
2. Parse JSON-formatted measurement results (experimental)
3. Select Atlas probes based on their area.

Most of the tools are work-in-progress, so don't expect too much.

Creating measurements
---------------------

Here's an example showing how you can fire off measurements from the command
line.  You will need an API key (denoted as `API_KEY`).

    $ ./create_measurement.py -o dns -u www.example.org CA 1 API_KEY

This will create a one-off DNS measurement using the probe's resolver.  The
measurement will attempt to resolve www.example.org on a randomly chosen probe
in Canada.

Parse JSON-formatted measurement results
----------------------------------------

Note that this tool is incomplete and experimental and you are better off using
[`RIPE Atlas Sagan`](https://github.com/RIPE-NCC/ripe.atlas.sagan).
Nevertheless, here's how you would do it:

    $ ./parser.py MEASUREMENT.JSON

The tool is meant to provide line-based results which can be piped into tools
such as `grep`.

Select Atlas probes based on their area
---------------------------------------

The distribution of Atlas probes is not uniform and several autonomous systems
(AS) contain a large fraction of all Atlas probes.  The tool
`probe_selector.py` will randomly sample probes from the given 2-letter country
code (or `WW` for world wide).  The sampling is done on the AS level which
means that there will be a maximum of one probe for each AS.  The output is a
list of probe IDs.

Here's how you can select 10 random probes in 10 distinct ASes in Italy:

    $ ./probe_selector.py IT 10

Alternatives
============

Don't like `atlas_tools`?  Luckily, there are a bunch of great alternatives
such as [`RIPE Atlas Sagan`](https://github.com/RIPE-NCC/ripe.atlas.sagan) for
parsing results and
[`ripe-atlas-community-contrib`](https://github.com/RIPE-Atlas-Community/ripe-atlas-community-contrib)
which provides various small tools.

Contact
=======

Contact: Philipp Winter <phw@nymity.ch>  
OpenPGP fingerprint: `B369 E7A2 18FE CEAD EB96  8C73 CF70 89E3 D7FD C0D0`
