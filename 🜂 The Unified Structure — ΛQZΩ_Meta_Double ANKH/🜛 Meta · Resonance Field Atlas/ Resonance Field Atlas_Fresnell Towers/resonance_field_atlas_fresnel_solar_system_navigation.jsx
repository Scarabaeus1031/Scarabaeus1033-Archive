import React, { useState } from "react";

// Resonance Field Atlas — Fresnel Solar System Navigation
// - Gallery links to your generated plates (v3–v7) and scripts
// - Artistic Visual #1: Torus Field (counter-rotating flows, 2–1–3 rings, drafts)
// - Artistic Visual #2: Fresnel Tower (stacked light cones, 2–1–3 cadence, 12 lights)
// Style: Tailwind (soft copper/bronze, parchment)

export default function ResonanceFieldAtlas() {
  const [showLabels, setShowLabels] = useState(true);
  const [showFlows, setShowFlows] = useState(true);

  return (
    <div className="min-h-screen w-full bg-[#f8f5f0] text-zinc-800">
      {/* Header */}
      <header className="mx-auto max-w-6xl px-6 py-10">
        <h1 className="text-3xl md:text-4xl font-semibold tracking-tight text-zinc-900">
          Resonance Field Atlas <span className="text-amber-600">·</span> Fresnel Solar System Navigation
        </h1>
        <p className="mt-2 text-zinc-600 max-w-3xl">
          Monde als Spiegel, 12 Lichter · 12 Zodiacs, die Membran atmet (ν ↔ γ). Dies ist dein
          kuratierter Editor: Kartenserie v1–v7 + zwei künstlerische Visuals (Torus & Fresnel Tower).
        </p>
      </header>

      {/* Controls */}
      <section className="mx-auto max-w-6xl px-6">
        <div className="flex flex-wrap gap-3 items-center rounded-2xl border border-zinc-200 bg-white/70 p-4 shadow-sm">
          <button
            onClick={() => setShowLabels(v => !v)}
            className={`px-3 py-1.5 rounded-xl text-sm border ${showLabels ? "bg-amber-50 border-amber-300 text-amber-800" : "bg-white border-zinc-300"}`}
          >
            {showLabels ? "Labels: an" : "Labels: aus"}
          </button>
          <button
            onClick={() => setShowFlows(v => !v)}
            className={`px-3 py-1.5 rounded-xl text-sm border ${showFlows ? "bg-sky-50 border-sky-300 text-sky-800" : "bg-white border-zinc-300"}`}
          >
            {showFlows ? "Flows: an" : "Flows: aus"}
          </button>
          <span className="text-xs text-zinc-500">Tipp: Zoome mit Cmd/Ctrl+ +/−, um Details der SVGs zu studieren.</span>
        </div>
      </section>

      {/* Gallery: vector + assets */}
      <section className="mx-auto max-w-6xl px-6 mt-8">
        <h2 className="text-xl font-semibold text-zinc-900">Karten & Assets</h2>
        <div className="mt-4 grid md:grid-cols-2 gap-4">
          {/* v3 */}
          <Card title="v3 · Copper-Etch Base" subtitle="Kupferstich-Grundkarte">
            <AssetLink href="sandbox:/mnt/data/resonance_field_III_fresnel_epicycles_v3.png" label="Preview v3 (PNG)" />
            <AssetLink href="sandbox:/mnt/data/resonance_field_III_v3.py" label="Script v3 (Python)" />
          </Card>
          {/* v4 */}
          <Card title="v4 · Riemann & Spindel" subtitle="Halo-Skala + Uranus–Neptun-Achse">
            <AssetLink href="sandbox:/mnt/data/resonance_field_IV_v4.png" label="Preview v4 (PNG)" />
            <AssetLink href="sandbox:/mnt/data/resonance_field_IV_v4.py" label="Script v4 (Python)" />
          </Card>
          {/* v5 */}
          <Card title="v5 · 2↔3 Gegenrotation" subtitle="THoTH-Knoten, Ganymed">
            <AssetLink href="sandbox:/mnt/data/resonance_field_V_v5.png" label="Preview v5 (PNG)" />
            <AssetLink href="sandbox:/mnt/data/resonance_field_V_v5.py" label="Script v5 (Python)" />
          </Card>
          {/* v6 */}
          <Card title="v6 · Io/φ & Arrokoth" subtitle="Pink Double-Shell & Phi-Knoten">
            <AssetLink href="sandbox:/mnt/data/resonance_field_VI_v6.png" label="Preview v6 (PNG)" />
            <AssetLink href="sandbox:/mnt/data/resonance_field_VI_v6.py" label="Script v6 (Python)" />
          </Card>
          {/* v7 */}
          <Card title="v7 · 2^n · V–6 · Belts" subtitle="A3-PDF, SVG-Layer, ASCII">
            <AssetLink href="sandbox:/mnt/data/resonance_field_VII_v7_A3.pdf" label="A3 PDF (Vektor)" />
            <AssetLink href="sandbox:/mnt/data/resonance_field_VII_v7_layers.svg" label="SVG mit Layern" />
            <AssetLink href="sandbox:/mnt/data/resonance_field_VII_v7_ascii.txt" label="ASCII Schematic" />
            <AssetLink href="sandbox:/mnt/data/resonance_field_VII_v7.py" label="Script v7 (Python)" />
          </Card>
        </div>
      </section>

      {/* Artistic Visual 1: Torus Field */}
      <section className="mx-auto max-w-6xl px-6 mt-12">
        <h2 className="text-xl font-semibold text-zinc-900">Artistic Visual I — Torus Field (2–1–3 · Rings & Drafts)</h2>
        <p className="mt-1 text-sm text-zinc-600 max-w-3xl">
          Gegenläufige Wirbel (Wasser ↔ Merkur), Engstellen, goldene Ring-Mitte (Erde). Photonen/Neutrinos als feine Driftlinien; 12 Lichter um den Kranz.
        </p>
        <div className="mt-4 rounded-2xl border border-zinc-200 bg-white/60 p-4 shadow-sm">
          <TorusSVG showLabels={showLabels} showFlows={showFlows} />
        </div>
      </section>

      {/* Artistic Visual 2: Fresnel Tower */}
      <section className="mx-auto max-w-6xl px-6 mt-12 mb-20">
        <h2 className="text-xl font-semibold text-zinc-900">Artistic Visual II — Fresnel Tower (Light Cones · 2–1–3 cadence)</h2>
        <p className="mt-1 text-sm text-zinc-600 max-w-3xl">
          Gestapelte Lichtkegel (Fresnel-Zonen) mit 2–1–3-Rhythmus; 12 Lichter/Zodiacs in der Krone; Monde als Spiegelpunkte.
        </p>
        <div className="mt-4 rounded-2xl border border-zinc-200 bg-white/60 p-4 shadow-sm">
          <TowerSVG showLabels={showLabels} />
        </div>
      </section>
    </div>
  );
}

