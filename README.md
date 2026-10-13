# Pipe wrap math

Pipe freeze protection arithmetic: the freeze names the wrap, the pipe names the tape, and the drip names the liters.

Live at https://ilanis-agent.github.io/pipewrapmath/

## The three tools

- **Wrap plan** - tubes = ceil(exposed pipe / labeled 1 m a tube), with faucet-sock, crawlspace-afternoon and whole-house bands.
- **Tape plan** - watts = pipe length x labeled 7 W per meter, with faucet-run, wall-run and perimeter-run bands.
- **Drip plan** - liters = faucets x hours x labeled 0.18 L an hour, with kettle, bucket and tub bands.

## Formulas and limits

- Watts and liters are rounded to one decimal (round half up), mirroring the oracle float-for-float.
- Every number the app borrows is labeled in the interface: tube length, tape wattage, drip rate.
- Illustrative planning arithmetic only. Real freeze protection is draining the line and shutting the valve - insulation buys time, not immunity - and heat tape follows its manufacturer's instructions exactly. This is not freeze insurance.

## Development

- `engine.js` - calculation and render engine (browser global `PipeWrapMath`, CommonJS for tests).
- `oracle.py` - Python mirror of the engine; regenerates `expected.json`.
- `test.js` - runs every case through the engine and compares fields and render strings: `node test.js`.
