# -*- coding: utf-8 -*-
"""
Generator script for Anatomy 2 (Lower Limb) Comprehensive Revision Guide & Essay Exam Bank
Target file: d:\Coding\PT12\final\anatomy2_lower_limb.html
"""

import sys

html_parts = []

# Part 1: Header, styles, CSS variables, body start
css_and_head = """<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<title>Anatomy 2 (Lower Limb) — Comprehensive Essay & Viva Master Guide</title>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0c10;
    --bg2: #0f1218;
    --bg3: #141820;
    --card: #13171f;
    --card2: #1a1f2a;
    --border: #1e2535;
    --border2: #2a3248;
    --text: #e2e8f0;
    --muted: #8892a4;
    --dim: #4a5568;
    --blue: #3b82f6;
    --blue2: #1d4ed8;
    --cyan: #06b6d4;
    --green: #10b981;
    --yellow: #f59e0b;
    --red: #ef4444;
    --purple: #8b5cf6;
    --pink: #ec4899;
    --orange: #f97316;
    --glow-blue: 0 0 20px rgba(59,130,246,0.25);
    --glow-cyan: 0 0 20px rgba(6,182,212,0.2);
    --glow-green: 0 0 20px rgba(16,185,129,0.2);
    --glow-purple: 0 0 20px rgba(139,92,246,0.2);
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    font-family: 'Cairo', sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    overflow-x: hidden;
  }

  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(59,130,246,0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(59,130,246,0.04) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }

  body::after {
    content: '';
    position: fixed;
    top: -200px;
    left: 50%;
    transform: translateX(-50%);
    width: 800px;
    height: 400px;
    background: radial-gradient(ellipse, rgba(139,92,246,0.08) 0%, rgba(59,130,246,0.05) 40%, transparent 70%);
    pointer-events: none;
    z-index: 0;
  }

  /* === PROGRESS BAR === */
  .progress-bar-container {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 200;
    height: 4px;
    background: var(--bg3);
  }
  .progress-bar-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--blue), var(--cyan), var(--green), var(--purple));
    background-size: 200% 100%;
    animation: gradientShift 3s ease infinite;
    transition: width 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    width: 0%;
    border-radius: 0 2px 2px 0;
  }
  @keyframes gradientShift {
    0%,100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
  }
  .progress-badge {
    position: fixed;
    top: 10px;
    right: 20px;
    z-index: 201;
    background: var(--card);
    border: 1px solid var(--border2);
    border-radius: 20px;
    padding: 5px 14px;
    font-size: 11px;
    font-weight: 700;
    color: var(--cyan);
    font-family: 'JetBrains Mono', monospace;
    backdrop-filter: blur(10px);
    transition: all 0.3s;
    cursor: default;
  }
  .progress-badge:hover { border-color: var(--cyan); }

  /* === BACK BUTTON === */
  .back-btn {
    position: fixed;
    top: 10px;
    left: 20px;
    z-index: 201;
    background: var(--card);
    border: 1px solid var(--border2);
    border-radius: 10px;
    padding: 6px 14px;
    font-size: 13px;
    color: var(--muted);
    text-decoration: none;
    font-family: 'Cairo', sans-serif;
    font-weight: 600;
    transition: all 0.3s;
    display: flex;
    align-items: center;
    gap: 6px;
    backdrop-filter: blur(10px);
  }
  .back-btn:hover { color: var(--text); border-color: var(--blue); background: var(--card2); }

  /* === FLOATING BUTTONS === */
  .fab-group {
    position: fixed;
    bottom: 24px;
    right: 24px;
    z-index: 150;
    display: flex;
    flex-direction: column;
    gap: 10px;
    align-items: flex-end;
  }
  .fab {
    width: 48px;
    height: 48px;
    border-radius: 14px;
    border: 1px solid var(--border2);
    background: var(--card);
    color: var(--muted);
    font-size: 20px;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s;
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
  }
  .fab:hover { color: var(--text); border-color: var(--blue); transform: translateY(-2px); box-shadow: 0 8px 30px rgba(0,0,0,0.4); }
  .fab.active { background: rgba(59,130,246,0.15); border-color: var(--blue); color: var(--blue); }

  header {
    position: relative;
    z-index: 10;
    padding: 60px 0 40px;
    text-align: center;
    border-bottom: 1px solid var(--border);
    background: linear-gradient(180deg, rgba(139,92,246,0.06) 0%, rgba(59,130,246,0.03) 50%, transparent 100%);
  }

  .header-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(139,92,246,0.12);
    border: 1px solid rgba(139,92,246,0.35);
    color: var(--purple);
    padding: 6px 18px;
    border-radius: 100px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 20px;
    animation: fadeDown 0.6s ease both;
  }

  .header-badge::before {
    content: '';
    width: 6px; height: 6px;
    background: var(--purple);
    border-radius: 50%;
    animation: pulse 2s infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.8); }
  }

  h1 {
    font-size: clamp(26px, 5vw, 44px);
    font-weight: 900;
    letter-spacing: -1px;
    line-height: 1.25;
    animation: fadeDown 0.6s 0.1s ease both;
    background: linear-gradient(135deg, #fff 0%, #cbd5e1 50%, var(--cyan) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .subtitle {
    color: var(--muted);
    margin-top: 10px;
    font-size: 14px;
    animation: fadeDown 0.6s 0.2s ease both;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 1px;
  }

  .exam-tags {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 14px;
    flex-wrap: wrap;
  }
  .exam-pill {
    font-size: 11px;
    font-weight: 700;
    padding: 4px 12px;
    border-radius: 20px;
    letter-spacing: 0.5px;
  }
  .pill-oral { background: rgba(59,130,246,0.15); color: #93c5fd; border: 1px solid rgba(59,130,246,0.3); }
  .pill-practical { background: rgba(16,185,129,0.15); color: #6ee7b7; border: 1px solid rgba(16,185,129,0.3); }
  .pill-midterm { background: rgba(245,158,11,0.15); color: #fde68a; border: 1px solid rgba(245,158,11,0.3); }
  .pill-essay { background: rgba(236,72,153,0.15); color: #f472b6; border: 1px solid rgba(236,72,153,0.3); }

  .stats-bar {
    display: flex;
    justify-content: center;
    gap: 36px;
    margin-top: 26px;
    flex-wrap: wrap;
    animation: fadeDown 0.6s 0.3s ease both;
  }

  .stat { text-align: center; }

  .stat-num {
    font-size: 26px;
    font-weight: 900;
    color: var(--cyan);
    font-family: 'JetBrains Mono', monospace;
  }

  .stat-label {
    font-size: 11px;
    color: var(--muted);
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-top: 2px;
  }

  /* NAV */
  .nav {
    position: sticky;
    top: 4px;
    z-index: 100;
    background: rgba(10,12,16,0.96);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border);
    padding: 0 16px;
    display: flex;
    gap: 4px;
    justify-content: center;
    overflow-x: auto;
    scrollbar-width: none;
  }

  .nav::-webkit-scrollbar { display: none; }

  .nav-btn {
    background: none;
    border: none;
    color: var(--muted);
    font-family: 'Cairo', sans-serif;
    font-size: 12px;
    font-weight: 600;
    padding: 13px 12px;
    cursor: pointer;
    white-space: nowrap;
    border-bottom: 2px solid transparent;
    transition: all 0.3s;
    position: relative;
  }

  .nav-btn:hover { color: var(--text); }
  .nav-btn.active {
    color: var(--cyan);
    border-bottom-color: var(--cyan);
    text-shadow: 0 0 20px rgba(6,182,212,0.4);
  }
  .nav-btn.active::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 20%;
    right: 20%;
    height: 2px;
    background: var(--cyan);
    box-shadow: 0 0 10px var(--cyan), 0 0 20px rgba(6,182,212,0.3);
  }

  .nav-btn.special {
    color: #f472b6;
    font-weight: 700;
  }
  .nav-btn.special:hover { color: #fbcfe8; }

  main {
    position: relative;
    z-index: 1;
    max-width: 1120px;
    margin: 0 auto;
    padding: 36px 18px 80px;
  }

  .section { display: none; animation: fadeIn 0.4s ease; }
  .section.active { display: block; }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }

  @keyframes fadeDown {
    from { opacity: 0; transform: translateY(-15px); }
    to { opacity: 1; transform: translateY(0); }
  }

  /* SECTION HEADERS */
  .sec-header {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 24px;
    padding-bottom: 14px;
    border-bottom: 1px solid var(--border);
    position: sticky;
    top: 50px;
    background: var(--bg);
    z-index: 10;
    padding-top: 12px;
    margin-top: -12px;
  }

  .sec-icon {
    width: 42px; height: 42px;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px;
    flex-shrink: 0;
  }

  .ic-blue { background: rgba(59,130,246,0.15); border: 1px solid rgba(59,130,246,0.3); }
  .ic-cyan { background: rgba(6,182,212,0.15); border: 1px solid rgba(6,182,212,0.3); }
  .ic-green { background: rgba(16,185,129,0.15); border: 1px solid rgba(16,185,129,0.3); }
  .ic-yellow { background: rgba(245,158,11,0.15); border: 1px solid rgba(245,158,11,0.3); }
  .ic-red { background: rgba(239,68,68,0.15); border: 1px solid rgba(239,68,68,0.3); }
  .ic-purple { background: rgba(139,92,246,0.15); border: 1px solid rgba(139,92,246,0.3); }
  .ic-orange { background: rgba(249,115,22,0.15); border: 1px solid rgba(249,115,22,0.3); }
  .ic-pink { background: rgba(236,72,153,0.15); border: 1px solid rgba(236,72,153,0.3); }

  .sec-title {
    font-size: 19px;
    font-weight: 700;
    color: var(--text);
    flex: 1;
    line-height: 1.35;
  }

  /* Section complete button */
  .sec-complete-btn {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 6px 14px;
    font-size: 11px;
    font-weight: 700;
    color: var(--muted);
    cursor: pointer;
    font-family: 'Cairo', sans-serif;
    transition: all 0.3s;
    display: flex;
    align-items: center;
    gap: 6px;
    white-space: nowrap;
    flex-shrink: 0;
  }
  .sec-complete-btn:hover { border-color: var(--green); color: var(--green); }
  .sec-complete-btn.completed {
    background: rgba(16,185,129,0.12);
    border-color: rgba(16,185,129,0.4);
    color: var(--green);
  }

  /* ESSAY QUESTION CARDS (Collapsible / High Quality) */
  .essay-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    margin-bottom: 16px;
    overflow: hidden;
    transition: all 0.3s ease;
  }
  .essay-card:hover {
    border-color: var(--border2);
    box-shadow: 0 6px 24px rgba(0,0,0,0.25);
  }
  .essay-card.open {
    border-color: rgba(59,130,246,0.35);
  }

  .essay-header {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 16px 20px;
    cursor: pointer;
    background: var(--card);
    transition: background 0.2s;
    user-select: none;
  }
  .essay-header:hover {
    background: var(--card2);
  }

  .essay-q-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    color: var(--purple);
    background: rgba(139,92,246,0.12);
    border: 1px solid rgba(139,92,246,0.3);
    border-radius: 6px;
    padding: 3px 8px;
    flex-shrink: 0;
    margin-top: 2px;
  }

  .essay-title {
    font-size: 15px;
    font-weight: 700;
    color: var(--text);
    flex: 1;
    line-height: 1.5;
  }

  .essay-badges {
    display: flex;
    gap: 6px;
    align-items: center;
    flex-shrink: 0;
  }

  .essay-toggle-icon {
    width: 26px;
    height: 26px;
    border-radius: 6px;
    background: var(--bg3);
    border: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--muted);
    font-size: 12px;
    transition: all 0.25s;
  }
  .essay-card.open .essay-toggle-icon {
    background: rgba(59,130,246,0.15);
    border-color: rgba(59,130,246,0.4);
    color: var(--blue);
    transform: rotate(180deg);
  }

  .essay-body {
    display: none;
    padding: 18px 22px 22px;
    border-top: 1px solid var(--border);
    background: rgba(15,18,24,0.6);
  }
  .essay-card.open .essay-body {
    display: block;
    animation: fadeIn 0.3s ease;
  }

  /* CONTENT CARDS */
  .content-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px 22px;
    margin-bottom: 16px;
    transition: all 0.3s ease;
  }

  .content-card:hover {
    border-color: var(--border2);
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.2);
  }

  .subsection-title {
    font-size: 13.5px;
    font-weight: 700;
    color: var(--cyan);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .subsection-title::before {
    content: '';
    width: 3px;
    height: 14px;
    background: var(--cyan);
    border-radius: 2px;
  }

  .info-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  .info-list li {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    font-size: 13.5px;
    color: var(--text);
    line-height: 1.6;
  }

  .info-list li::before {
    content: '▸';
    color: var(--blue);
    flex-shrink: 0;
    margin-top: 1px;
    font-size: 12px;
  }

  .info-list.numbered { counter-reset: item; }
  .info-list.numbered li::before {
    counter-increment: item;
    content: counter(item) '.';
    color: var(--yellow);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    min-width: 18px;
  }

  /* TABLES */
  .data-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    margin-top: 6px;
  }

  .data-table th {
    background: rgba(59,130,246,0.12);
    color: var(--blue);
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-size: 11px;
    padding: 10px 14px;
    text-align: left;
    border-bottom: 1px solid var(--border2);
  }

  .data-table td {
    padding: 11px 14px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
    vertical-align: top;
    line-height: 1.6;
    transition: background 0.2s;
  }

  .data-table tr:last-child td { border-bottom: none; }
  .data-table tr:hover td { background: rgba(59,130,246,0.04); }

  .data-table td:first-child {
    font-weight: 700;
    color: var(--cyan);
  }

  /* COMPARE TABLE */
  .compare-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    margin-top: 8px;
    margin-bottom: 8px;
  }

  .compare-table th {
    padding: 12px 14px;
    font-weight: 700;
    font-size: 12.5px;
    text-align: center;
  }

  .compare-table th:first-child { text-align: left; color: var(--muted); font-size: 11px; text-transform: uppercase; }
  .compare-table th:nth-child(2) { color: var(--blue); background: rgba(59,130,246,0.08); border-bottom: 2px solid var(--blue); }
  .compare-table th:nth-child(3) { color: var(--green); background: rgba(16,185,129,0.08); border-bottom: 2px solid var(--green); }
  .compare-table th:nth-child(4) { color: var(--purple); background: rgba(139,92,246,0.08); border-bottom: 2px solid var(--purple); }

  .compare-table td {
    padding: 10px 14px;
    border-bottom: 1px solid var(--border);
    vertical-align: top;
    line-height: 1.6;
    font-size: 13px;
    transition: background 0.2s;
  }

  .compare-table td:first-child {
    font-weight: 700;
    color: var(--yellow);
    font-size: 12px;
  }

  .compare-table td:nth-child(2) { background: rgba(59,130,246,0.03); }
  .compare-table td:nth-child(3) { background: rgba(16,185,129,0.03); }
  .compare-table td:nth-child(4) { background: rgba(139,92,246,0.03); }

  .compare-table tr:last-child td { border-bottom: none; }
  .compare-table tr:hover td { filter: brightness(1.15); }

  /* HIGHLIGHT BOXES */
  .highlight-box {
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 12px;
    font-size: 13px;
    line-height: 1.7;
    transition: transform 0.2s;
  }
  .highlight-box:hover { transform: translateX(4px); }

  .highlight-box.blue {
    background: rgba(59,130,246,0.08);
    border: 1px solid rgba(59,130,246,0.25);
    border-left: 3px solid var(--blue);
  }

  .highlight-box.cyan {
    background: rgba(6,182,212,0.08);
    border: 1px solid rgba(6,182,212,0.25);
    border-left: 3px solid var(--cyan);
  }

  .highlight-box.green {
    background: rgba(16,185,129,0.08);
    border: 1px solid rgba(16,185,129,0.25);
    border-left: 3px solid var(--green);
  }

  .highlight-box.yellow {
    background: rgba(245,158,11,0.08);
    border: 1px solid rgba(245,158,11,0.25);
    border-left: 3px solid var(--yellow);
  }

  .highlight-box.purple {
    background: rgba(139,92,246,0.08);
    border: 1px solid rgba(139,92,246,0.25);
    border-left: 3px solid var(--purple);
  }

  .highlight-box.red {
    background: rgba(239,68,68,0.08);
    border: 1px solid rgba(239,68,68,0.25);
    border-left: 3px solid var(--red);
  }

  .hb-title {
    font-weight: 700;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 8px;
  }

  .blue .hb-title { color: var(--blue); }
  .cyan .hb-title { color: var(--cyan); }
  .green .hb-title { color: var(--green); }
  .yellow .hb-title { color: var(--yellow); }
  .purple .hb-title { color: var(--purple); }
  .red .hb-title { color: var(--red); }

  /* GRID LAYOUT */
  .two-col {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 16px;
  }
  .three-col {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 14px;
    margin-bottom: 16px;
  }

  @media (max-width: 768px) {
    .two-col, .three-col { grid-template-columns: 1fr; }
    .compare-table td:first-child { white-space: normal; }
    .data-table td:first-child { white-space: normal; }
  }

  /* TAGS LIST */
  .vein-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 4px;
  }

  .vein-tag {
    background: rgba(239,68,68,0.1);
    border: 1px solid rgba(239,68,68,0.25);
    color: #fca5a5;
    font-size: 12px;
    padding: 4px 12px;
    border-radius: 6px;
    font-weight: 600;
    transition: transform 0.2s;
  }
  .vein-tag:hover { transform: scale(1.05); }

  .artery-tag {
    background: rgba(249,115,22,0.1);
    border: 1px solid rgba(249,115,22,0.25);
    color: #fdba74;
    font-size: 12px;
    padding: 4px 12px;
    border-radius: 6px;
    font-weight: 600;
    transition: transform 0.2s;
  }
  .artery-tag:hover { transform: scale(1.05); }

  .nerve-tag {
    background: rgba(139,92,246,0.1);
    border: 1px solid rgba(139,92,246,0.25);
    color: #c4b5fd;
    font-size: 12px;
    padding: 4px 12px;
    border-radius: 6px;
    font-weight: 600;
    transition: transform 0.2s;
  }
  .nerve-tag:hover { transform: scale(1.05); }

  .tube-tag {
    background: rgba(6,182,212,0.1);
    border: 1px solid rgba(6,182,212,0.25);
    color: #67e8f9;
    font-size: 12px;
    padding: 4px 12px;
    border-radius: 6px;
    font-weight: 600;
    transition: transform 0.2s;
  }
  .tube-tag:hover { transform: scale(1.05); }

  .lymph-tag {
    background: rgba(16,185,129,0.1);
    border: 1px solid rgba(16,185,129,0.25);
    color: #6ee7b7;
    font-size: 12px;
    padding: 4px 12px;
    border-radius: 6px;
    font-weight: 600;
    transition: transform 0.2s;
  }
  .lymph-tag:hover { transform: scale(1.05); }

  /* MUSCLE TABLE */
  .muscle-table { width: 100%; border-collapse: collapse; font-size: 12.5px; margin-top: 6px; }
  .muscle-table th {
    background: rgba(245,158,11,0.1);
    color: var(--yellow);
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 10px 12px;
    border-bottom: 1px solid rgba(245,158,11,0.2);
    text-align: left;
  }
  .muscle-table td {
    padding: 10px 12px;
    border-bottom: 1px solid var(--border);
    vertical-align: top;
    line-height: 1.6;
    color: var(--text);
    transition: background 0.2s;
  }
  .muscle-table tr:last-child td { border-bottom: none; }
  .muscle-table tr:hover td { background: rgba(245,158,11,0.04); }
  .muscle-table td:first-child {
    font-weight: 700;
    color: var(--orange);
    white-space: nowrap;
  }

  /* SEARCH */
  .search-wrap {
    margin-bottom: 24px;
    position: relative;
  }
  .search-input {
    width: 100%;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    color: var(--text);
    font-family: 'Cairo', sans-serif;
    font-size: 14px;
    padding: 12px 16px 12px 44px;
    outline: none;
    transition: all 0.3s;
  }
  .search-input:focus { border-color: var(--cyan); box-shadow: 0 0 0 3px rgba(6,182,212,0.15); }
  .search-input::placeholder { color: var(--dim); }
  .search-icon {
    position: absolute;
    left: 14px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--dim);
    font-size: 16px;
    pointer-events: none;
  }
  .search-results-info {
    margin-top: 8px;
    font-size: 12px;
    color: var(--muted);
    display: none;
  }
  .search-results-info span { color: var(--cyan); font-weight: 700; }

  mark.search-hl {
    background: rgba(6,182,212,0.35);
    color: #fff;
    padding: 1px 4px;
    border-radius: 3px;
    box-shadow: 0 0 8px rgba(6,182,212,0.4);
  }

  /* BADGE */
  .badge {
    display: inline-block;
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 2px 8px;
    border-radius: 4px;
    vertical-align: middle;
  }
  .badge-blue { background: rgba(59,130,246,0.15); color: var(--blue); }
  .badge-yellow { background: rgba(245,158,11,0.15); color: var(--yellow); }
  .badge-red { background: rgba(239,68,68,0.15); color: var(--red); }
  .badge-green { background: rgba(16,185,129,0.15); color: var(--green); }
  .badge-purple { background: rgba(139,92,246,0.15); color: var(--purple); }

  .topic-group { margin-bottom: 36px; }

  /* ARABIC TRANSLATION BUTTON & PANEL */
  .translate-btn {
    background: rgba(16,185,129,0.1);
    border: 1px solid rgba(16,185,129,0.3);
    border-radius: 8px;
    padding: 6px 12px;
    font-size: 13.5px;
    color: var(--green);
    cursor: pointer;
    font-family: 'Cairo', sans-serif;
    font-weight: 600;
    transition: all 0.3s;
    display: flex;
    align-items: center;
    gap: 6px;
    white-space: nowrap;
    flex-shrink: 0;
  }
  .translate-btn:hover {
    background: rgba(16,185,129,0.2);
    border-color: rgba(16,185,129,0.5);
    transform: translateY(-1px);
    box-shadow: 0 4px 15px rgba(16,185,129,0.15);
  }
  .translate-btn.active {
    background: rgba(16,185,129,0.25);
    border-color: var(--green);
    color: #6ee7b7;
    box-shadow: 0 0 12px rgba(16,185,129,0.2);
  }
  .translate-btn .btn-label { font-size: 11px; }

  .arabic-panel {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.5s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.4s ease, padding 0.4s ease;
    opacity: 0;
    background: linear-gradient(135deg, rgba(16,185,129,0.06) 0%, rgba(6,182,212,0.04) 100%);
    border: 1px solid rgba(16,185,129,0.2);
    border-radius: 12px;
    margin-bottom: 16px;
    direction: rtl;
    text-align: right;
    padding: 0 20px;
  }
  .arabic-panel.active {
    max-height: 1200px;
    opacity: 1;
    padding: 20px;
    overflow-y: auto;
  }
  .arabic-panel-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 14px;
    padding-bottom: 10px;
    border-bottom: 1px solid rgba(16,185,129,0.15);
  }
  .arabic-panel-icon { font-size: 20px; }
  .arabic-panel-title {
    font-size: 15px;
    font-weight: 800;
    color: var(--green);
    font-family: 'Cairo', sans-serif;
  }
  .arabic-panel-badge {
    background: rgba(16,185,129,0.15);
    border: 1px solid rgba(16,185,129,0.3);
    color: #6ee7b7;
    font-size: 10px;
    font-weight: 700;
    padding: 2px 10px;
    border-radius: 20px;
    margin-right: auto;
    direction: ltr;
  }
  .arabic-panel p {
    font-size: 13.5px;
    color: #b8c5d4;
    line-height: 2;
    margin-bottom: 10px;
    font-family: 'Cairo', sans-serif;
  }
  .arabic-panel p:last-child { margin-bottom: 0; }
  .arabic-panel strong { color: #6ee7b7; font-weight: 700; }
  .arabic-panel .ar-highlight {
    background: rgba(16,185,129,0.1);
    border-right: 3px solid var(--green);
    padding: 10px 14px;
    border-radius: 0 8px 8px 0;
    margin: 10px 0;
    font-size: 13px;
    color: #a8b8c8;
    line-height: 1.9;
  }

  /* === FLASHCARD MODE === */
  .flashcard-overlay {
    position: fixed;
    inset: 0;
    z-index: 300;
    background: rgba(10,12,16,0.97);
    backdrop-filter: blur(20px);
    display: none;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }
  .flashcard-overlay.active { display: flex; }

  .flashcard-header {
    position: absolute;
    top: 20px;
    left: 0;
    right: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 16px;
  }
  .flashcard-counter {
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    color: var(--muted);
  }
  .flashcard-close {
    position: absolute;
    right: 24px;
    top: 0;
    background: var(--card);
    border: 1px solid var(--border);
    color: var(--muted);
    width: 40px;
    height: 40px;
    border-radius: 10px;
    cursor: pointer;
    font-size: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s;
  }
  .flashcard-close:hover { color: var(--red); border-color: var(--red); }

  .flashcard-scene {
    width: 100%;
    max-width: 580px;
    height: 340px;
    perspective: 1000px;
    cursor: pointer;
  }
  .flashcard-card {
    width: 100%;
    height: 100%;
    position: relative;
    transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    transform-style: preserve-3d;
  }
  .flashcard-card.flipped { transform: rotateY(180deg); }

  .flashcard-face {
    position: absolute;
    inset: 0;
    backface-visibility: hidden;
    border-radius: 16px;
    border: 1px solid var(--border2);
    padding: 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
  }
  .flashcard-front {
    background: linear-gradient(135deg, var(--card) 0%, var(--card2) 100%);
  }
  .flashcard-back {
    background: linear-gradient(135deg, rgba(6,182,212,0.08) 0%, rgba(139,92,246,0.08) 100%);
    border-color: rgba(6,182,212,0.3);
    transform: rotateY(180deg);
  }
  .flashcard-label {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 16px;
    font-weight: 700;
  }
  .flashcard-front .flashcard-label { color: var(--cyan); }
  .flashcard-back .flashcard-label { color: var(--green); }
  .flashcard-text {
    font-size: 17px;
    font-weight: 600;
    line-height: 1.6;
    color: var(--text);
  }
  .flashcard-back .flashcard-text { color: #6ee7b7; font-size: 15px; }
  .flashcard-hint {
    position: absolute;
    bottom: 16px;
    font-size: 11px;
    color: var(--dim);
  }
  .flashcard-section-tag {
    position: absolute;
    top: 16px;
    right: 16px;
    font-size: 10px;
    background: rgba(139,92,246,0.12);
    border: 1px solid rgba(139,92,246,0.3);
    color: var(--purple);
    padding: 3px 10px;
    border-radius: 20px;
    font-weight: 600;
  }

  .flashcard-nav {
    display: flex;
    gap: 16px;
    margin-top: 26px;
  }
  .flashcard-nav button {
    background: var(--card);
    border: 1px solid var(--border);
    color: var(--muted);
    padding: 10px 24px;
    border-radius: 10px;
    cursor: pointer;
    font-family: 'Cairo', sans-serif;
    font-size: 13px;
    font-weight: 600;
    transition: all 0.3s;
  }
  .flashcard-nav button:hover { color: var(--text); border-color: var(--cyan); }

  /* === QUICK REF SIDEBAR === */
  .quickref-overlay {
    position: fixed;
    inset: 0;
    z-index: 250;
    background: rgba(0,0,0,0.5);
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s;
  }
  .quickref-overlay.active { opacity: 1; pointer-events: all; }

  .quickref-sidebar {
    position: fixed;
    top: 0;
    right: -420px;
    bottom: 0;
    width: 400px;
    max-width: 90vw;
    z-index: 251;
    background: var(--bg2);
    border-left: 1px solid var(--border);
    overflow-y: auto;
    transition: right 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    padding: 24px;
  }
  .quickref-sidebar.active { right: 0; }
  .quickref-sidebar::-webkit-scrollbar { width: 4px; }
  .quickref-sidebar::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 4px; }

  .qr-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 22px;
    padding-bottom: 14px;
    border-bottom: 1px solid var(--border);
  }
  .qr-title {
    font-size: 17px;
    font-weight: 800;
    color: var(--text);
  }
  .qr-close {
    background: none;
    border: 1px solid var(--border);
    color: var(--muted);
    width: 32px;
    height: 32px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s;
  }
  .qr-close:hover { color: var(--red); border-color: var(--red); }

  .qr-section { margin-bottom: 18px; }
  .qr-section-title {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 5px 10px;
    border-radius: 6px;
    margin-bottom: 8px;
    display: inline-block;
  }
  .qr-section-title.blue { background: rgba(59,130,246,0.1); color: var(--blue); }
  .qr-section-title.cyan { background: rgba(6,182,212,0.1); color: var(--cyan); }
  .qr-section-title.orange { background: rgba(249,115,22,0.1); color: var(--orange); }
  .qr-section-title.yellow { background: rgba(245,158,11,0.1); color: var(--yellow); }
  .qr-section-title.red { background: rgba(239,68,68,0.1); color: var(--red); }
  .qr-section-title.purple { background: rgba(139,92,246,0.1); color: var(--purple); }
  .qr-section-title.green { background: rgba(16,185,129,0.1); color: var(--green); }

  .qr-items {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 6px;
    padding-left: 6px;
  }
  .qr-items li {
    font-size: 12.5px;
    color: var(--muted);
    line-height: 1.5;
    display: flex;
    align-items: flex-start;
    gap: 8px;
  }
  .qr-items li::before { content: '→'; color: var(--dim); flex-shrink: 0; }

  /* === KEYBOARD SHORTCUTS MODAL === */
  .shortcuts-modal {
    position: fixed;
    inset: 0;
    z-index: 400;
    background: rgba(10,12,16,0.9);
    backdrop-filter: blur(10px);
    display: none;
    align-items: center;
    justify-content: center;
  }
  .shortcuts-modal.active { display: flex; }
  .shortcuts-box {
    background: var(--card);
    border: 1px solid var(--border2);
    border-radius: 16px;
    padding: 30px;
    max-width: 400px;
    width: 90%;
  }
  .shortcuts-box h3 {
    font-size: 18px;
    font-weight: 800;
    color: var(--text);
    margin-bottom: 18px;
    text-align: center;
  }
  .shortcut-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 0;
    border-bottom: 1px solid var(--border);
  }
  .shortcut-row:last-child { border-bottom: none; }
  .shortcut-key {
    background: var(--bg3);
    border: 1px solid var(--border2);
    color: var(--cyan);
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 6px;
  }
  .shortcut-desc { font-size: 13px; color: var(--muted); }

  /* === CONFETTI === */
  .confetti-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 500;
    overflow: hidden;
  }
  .confetti-piece {
    position: absolute;
    width: 8px;
    height: 8px;
    border-radius: 2px;
    animation: confettiFall 1.5s ease-out forwards;
  }
  @keyframes confettiFall {
    0% { transform: translateY(-20px) rotate(0deg) scale(1); opacity: 1; }
    100% { transform: translateY(100vh) rotate(720deg) scale(0); opacity: 0; }
  }

  /* === PRINT === */
  @media print {
    body::before, body::after, .nav, .progress-bar-container, .progress-badge,
    .back-btn, .fab-group, .search-wrap, .sec-complete-btn, .translate-btn,
    .arabic-panel, .essay-toggle-icon,
    .flashcard-overlay, .quickref-overlay, .quickref-sidebar, .shortcuts-modal { display: none !important; }
    .section { display: block !important; page-break-inside: avoid; }
    .essay-card { border-color: #ccc !important; background: #fafafa !important; break-inside: avoid; }
    .essay-body { display: block !important; background: #fff !important; color: #000 !important; }
    body { background: #fff; color: #000; }
    header { background: none; border-bottom: 2px solid #000; }
    h1 { background: none; -webkit-text-fill-color: #000; color: #000; }
    .content-card { border-color: #ccc; background: #fafafa; }
    .highlight-box { border-color: #ccc; background: #f5f5f5; color: #000; }
    .sec-header { position: static; background: #fff; }
    .stat-num { color: #000; }
    .subtitle, .stat-label { color: #666; }
    .header-badge { color: #333; border-color: #ccc; background: #eee; }
    .sec-title { color: #000; }
    .subsection-title { color: #333; }
    .info-list li { color: #000; }
    .data-table th, .muscle-table th, .compare-table th { background: #eee !important; color: #333 !important; }
    .data-table td, .muscle-table td, .compare-table td { color: #000 !important; border-color: #ddd !important; background: transparent !important; }
  }

  /* === RESPONSIVE === */
  @media (max-width: 640px) {
    .stats-bar { gap: 20px; }
    .nav-btn { padding: 11px 8px; font-size: 11px; }
    .back-btn { padding: 4px 10px; font-size: 11px; top: 8px; left: 8px; }
    .progress-badge { top: 8px; right: 8px; font-size: 10px; padding: 4px 10px; }
    header { padding: 50px 14px 26px; }
    .fab-group { bottom: 16px; right: 16px; }
    .fab { width: 42px; height: 42px; font-size: 18px; }
    .sec-header { top: 46px; }
    .flashcard-scene { height: 280px; }
    .flashcard-text { font-size: 14.5px; }
  }
</style>
</head>
<body>

<!-- Progress Bar -->
<div class="progress-bar-container"><div class="progress-bar-fill" id="progressFill"></div></div>
<div class="progress-badge" id="progressBadge">0/9</div>

<!-- Back Button -->
<a href="../index.html" class="back-btn">← الرئيسية</a>

<!-- Floating Action Buttons -->
<div class="fab-group">
  <button class="fab" onclick="toggleShortcuts()" title="اختصارات لوحة المفاتيح (K)">⌨️</button>
  <button class="fab" onclick="toggleQuickRef()" title="مرجع سريع (Q)">📌</button>
  <button class="fab" onclick="window.print()" title="طباعة / تصدير PDF">🖨️</button>
</div>

<header>
  <div class="header-badge">Anatomy 2 — Lower Limb</div>
  <h1>Anatomy 2 (Lower Limb) Notebook</h1>
  <div class="subtitle">Complete Essay Questions, Model Answers & Practical Viva Guide</div>
  <div class="exam-tags">
    <span class="exam-pill pill-essay">📝 100% Essay & Written</span>
    <span class="exam-pill pill-oral">🎤 Oral / Viva High-Yield</span>
    <span class="exam-pill pill-practical">🔬 Practical & OSPE Spotting</span>
    <span class="exam-pill pill-midterm">⚡ Midterm & Final Ready</span>
  </div>
  <div class="stats-bar">
    <div class="stat"><div class="stat-num">9</div><div class="stat-label">Master Topics</div></div>
    <div class="stat"><div class="stat-num">45+</div><div class="stat-label">Essay Questions</div></div>
    <div class="stat"><div class="stat-num">8</div><div class="stat-label">Comparison Tables</div></div>
    <div class="stat"><div class="stat-num">30</div><div class="stat-label">Viva Flashcards</div></div>
    <div class="stat"><div class="stat-num" style="color:var(--green)">100%</div><div class="stat-label">Coverage Guarantee</div></div>
  </div>
</header>

<nav class="nav" id="mainNav">
  <button class="nav-btn active" onclick="showSection('gluteal', this)">🍑 Gluteal Region</button>
  <button class="nav-btn" onclick="showSection('femoral-triangle', this)">📐 Femoral Triangle & Canal</button>
  <button class="nav-btn" onclick="showSection('ant-thigh', this)">🦵 Ant. Thigh & Hunter's</button>
  <button class="nav-btn" onclick="showSection('med-thigh', this)">🧲 Medial Thigh (Adductors)</button>
  <button class="nav-btn" onclick="showSection('post-thigh', this)">🏃 Post. Thigh & Popliteal</button>
  <button class="nav-btn" onclick="showSection('fem-obt-nerves', this)">⚡ Femoral & Obturator N.</button>
  <button class="nav-btn" onclick="showSection('sciatic-nerves', this)">⚡ Sciatic, Tibial & Fibular</button>
  <button class="nav-btn" onclick="showSection('comparisons', this)">📊 Tables & Clinicals</button>
  <button class="nav-btn" onclick="showSection('viva-spotting', this)">🔬 Practical & Spotting</button>
  <button class="nav-btn special" onclick="openFlashcards()">🧠 اختبر نفسك (Flashcards)</button>
</nav>

<main>

<!-- SEARCH -->
<div class="search-wrap">
  <span class="search-icon">🔍</span>
  <input class="search-input" id="searchInput" placeholder="ابحث في جميع أسئلة المقالي والعملي والأعصاب..." oninput="searchAll(this.value)">
  <div class="search-results-info" id="searchInfo">تم العثور على <span id="searchCount">0</span> نتيجة</div>
</div>
"""

print("Constructed base layout. Writing script...")