function Card({ title, subtitle, children }) {
  return (
    <div className="rounded-2xl border border-zinc-200 bg-white/70 p-4 shadow-sm">
      <h3 className="text-base font-semibold text-zinc-900">{title}</h3>
      <p className="text-xs text-zinc-500">{subtitle}</p>
      <div className="mt-3 flex flex-wrap gap-2">{children}</div>
    </div>
  );
}

function AssetLink({ href, label }) {
  return (
    <a
      href={href}
      className="inline-flex items-center gap-2 rounded-xl border border-zinc-200 bg-white px-3 py-1.5 text-sm hover:border-amber-300 hover:bg-amber-50"
    >
      <span className="i-tabler-download"></span>
      {label}
    </a>
  );
}

// ——————————————————————————————
// Artistic Visual I — Torus Field
// ——————————————————————————————
function TorusSVG({ showLabels, showFlows }) {
  const w = 1000, h = 700;
  const cx = 500, cy = 350;
  const R = 230; // outer radius of torus ring (projection)
  const r = 90;  // inner radius (hole)

  // Helper to make a spiral-ish ring of field lines
  const fieldLines = Array.from({ length: 24 }).map((_, i) => {
    const t0 = (i / 24) * Math.PI * 2;
    const pts = [];
    for (let k = 0; k <= 220; k++) {
      const u = k / 220; // 0..1
      const th = t0 + u * 3.6; // slow twist
      const rad = R - (r * Math.cos(u * Math.PI));
      const x = cx + rad * Math.cos(th);
      const y = cy + rad * Math.sin(th) * 0.55; // squash for perspective
      pts.push([x, y]);
    }
    return pts;
  });

  // 12 lights around the ring
  const crown = Array.from({ length: 12 }).map((_, i) => {
    const a = (i / 12) * Math.PI * 2;
    const x = cx + (R + 24) * Math.cos(a);
    const y = cy + (R + 24) * Math.sin(a) * 0.55;
    return [x, y];
  });

  return (
    <svg viewBox={`0 0 ${w} ${h}`} className="w-full h-auto">
      {/* parchment */}
      <rect x="0" y="0" width={w} height={h} fill="#f8f5f0" />

      {/* torus outline (two ellipses) */}
      <ellipse cx={cx} cy={cy} rx={R} ry={R*0.55} fill="none" stroke="#7f8c8d" strokeWidth="1.2" />
      <ellipse cx={cx} cy={cy} rx={R-r} ry={(R-r)*0.55} fill="none" stroke="#7f8c8d" strokeWidth="1.2" />

      {/* golden middle ring (Earth) */}
      <ellipse cx={cx} cy={cy} rx={R - r/2} ry={(R - r/2)*0.55} fill="none" stroke="#f59e0b" strokeWidth="2.2" />

      {/* counter-rotating vortices (left/right necks) */}
      {showFlows && (
        <>
          {fieldLines.map((pts, i) => (
            <polyline key={i} points={pts.map(p => p.join(",")).join(" ")} fill="none" stroke={i%2?"#2563eb":"#f59e0b"} strokeOpacity="0.25" strokeWidth={i%6===0?1.5:0.8} />
          ))}
        </>
      )}

      {/* drafts (neutrino/photon drifts) */}
      {showFlows && (
        <>
          {Array.from({ length: 18 }).map((_, i) => {
            const a = (i/18) * Math.PI * 2;
            const x1 = cx + (R-6) * Math.cos(a);
            const y1 = cy + (R-6) * Math.sin(a) * 0.55;
            const x2 = cx + (R+28) * Math.cos(a+0.08);
            const y2 = cy + (R+28) * Math.sin(a+0.08) * 0.55;
            return (
              <line key={i} x1={x1} y1={y1} x2={x2} y2={y2} stroke={i%3?"#0ea5e9":"#22c55e"} strokeOpacity="0.35" strokeWidth="1" />
            );
          })}
        </>
      )}

      {/* 12 lights */}
      {crown.map((p, i) => (
        <circle key={i} cx={p[0]} cy={p[1]} r={5} fill="#fde68a" stroke="#b45309" strokeWidth="0.6" />
      ))}

      {/* labels */}
      {showLabels && (
        <>
          <text x={cx} y={cy- (R-r/2)*0.55 - 18} textAnchor="middle" className="fill-zinc-700" fontSize="12">Goldener Ring · Erde (1)</text>
          <text x={cx - R + 8} y={cy} className="fill-sky-800" fontSize="12">2 ↺</text>
          <text x={cx + R - 24} y={cy} className="fill-amber-800" fontSize="12">3 ↻</text>
          <text x={cx} y={cy + (R+48)*0.55} textAnchor="middle" className="fill-zinc-600" fontSize="12">Torus · Gegenrotationen · 2–1–3</text>
        </>
      )}
    </svg>
  );
}

