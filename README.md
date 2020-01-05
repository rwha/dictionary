This uses the 1913 edition of Webster's Unabridged Dictionary from Project Gutenburg

[https://www.gutenberg.org/ebooks/29765](https://www.gutenberg.org/ebooks/29765)

Running `parser.py` will load the file into memory and open port 1913 on localhost so you
can curl for a definition; e.g.:

```console
me@here ~ $ curl localhost:1913/abracadabra
Ab`ra*ca*dab"ra, n. Etym: [L. Of unknown origin.]

Defn: A mystical word or collocation of letters written as in the
figure. Worn on an amulet it was supposed to ward off fever. At
present the word is used chiefly in jest to denote something without
meaning; jargon.
me@here ~ $
```

No frameworks are used and no safegaurds are in place, so as stated in the
[Python documentation](https://docs.python.org/3/library/http.server.html):

__This is not recommended for production__

However, I find it useful to run as a systemd user mode service. It uses
less than 100MB of memory and could probably use less if needed. I use
it with a bash function:

```bash
# in ~/.bashrc

function define() {
    local word=$1
    curl -s "localhost:1913/$word"
}
```

```console
me@here ~ $ define light
Light, n. Etym: [OE.light, liht, AS. leót; akin to OS. lioht, D. & G.
licht, OHG. lioht, Goth. liuhap, Icel. lj, L. lux light, lucere to
shine, Gr. ruc to shine. Lucid, Lunar, Luminous, Lynx.]

1. That agent, force, or action in nature by the operation of which
upon the organs of sight, objects are rendered visible or luminous.

Note: Light was regarded formerly as consisting of material
particles, or corpuscules, sent off in all directions from luminous
bodies, and traversing space, in right lines, with the known velocity
of about 186,300 miles per second; but it is now generally understood
to consist, not in any actual transmission of particles or substance,
but in the propagation of vibrations or undulations in a subtile,
elastic medium, or ether, assumed to pervade all space, and to be
thus set in vibratory motion by the action of luminous bodies, as the
atmosphere is by sonorous bodies. This view of the nature of light is
known as the undulatory or wave theory; the other, advocated by
Newton (but long since abandoned), as the corpuscular, emission, or
Newtonian theory. A more recent theory makes light to consist in
electrical oscillations, and is known as the electro-magnetic theory
of light.

2. That which furnishes, or is a source of, light, as the sun, a
...
```

heh... ether.
