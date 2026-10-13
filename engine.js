(function (root) {
  "use strict";
  var TUBE_M = 1;      // labeled foam tube length, m
  var TAPE_W_M = 7;    // labeled heat-tape watts per meter
  var DRIP_L_H = 0.18; // labeled drip rate per faucet, liters per hour

  function round1(x) { return Math.round(x * 10) / 10; }
  function plural(n, word, form) { return n + " " + (n === 1 ? word : (form || word + "s")); }

  function wrapPlan(lengthM) {
    if (!(lengthM > 0)) return { error: "the length must be positive" };
    var tubes = Math.ceil(lengthM / TUBE_M);
    var verdict;
    if (lengthM <= 2) verdict = "a faucet-sock job";
    else if (lengthM <= 10) verdict = "a crawlspace afternoon";
    else verdict = "a whole-house wrap";
    return { tubes: tubes, verdict: verdict };
  }

  function tapePlan(lengthM) {
    if (!(lengthM > 0)) return { error: "the length must be positive" };
    var watts = round1(lengthM * TAPE_W_M);
    var verdict;
    if (lengthM <= 5) verdict = "a faucet run";
    else if (lengthM <= 20) verdict = "a wall run";
    else verdict = "a perimeter run";
    return { watts: watts, verdict: verdict };
  }

  function dripPlan(faucets, hours) {
    if (!(faucets > 0) || !(hours > 0)) return { error: "the faucets and the hours must be positive" };
    var liters = round1(faucets * hours * DRIP_L_H);
    var verdict;
    if (liters <= 2) verdict = "a kettle's worth";
    else if (liters <= 10) verdict = "a bucket's worth";
    else verdict = "a tub's worth";
    return { liters: liters, verdict: verdict };
  }

  function renderWrap(r, lengthM) {
    return "Your " + lengthM + " m of pipe at a labeled " + TUBE_M + " m a tube asks "
      + plural(r.tubes, "tube") + " of foam - " + r.verdict + ".";
  }

  function renderTape(r, lengthM) {
    return "Your " + lengthM + " m of pipe at a labeled " + TAPE_W_M + " W per meter draws "
      + r.watts + " W of heat tape - " + r.verdict + ".";
  }

  function renderDrip(r, faucets, hours) {
    return "Your " + plural(faucets, "faucet") + " dripping over " + hours + " hours at a labeled "
      + DRIP_L_H + " L an hour each " + (faucets === 1 ? "lets" : "let") + " " + r.liters + " L through - " + r.verdict + ".";
  }

  var api = { wrapPlan: wrapPlan, tapePlan: tapePlan, dripPlan: dripPlan, renderWrap: renderWrap, renderTape: renderTape, renderDrip: renderDrip };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.PipeWrapMath = api;
})(this);