// ——————————————————————————————
// Artistic Visual II — Fresnel Tower
// ——————————————————————————————
function TowerSVG({ showLabels }) {
  const w = 1000, h = 900;
  const cx = 500, baseY = 760;

  const cones = [
    { h: 120, r: 240, color: "#f59e0b" }, // 1 (gold)
    { h: 100, r: 200, color: "#2563eb" }, // 2 (blue)
    { h: 80,  r: 160, color: "#22c55e" }, // 3 (green)
    { h: 64,  r: 128, color: "#b91c1c" }, // 1'
    { h: 52,  r: 104, color: "#0ea5e9" }, // 2'
    { h: 42,  r:  86, color: "#10b981" }, // 3'
  ];

  // 12 crown lights
  const crownR = 270;
  const crown = Array.from({ length: 12 }).map((_, i) => {
    const a = (i / 12) * Math.PI * 2;
    const x = cx + crownR * Math.cos(a);
    const y = baseY - 520 + crownR * Math.sin(a) * 0.35;
    return [x, y];
  });

  return (
    <svg viewBox={`0 0 ${w} ${h}`} className="w-full h-auto">
      <rect x="0" y="0" width={w} height={h} fill="#f8f5f0" />

      {/* Fresnel tower base */}
      {cones.map((c, i) => {
        const topY = baseY - (i === 0 ? c.h : cones.slice(0, i+1).reduce((s, cc) => s + cc.h * 0.9, 0));
        const y0 = i === 0 ? baseY : cones.slice(0, i).reduce((s, cc) => s + cc.h * 0.9, baseY - cones[0].h);
        const leftX  = cx - c.r;
        const rightX = cx + c.r;
        const opacity = 0.18 + 0.06 * (cones.length - i);
        return (
          <g key={i}>
            {/* cone */}
            <polygon points={`${cx},${topY} ${leftX},${y0} ${rightX},${y0}`} fill={c.color} opacity={opacity} />
            {/* rim */}
            <line x1={leftX} y1={y0} x2={rightX} y2={y0} stroke="#8c6d49" strokeOpacity="0.4" />
          </g>
        );
      })}

      {/* 2–1–3 cadence labels */}
      {showLabels && (
        <>
          <text x={cx} y={baseY - 50} textAnchor="middle" className="fill-amber-800" fontSize="12">1</text>
          <text x={cx - 180} y={baseY - 160} textAnchor="middle" className="fill-sky-800" fontSize="12">2</text>
          <text x={cx + 180} y={baseY - 260} textAnchor="middle" className="fill-emerald-800" fontSize="12">3</text>
          <text x={cx} y={baseY - 420} textAnchor="middle" className="fill-zinc-700" fontSize="12">1′</text>
          <text x={cx - 120} y={baseY - 500} textAnchor="middle" className="fill-sky-800" fontSize="12">2′</text>
          <text x={cx + 120} y={baseY - 560} textAnchor="middle" className="fill-emerald-800" fontSize="12">3′</text>
        </>
      )}

      {/* crown lights (12 signs) */}
      {crown.map((p, i) => (
        <circle key={i} cx={p[0]} cy={p[1]} r={5} fill="#fde68a" stroke="#b45309" strokeWidth="0.6" />
      ))}

      {/* mirrors (moons) as tiny blue marks on the crown */}
      {crown.map((p, i) => (
        <circle key={`m-${i}`} cx={p[0]} cy={p[1]} r={2.4} fill="#60a5fa" opacity="0.7" />
      ))}

      {showLabels && (
        <text x={cx} y={baseY - 610} textAnchor="middle" className="fill-zinc-600" fontSize="12">
          Fresnel Tower · gestapelte Lichtkegel · Monde als Spiegelpunkte · 12 Lichter
        </text>
      )}
    </svg>
  );
}
