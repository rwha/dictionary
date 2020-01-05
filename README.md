This uses the 1913 edition of Webster's Unabridged Dictionary from Project Gutenburg

[https://www.gutenberg.org/ebooks/29765](https://www.gutenberg.org/ebooks/29765)

Running `parser.py` will load the file into memory and open port 1913 on localhost so you
can curl for a definition; e.g.:

```console
$ curl localhost:1913/allegiance
Al*le"giance, n. Etym: [OE. alegeaunce; pref. a- + OF. lige, liege.
The meaning was influenced by L. ligare to bind, and even by lex,
legis, law. See Liege, Ligeance.]

1. The tie or obligation, implied or expressed, which a subject owes
to his sovereign or government; the duty of fidelity to one's king,
government, or state.

2. Devotion; loyalty; as, allegiance to science.

Syn.
-- Loyalty; fealty.
-- Allegiance, Loyalty. These words agree in expressing the general
idea of fidelity and attachment to the "powers that be." Allegiance
is an obligation to a ruling power. Loyalty is a feeling or sentiment
towards such power. Allegiance may exist under any form of
government, and, in a republic, we generally speak of allegiance to
the government, to the state, etc. In well conducted monarchies,
loyalty is a warm-hearted feeling of fidelity and obedience to the
sovereign. It is personal in its nature; and hence we speak of the
loyalty of a wife to her husband, not of her allegiance. In cases
where we personify, loyalty is more commonly the word used; as,
loyalty to the constitution; loyalty to the cause of virtue; loyalty
to truth and religion, etc.
Hear me, recreant, on thine allegiance hear me! Shak.
So spake the Seraph Abdiel, faithful found, . . . Unshaken,
unseduced, unterrified, His loyalty he kept, his love, his zeal.
Milton.
$
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
me@here ~ $ define abracadabra
Ab`ra*ca*dab"ra, n. Etym: [L. Of unknown origin.]

Defn: A mystical word or collocation of letters written as in the
figure. Worn on an amulet it was supposed to ward off fever. At
present the word is used chiefly in jest to denote something without
meaning; jargon.
me@here ~ $
```
