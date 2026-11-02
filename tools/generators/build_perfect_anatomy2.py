# -*- coding: utf-8 -*-
"""
Perfect Builder for Anatomy 2 (Lower Limb)
Generates clean, non-duplicated, perfectly responsive HTML with stunning Nav Bar with smooth horizontal arrows.
"""

import os
from sec1 import get_section_1
from sec2 import get_section_2
from sec3 import get_section_3
from sec4 import get_section_4
from sec5 import get_section_5
from sec6 import get_section_6
from sec7 import get_section_7
from sec8 import get_section_8
from sec9 import get_section_9

def build_full_html():
    return """<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate, max-age=0, post-check=0, pre-check=0">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<meta http-equiv="Expires" content="Tue, 01 Jan 1980 1:00:00 GMT">
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
    background: radial-gradient(ellipse, rgba(139,92,246,0.08) 0%, rgba(6,182,212,0.05) 40%, transparent 70%);
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
  .back-btn:hover { color: var(--text); border-color: var(--cyan); background: var(--card2); }

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
  .fab:hover { color: var(--text); border-color: var(--cyan); transform: translateY(-2px); box-shadow: 0 8px 30px rgba(0,0,0,0.4); }
  .fab.active { background: rgba(6,182,212,0.15); border-color: var(--cyan); color: var(--cyan); }

  header {
    position: relative;
    z-index: 10;
    padding: 64px 16px 36px;
    text-align: center;
    border-bottom: 1px solid var(--border);
    background: linear-gradient(180deg, rgba(139,92,246,0.08) 0%, rgba(6,182,212,0.03) 60%, transparent 100%);
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
    font-size: clamp(24px, 5vw, 42px);
    font-weight: 900;
    letter-spacing: -0.5px;
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
    letter-spacing: 0.5px;
  }

  .exam-tags {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 16px;
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
    gap: 28px;
    margin-top: 24px;
    flex-wrap: wrap;
    animation: fadeDown 0.6s 0.3s ease both;
  }

  .stat { text-align: center; }

  .stat-num {
    font-size: 24px;
    font-weight: 900;
    color: var(--cyan);
    font-family: 'JetBrains Mono', monospace;
  }

  .stat-label {
    font-size: 10.5px;
    color: var(--muted);
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-top: 2px;
  }

  /* === MODERN ULTRA-SLEEK NAV BAR === */
  .nav-wrapper {
    position: sticky;
    top: 0;
    z-index: 100;
    background: rgba(10, 12, 16, 0.95);
    backdrop-filter: blur(20px) saturate(1.4);
    -webkit-backdrop-filter: blur(20px) saturate(1.4);
    border-bottom: 1px solid var(--border);
    padding: 8px 0;
    box-shadow: 0 4px 20px rgba(0,0,0,0.4);
  }

  .nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 12px;
    display: flex;
    align-items: center;
    gap: 6px;
    position: relative;
  }

  .nav-scroll-btn {
    width: 32px;
    height: 32px;
    border-radius: 8px;
    background: var(--card);
    border: 1px solid var(--border);
    color: var(--muted);
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    font-size: 13px;
    flex-shrink: 0;
    transition: all 0.2s;
  }
  .nav-scroll-btn:hover {
    color: var(--cyan);
    border-color: var(--cyan);
    background: var(--card2);
  }

  .nav-scroll {
    display: flex;
    gap: 8px;
    overflow-x: auto;
    scrollbar-width: thin;
    scrollbar-color: var(--border2) transparent;
    padding: 4px 2px 6px;
    scroll-behavior: smooth;
    width: 100%;
    -webkit-overflow-scrolling: touch;
    align-items: center;
  }

  .nav-scroll::-webkit-scrollbar {
    height: 4px;
  }
  .nav-scroll::-webkit-scrollbar-track {
    background: rgba(255,255,255,0.02);
    border-radius: 4px;
  }
  .nav-scroll::-webkit-scrollbar-thumb {
    background: var(--border2);
    border-radius: 4px;
  }
  .nav-scroll::-webkit-scrollbar-thumb:hover {
    background: var(--cyan);
  }

  .nav-btn {
    background: var(--card);
    border: 1px solid var(--border);
    color: var(--muted);
    font-family: 'Cairo', sans-serif;
    font-size: 12px;
    font-weight: 600;
    padding: 7px 13px;
    border-radius: 10px;
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    display: inline-flex;
    align-items: center;
    gap: 7px;
    flex-shrink: 0;
  }

  .nav-btn .num-badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 700;
    background: var(--bg3);
    border: 1px solid var(--border);
    color: var(--dim);
    padding: 1px 5px;
    border-radius: 4px;
    transition: all 0.25s;
  }

  .nav-btn:hover {
    color: var(--text);
    border-color: rgba(6,182,212,0.4);
    background: rgba(6,182,212,0.06);
    transform: translateY(-1px);
  }

  .nav-btn:hover .num-badge {
    color: var(--cyan);
    border-color: rgba(6,182,212,0.3);
  }

  .nav-btn.active {
    background: linear-gradient(135deg, rgba(6,182,212,0.2) 0%, rgba(59,130,246,0.12) 100%);
    border-color: var(--cyan);
    color: #fff;
    box-shadow: 0 0 14px rgba(6,182,212,0.25);
    font-weight: 700;
  }

  .nav-btn.active .num-badge {
    background: rgba(6,182,212,0.25);
    border-color: var(--cyan);
    color: #67e8f9;
  }

  .nav-btn.special {
    background: linear-gradient(135deg, rgba(236,72,153,0.12) 0%, rgba(139,92,246,0.12) 100%);
    border-color: rgba(236,72,153,0.35);
    color: #f472b6;
    font-weight: 700;
  }
  .nav-btn.special:hover {
    border-color: #ec4899;
    color: #fbcfe8;
    box-shadow: 0 0 14px rgba(236,72,153,0.3);
  }

  main {
    position: relative;
    z-index: 1;
    max-width: 1140px;
    margin: 0 auto;
    padding: 28px 16px 80px;
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
    gap: 12px;
    margin-bottom: 22px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border);
    position: sticky;
    top: 52px;
    background: var(--bg);
    z-index: 10;
    padding-top: 10px;
    margin-top: -10px;
  }

  .sec-icon {
    width: 38px; height: 38px;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px;
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
    font-size: 18px;
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
    padding: 6px 12px;
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

  /* ESSAY QUESTION CARDS */
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
    padding: 16px 18px;
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
    font-size: 14.5px;
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
    width: 24px;
    height: 24px;
    border-radius: 6px;
    background: var(--bg3);
    border: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--muted);
    font-size: 11px;
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
    padding: 16px 20px 20px;
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
    padding: 18px 20px;
    margin-bottom: 14px;
    transition: all 0.3s ease;
  }

  .content-card:hover {
    border-color: var(--border2);
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.2);
  }

  .subsection-title {
    font-size: 13px;
    font-weight: 700;
    color: var(--cyan);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .subsection-title::before {
    content: '';
    width: 3px;
    height: 13px;
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
    font-size: 13px;
    color: var(--text);
    line-height: 1.6;
  }

  .info-list li::before {
    content: '▸';
    color: var(--blue);
    flex-shrink: 0;
    margin-top: 1px;
    font-size: 11px;
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
    font-size: 12.5px;
    margin-top: 6px;
  }

  .data-table th {
    background: rgba(59,130,246,0.12);
    color: var(--blue);
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-size: 11px;
    padding: 9px 12px;
    text-align: left;
    border-bottom: 1px solid var(--border2);
  }

  .data-table td {
    padding: 10px 12px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
    vertical-align: top;
    line-height: 1.55;
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
    font-size: 12.5px;
    margin-top: 6px;
    margin-bottom: 6px;
  }

  .compare-table th {
    padding: 10px 12px;
    font-weight: 700;
    font-size: 12px;
    text-align: center;
  }

  .compare-table th:first-child { text-align: left; color: var(--muted); font-size: 10.5px; text-transform: uppercase; }
  .compare-table th:nth-child(2) { color: var(--blue); background: rgba(59,130,246,0.08); border-bottom: 2px solid var(--blue); }
  .compare-table th:nth-child(3) { color: var(--green); background: rgba(16,185,129,0.08); border-bottom: 2px solid var(--green); }
  .compare-table th:nth-child(4) { color: var(--purple); background: rgba(139,92,246,0.08); border-bottom: 2px solid var(--purple); }

  .compare-table td {
    padding: 9px 12px;
    border-bottom: 1px solid var(--border);
    vertical-align: top;
    line-height: 1.55;
    font-size: 12.5px;
    transition: background 0.2s;
  }

  .compare-table td:first-child {
    font-weight: 700;
    color: var(--yellow);
    font-size: 11.5px;
  }

  .compare-table td:nth-child(2) { background: rgba(59,130,246,0.03); }
  .compare-table td:nth-child(3) { background: rgba(16,185,129,0.03); }
  .compare-table td:nth-child(4) { background: rgba(139,92,246,0.03); }

  .compare-table tr:last-child td { border-bottom: none; }
  .compare-table tr:hover td { filter: brightness(1.15); }

  /* HIGHLIGHT BOXES */
  .highlight-box {
    border-radius: 8px;
    padding: 12px 16px;
    margin-bottom: 10px;
    font-size: 12.5px;
    line-height: 1.65;
    transition: transform 0.2s;
  }
  .highlight-box:hover { transform: translateX(3px); }

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
    font-size: 11.5px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
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
    gap: 14px;
    margin-bottom: 14px;
  }

  @media (max-width: 768px) {
    .two-col { grid-template-columns: 1fr; }
    .compare-table td:first-child { white-space: normal; }
    .data-table td:first-child { white-space: normal; }
  }

  /* TAGS LIST */
  .vein-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 4px;
  }

  .vein-tag {
    background: rgba(239,68,68,0.1);
    border: 1px solid rgba(239,68,68,0.25);
    color: #fca5a5;
    font-size: 11.5px;
    padding: 3px 10px;
    border-radius: 6px;
    font-weight: 600;
    transition: transform 0.2s;
  }
  .vein-tag:hover { transform: scale(1.04); }

  .artery-tag {
    background: rgba(249,115,22,0.1);
    border: 1px solid rgba(249,115,22,0.25);
    color: #fdba74;
    font-size: 11.5px;
    padding: 3px 10px;
    border-radius: 6px;
    font-weight: 600;
    transition: transform 0.2s;
  }
  .artery-tag:hover { transform: scale(1.04); }

  .nerve-tag {
    background: rgba(139,92,246,0.1);
    border: 1px solid rgba(139,92,246,0.25);
    color: #c4b5fd;
    font-size: 11.5px;
    padding: 3px 10px;
    border-radius: 6px;
    font-weight: 600;
    transition: transform 0.2s;
  }
  .nerve-tag:hover { transform: scale(1.04); }

  .tube-tag {
    background: rgba(6,182,212,0.1);
    border: 1px solid rgba(6,182,212,0.25);
    color: #67e8f9;
    font-size: 11.5px;
    padding: 3px 10px;
    border-radius: 6px;
    font-weight: 600;
    transition: transform 0.2s;
  }
  .tube-tag:hover { transform: scale(1.04); }

  .lymph-tag {
    background: rgba(16,185,129,0.1);
    border: 1px solid rgba(16,185,129,0.25);
    color: #6ee7b7;
    font-size: 11.5px;
    padding: 3px 10px;
    border-radius: 6px;
    font-weight: 600;
    transition: transform 0.2s;
  }
  .lymph-tag:hover { transform: scale(1.04); }

  /* MUSCLE TABLE */
  .muscle-table { width: 100%; border-collapse: collapse; font-size: 12px; margin-top: 6px; }
  .muscle-table th {
    background: rgba(245,158,11,0.1);
    color: var(--yellow);
    font-size: 10.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 8px 10px;
    border-bottom: 1px solid rgba(245,158,11,0.2);
    text-align: left;
  }
  .muscle-table td {
    padding: 9px 10px;
    border-bottom: 1px solid var(--border);
    vertical-align: top;
    line-height: 1.55;
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
    margin-bottom: 20px;
    position: relative;
  }
  .search-input {
    width: 100%;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    color: var(--text);
    font-family: 'Cairo', sans-serif;
    font-size: 13.5px;
    padding: 11px 16px 11px 42px;
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
    font-size: 15px;
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
    font-size: 9.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 2px 7px;
    border-radius: 4px;
    vertical-align: middle;
  }
  .badge-blue { background: rgba(59,130,246,0.15); color: var(--blue); }
  .badge-yellow { background: rgba(245,158,11,0.15); color: var(--yellow); }
  .badge-red { background: rgba(239,68,68,0.15); color: var(--red); }
  .badge-green { background: rgba(16,185,129,0.15); color: var(--green); }
  .badge-purple { background: rgba(139,92,246,0.15); color: var(--purple); }

  .topic-group { margin-bottom: 30px; }

  /* ARABIC TRANSLATION BUTTON & PANEL */
  .translate-btn {
    background: rgba(16,185,129,0.1);
    border: 1px solid rgba(16,185,129,0.3);
    border-radius: 8px;
    padding: 5px 10px;
    font-size: 12.5px;
    color: var(--green);
    cursor: pointer;
    font-family: 'Cairo', sans-serif;
    font-weight: 600;
    transition: all 0.3s;
    display: flex;
    align-items: center;
    gap: 5px;
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
    padding: 0 18px;
  }
  .arabic-panel.active {
    max-height: 1200px;
    opacity: 1;
    padding: 18px;
    overflow-y: auto;
  }
  .arabic-panel-header {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid rgba(16,185,129,0.15);
  }
  .arabic-panel-icon { font-size: 18px; }
  .arabic-panel-title {
    font-size: 14.5px;
    font-weight: 800;
    color: var(--green);
    font-family: 'Cairo', sans-serif;
  }
  .arabic-panel-badge {
    background: rgba(16,185,129,0.15);
    border: 1px solid rgba(16,185,129,0.3);
    color: #6ee7b7;
    font-size: 9.5px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 20px;
    margin-right: auto;
    direction: ltr;
  }
  .arabic-panel p {
    font-size: 13px;
    color: #b8c5d4;
    line-height: 1.9;
    margin-bottom: 8px;
    font-family: 'Cairo', sans-serif;
  }
  .arabic-panel p:last-child { margin-bottom: 0; }
  .arabic-panel strong { color: #6ee7b7; font-weight: 700; }
  .arabic-panel .ar-highlight {
    background: rgba(16,185,129,0.1);
    border-right: 3px solid var(--green);
    padding: 9px 12px;
    border-radius: 0 8px 8px 0;
    margin: 8px 0;
    font-size: 12.5px;
    color: #a8b8c8;
    line-height: 1.85;
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
    height: 330px;
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
    padding: 28px;
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
    margin-bottom: 14px;
    font-weight: 700;
  }
  .flashcard-front .flashcard-label { color: var(--cyan); }
  .flashcard-back .flashcard-label { color: var(--green); }
  .flashcard-text {
    font-size: 16.5px;
    font-weight: 600;
    line-height: 1.6;
    color: var(--text);
  }
  .flashcard-back .flashcard-text { color: #6ee7b7; font-size: 14.5px; }
  .flashcard-hint {
    position: absolute;
    bottom: 14px;
    font-size: 11px;
    color: var(--dim);
  }
  .flashcard-section-tag {
    position: absolute;
    top: 14px;
    right: 14px;
    font-size: 9.5px;
    background: rgba(139,92,246,0.12);
    border: 1px solid rgba(139,92,246,0.3);
    color: var(--purple);
    padding: 3px 9px;
    border-radius: 20px;
    font-weight: 600;
  }

  .flashcard-nav {
    display: flex;
    gap: 14px;
    margin-top: 24px;
  }
  .flashcard-nav button {
    background: var(--card);
    border: 1px solid var(--border);
    color: var(--muted);
    padding: 9px 22px;
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
    width: 390px;
    max-width: 90vw;
    z-index: 251;
    background: var(--bg2);
    border-left: 1px solid var(--border);
    overflow-y: auto;
    transition: right 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    padding: 22px;
  }
  .quickref-sidebar.active { right: 0; }
  .quickref-sidebar::-webkit-scrollbar { width: 4px; }
  .quickref-sidebar::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 4px; }

  .qr-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 20px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border);
  }
  .qr-title {
    font-size: 16.5px;
    font-weight: 800;
    color: var(--text);
  }
  .qr-close {
    background: none;
    border: 1px solid var(--border);
    color: var(--muted);
    width: 30px;
    height: 30px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 15px;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.2s;
  }
  .qr-close:hover { color: var(--red); border-color: var(--red); }

  .qr-section { margin-bottom: 16px; }
  .qr-section-title {
    font-size: 10.5px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    padding: 4px 9px;
    border-radius: 6px;
    margin-bottom: 6px;
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
    gap: 5px;
    padding-left: 4px;
  }
  .qr-items li {
    font-size: 12px;
    color: var(--muted);
    line-height: 1.5;
    display: flex;
    align-items: flex-start;
    gap: 7px;
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
    padding: 26px;
    max-width: 380px;
    width: 90%;
  }
  .shortcuts-box h3 {
    font-size: 17px;
    font-weight: 800;
    color: var(--text);
    margin-bottom: 16px;
    text-align: center;
  }
  .shortcut-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 7px 0;
    border-bottom: 1px solid var(--border);
  }
  .shortcut-row:last-child { border-bottom: none; }
  .shortcut-key {
    background: var(--bg3);
    border: 1px solid var(--border2);
    color: var(--cyan);
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 5px;
  }
  .shortcut-desc { font-size: 12.5px; color: var(--muted); }

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
    body::before, body::after, .nav-wrapper, .progress-bar-container, .progress-badge,
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
    .stats-bar { gap: 16px; }
    .nav-btn { padding: 6px 10px; font-size: 11.5px; }
    .back-btn { padding: 4px 10px; font-size: 11px; top: 8px; left: 8px; }
    .progress-badge { top: 8px; right: 8px; font-size: 10px; padding: 4px 10px; }
    header { padding: 46px 12px 24px; }
    .fab-group { bottom: 16px; right: 16px; }
    .fab { width: 42px; height: 42px; font-size: 18px; }
    .sec-header { top: 48px; }
    .flashcard-scene { height: 280px; }
    .flashcard-text { font-size: 14px; }
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

<!-- === ULTRA-SLEEK NAVIGATION BAR === -->
<div class="nav-wrapper">
  <div class="nav-container">
    <button class="nav-scroll-btn" onclick="scrollNav(-200)" title="تمرير لليسار">◀</button>
    <div class="nav-scroll" id="navScroll">
      <button class="nav-btn active" onclick="showSection('gluteal', this)">
        <span class="num-badge">1</span> 🍑 Gluteal Region
      </button>
      <button class="nav-btn" onclick="showSection('femoral-triangle', this)">
        <span class="num-badge">2</span> 📐 Femoral Triangle
      </button>
      <button class="nav-btn" onclick="showSection('ant-thigh', this)">
        <span class="num-badge">3</span> 🦵 Anterior Thigh
      </button>
      <button class="nav-btn" onclick="showSection('med-thigh', this)">
        <span class="num-badge">4</span> 🧲 Medial (Adductors)
      </button>
      <button class="nav-btn" onclick="showSection('post-thigh', this)">
        <span class="num-badge">5</span> 🏃 Hamstrings & Popliteal
      </button>
      <button class="nav-btn" onclick="showSection('fem-obt-nerves', this)">
        <span class="num-badge">6</span> ⚡ Femoral & Obturator
      </button>
      <button class="nav-btn" onclick="showSection('sciatic-nerves', this)">
        <span class="num-badge">7</span> ⚡ Sciatic, Tibial & Fibular
      </button>
      <button class="nav-btn" onclick="showSection('comparisons', this)">
        <span class="num-badge">8</span> 📊 Comparisons
      </button>
      <button class="nav-btn" onclick="showSection('viva-spotting', this)">
        <span class="num-badge">9</span> 🔬 OSPE & Oral Simulator
      </button>
      <button class="nav-btn special" onclick="openFlashcards()">
        🧠 اختبر نفسك (Flashcards)
      </button>
    </div>
    <button class="nav-scroll-btn" onclick="scrollNav(200)" title="تمرير لليمين">▶</button>
  </div>
</div>

<main>

<!-- SEARCH -->
<div class="search-wrap">
  <span class="search-icon">🔍</span>
  <input class="search-input" id="searchInput" placeholder="ابحث في جميع أسئلة المقالي والعملي والأعصاب..." oninput="searchAll(this.value)">
  <div class="search-results-info" id="searchInfo">تم العثور على <span id="searchCount">0</span> نتيجة</div>
</div>
""" + get_section_1() + get_section_2() + get_section_3() + get_section_4() + get_section_5() + get_section_6() + get_section_7() + get_section_8() + get_section_9() + """
</main>

<!-- === FLASHCARD OVERLAY === -->
<div class="flashcard-overlay" id="flashcardOverlay">
  <div class="flashcard-header">
    <span class="flashcard-counter" id="flashcardCounter">1 / 30</span>
    <button class="flashcard-close" onclick="closeFlashcards()">✕</button>
  </div>

  <div class="flashcard-scene" onclick="flipCard()">
    <div class="flashcard-card" id="flashcardCard">
      <div class="flashcard-face flashcard-front">
        <span class="flashcard-section-tag" id="fcSection">Gluteal Region</span>
        <div class="flashcard-label">Question</div>
        <div class="flashcard-text" id="fcQuestion">What is the nerve supply of Gluteus Maximus?</div>
        <div class="flashcard-hint">اضغط للقلب والاطلاع على الإجابة (أو مسافة Space)</div>
      </div>
      <div class="flashcard-face flashcard-back">
        <span class="flashcard-section-tag">Model Answer</span>
        <div class="flashcard-label">Answer</div>
        <div class="flashcard-text" id="fcAnswer">Inferior Gluteal Nerve (L5, S1, S2)</div>
        <div class="flashcard-hint">استخدم الأسهم ◀ ▶ للتنقل</div>
      </div>
    </div>
  </div>

  <div class="flashcard-nav">
    <button onclick="prevCard()">◀ السابق</button>
    <button onclick="shuffleCards()">🔀 عشوائي</button>
    <button onclick="nextCard()">التالي ▶</button>
  </div>
</div>

<!-- === QUICK REF SIDEBAR === -->
<div class="quickref-overlay" id="qrOverlay" onclick="toggleQuickRef()"></div>
<div class="quickref-sidebar" id="qrSidebar">
  <div class="qr-header">
    <div class="qr-title">📌 Quick Reference — Lower Limb</div>
    <button class="qr-close" onclick="toggleQuickRef()">✕</button>
  </div>

  <div class="qr-section">
    <span class="qr-section-title purple">Nerve Roots & Innervations</span>
    <ul class="qr-items">
      <li><strong>Femoral Nerve:</strong> L2, L3, L4 (Posterior divisions)</li>
      <li><strong>Obturator Nerve:</strong> L2, L3, L4 (Anterior divisions)</li>
      <li><strong>Superior Gluteal:</strong> L4, L5, S1 (Gluteus medius/minimus)</li>
      <li><strong>Inferior Gluteal:</strong> L5, S1, S2 (Gluteus maximus)</li>
      <li><strong>Sciatic Nerve:</strong> L4, L5, S1, S2, S3 (Thickest nerve)</li>
      <li><strong>Common Fibular:</strong> L4, L5, S1, S2 (Neck of fibula)</li>
      <li><strong>Tibial Nerve:</strong> L4, L5, S1, S2, S3 (Posterior compartment)</li>
    </ul>
  </div>

  <div class="qr-section">
    <span class="qr-section-title cyan">Crucial Reflexes & Tests</span>
    <ul class="qr-items">
      <li><strong>Knee Jerk (Patellar):</strong> L3, L4 (Femoral nerve)</li>
      <li><strong>Ankle Jerk (Achilles):</strong> S1, S2 (Tibial nerve)</li>
      <li><strong>Trendelenburg Test:</strong> Superior Gluteal N. (Stance side)</li>
      <li><strong>Straight Leg Raise (SLR):</strong> Sciatic nerve root traction</li>
      <li><strong>Femoral Pulse:</strong> Mid-Inguinal Point (ASIS to Pubic Symphysis)</li>
    </ul>
  </div>

  <div class="qr-section">
    <span class="qr-section-title red">Clinical Deformities</span>
    <ul class="qr-items">
      <li><strong>Foot Drop (Equinovarus):</strong> Common Fibular N. lesion</li>
      <li><strong>Calcaneovalgus:</strong> Tibial N. lesion (loss of plantarflexion)</li>
      <li><strong>Waddling Gait:</strong> Bilateral Trendelenburg deficiency</li>
      <li><strong>Meralgia Paresthetica:</strong> Lateral Cutaneous of Thigh (L2, L3)</li>
      <li><strong>Tarsal Tunnel Syndrome:</strong> Tibial N. behind medial malleolus</li>
      <li><strong>Baker's Cyst:</strong> Semimembranosus bursa enlargement</li>
    </ul>
  </div>

  <div class="qr-section">
    <span class="qr-section-title yellow">High-Yield Mnemonics</span>
    <ul class="qr-items">
      <li><strong>NAVL (Femoral Base):</strong> Nerve, Artery, Vein, Lymphatics (lat to med)</li>
      <li><strong>SGS (Pes Anserinus):</strong> Sartorius (Femoral), Gracilis (Obturator), Semitendinosus (Sciatic)</li>
      <li><strong>PIN (GSF to LSF):</strong> Pudendal N., Int. Pudendal vessels, N. to Obturator Internus</li>
    </ul>
  </div>
</div>

<!-- === KEYBOARD SHORTCUTS MODAL === -->
<div class="shortcuts-modal" id="shortcutsModal" onclick="if(event.target===this) toggleShortcuts()">
  <div class="shortcuts-box">
    <h3>⌨️ اختصارات لوحة المفاتيح</h3>
    <div class="shortcut-row"><span class="shortcut-key">S</span><span class="shortcut-desc">البحث السريع</span></div>
    <div class="shortcut-row"><span class="shortcut-key">F</span><span class="shortcut-desc">فتح الفلاش كاردز (اختبر نفسك)</span></div>
    <div class="shortcut-row"><span class="shortcut-key">Q</span><span class="shortcut-desc">المرجع السريع جانبي</span></div>
    <div class="shortcut-row"><span class="shortcut-key">P</span><span class="shortcut-desc">طباعة أو تصدير PDF</span></div>
    <div class="shortcut-row"><span class="shortcut-key">◀ / ▶</span><span class="shortcut-desc">التنقل بين الأقسام / البطاقات</span></div>
    <div class="shortcut-row"><span class="shortcut-key">Space</span><span class="shortcut-desc">قلب البطاقة (Flip Card)</span></div>
    <div class="shortcut-row"><span class="shortcut-key">Esc</span><span class="shortcut-desc">إغلاق النوافذ المنبثقة</span></div>
  </div>
</div>

<script>
  // === SECTION NAVIGATION ===
  const sectionIds = [
    'gluteal',
    'femoral-triangle',
    'ant-thigh',
    'med-thigh',
    'post-thigh',
    'fem-obt-nerves',
    'sciatic-nerves',
    'comparisons',
    'viva-spotting'
  ];
  let currentSectionIndex = 0;

  function showSection(id, btn) {
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.nav-btn:not(.special)').forEach(b => b.classList.remove('active'));
    
    const targetSection = document.getElementById(id);
    if (targetSection) {
      targetSection.classList.add('active');
      currentSectionIndex = sectionIds.indexOf(id);
    }
    
    if (btn) {
      btn.classList.add('active');
      btn.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
    } else {
      const matchingBtn = document.querySelector(`.nav-btn[onclick*="'${id}'"]`);
      if (matchingBtn) {
        matchingBtn.classList.add('active');
        matchingBtn.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
      }
    }
    
    window.scrollTo({ top: 0, behavior: 'smooth' });
    updateProgress();
  }

  function scrollNav(amount) {
    const nav = document.getElementById('navScroll');
    if (nav) {
      nav.scrollBy({ left: amount, behavior: 'smooth' });
    }
  }

  function nextSection() {
    currentSectionIndex = (currentSectionIndex + 1) % sectionIds.length;
    showSection(sectionIds[currentSectionIndex]);
  }

  function prevSection() {
    currentSectionIndex = (currentSectionIndex - 1 + sectionIds.length) % sectionIds.length;
    showSection(sectionIds[currentSectionIndex]);
  }

  // === ESSAY QUESTION ACCORDION ===
  function toggleEssay(header) {
    const card = header.parentElement;
    card.classList.toggle('open');
  }

  // Open first 2 essay cards by default for smooth reading
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.essay-card').forEach((c, idx) => {
      if (idx < 2) c.classList.add('open');
    });
  });

  // === COMPLETION TRACKING ===
  const completedSections = JSON.parse(localStorage.getItem('anatomy2_completed') || '{}');

  function toggleComplete(sectionId, btn) {
    completedSections[sectionId] = !completedSections[sectionId];
    localStorage.setItem('anatomy2_completed', JSON.stringify(completedSections));
    updateCompletionUI(sectionId, btn);
    updateProgress();

    if (completedSections[sectionId]) {
      triggerConfetti(btn);
    }
  }

  function updateCompletionUI(sectionId, btn) {
    const isDone = !!completedSections[sectionId];
    if (btn) {
      btn.textContent = isDone ? '✓ تم المذاكرة' : '☐ تم المذاكرة';
      btn.classList.toggle('completed', isDone);
    }
  }

  function updateProgress() {
    const total = sectionIds.length;
    let completedCount = 0;
    sectionIds.forEach(id => {
      if (completedSections[id]) completedCount++;
      const btn = document.querySelector(`.sec-complete-btn[data-section="${id}"]`);
      if (btn) updateCompletionUI(id, btn);
    });

    const percent = Math.round((completedCount / total) * 100);
    document.getElementById('progressFill').style.width = percent + '%';
    document.getElementById('progressBadge').textContent = `${completedCount}/${total}`;
  }

  // === CONFETTI ANIMATION ===
  function triggerConfetti(el) {
    const container = document.createElement('div');
    container.className = 'confetti-container';
    document.body.appendChild(container);

    const colors = ['#3b82f6', '#06b6d4', '#10b981', '#f59e0b', '#8b5cf6', '#ec4899'];
    const rect = el.getBoundingClientRect();
    for (let i = 0; i < 35; i++) {
      const piece = document.createElement('div');
      piece.className = 'confetti-piece';
      piece.style.background = colors[Math.floor(Math.random() * colors.length)];
      piece.style.left = (rect.left + rect.width/2 + (Math.random()-0.5)*120) + 'px';
      piece.style.top = (rect.top) + 'px';
      piece.style.animationDuration = (1 + Math.random()) + 's';
      piece.style.animationDelay = (Math.random() * 0.3) + 's';
      container.appendChild(piece);
    }
    setTimeout(() => container.remove(), 2000);
  }

  // === SEARCH FUNCTIONALITY ===
  function searchAll(query) {
    document.querySelectorAll('mark.search-hl').forEach(m => {
      const parent = m.parentNode;
      parent.replaceChild(document.createTextNode(m.textContent), m);
      parent.normalize();
    });

    const info = document.getElementById('searchInfo');
    if (!query || query.length < 2) {
      info.style.display = 'none';
      return;
    }

    let totalMatches = 0;
    let firstMatchSection = null;

    sectionIds.forEach(id => {
      const section = document.getElementById(id);
      const walker = document.createTreeWalker(section, NodeFilter.SHOW_TEXT, null, false);
      const nodes = [];
      while (walker.nextNode()) nodes.push(walker.currentNode);

      nodes.forEach(node => {
        const text = node.textContent;
        const lowerText = text.toLowerCase();
        const lowerQuery = query.toLowerCase();
        const idx = lowerText.indexOf(lowerQuery);
        if (idx >= 0) {
          totalMatches++;
          if (!firstMatchSection) firstMatchSection = id;
          const before = text.substring(0, idx);
          const match = text.substring(idx, idx + query.length);
          const after = text.substring(idx + query.length);
          const mark = document.createElement('mark');
          mark.className = 'search-hl';
          mark.textContent = match;
          const parent = node.parentNode;
          parent.insertBefore(document.createTextNode(before), node);
          parent.insertBefore(mark, node);
          parent.insertBefore(document.createTextNode(after), node);
          parent.removeChild(node);
        }
      });
    });

    document.getElementById('searchCount').textContent = totalMatches;
    info.style.display = totalMatches > 0 ? 'block' : 'none';

    if (firstMatchSection && firstMatchSection !== sectionIds[currentSectionIndex]) {
      showSection(firstMatchSection);
    }

    document.querySelectorAll('.section.active mark.search-hl').forEach(m => {
      const essayCard = m.closest('.essay-card');
      if (essayCard) essayCard.classList.add('open');
    });

    const firstMark = document.querySelector('.section.active mark.search-hl');
    if (firstMark) {
      setTimeout(() => firstMark.scrollIntoView({ behavior: 'smooth', block: 'center' }), 200);
    }
  }

  // === FLASHCARDS DECK (30 CARDS) ===
  const flashcards = [
    { q: "What is the nerve supply of Gluteus Maximus?", a: "Inferior Gluteal Nerve (L5, S1, S2)", s: "Gluteal Region" },
    { q: "What is the nerve supply of Gluteus Medius & Minimus?", a: "Superior Gluteal Nerve (L4, L5, S1)", s: "Gluteal Region" },
    { q: "What causes a Positive Trendelenburg Sign?", a: "Superior Gluteal Nerve injury or Gluteus Medius paralysis on the STANCE side (pelvis drops on unsupported swing side)", s: "Gluteal Region" },
    { q: "Where is the ONLY safe quadrant for IM injection in the buttock?", a: "Upper Outer (Anterosuperior) Quadrant — avoids the Sciatic Nerve!", s: "Gluteal Region" },
    { q: "Name the structures passing ABOVE the Piriformis muscle", a: "Superior Gluteal Nerve, Superior Gluteal Artery, Superior Gluteal Vein", s: "Gluteal Region" },
    { q: "Name the structures passing through BOTH Greater and Lesser Sciatic Foramina (PIN)", a: "Pudendal nerve, Internal pudendal vessels, Nerve to obturator internus", s: "Gluteal Region" },
    { q: "What forms the boundaries of the Femoral Ring?", a: "Anterior: Inguinal ligament; Posterior: Pectineus & Pectineal ligament; Medial: Lacunar ligament; Lateral: Femoral vein", s: "Femoral Triangle" },
    { q: "What are the contents of the Femoral Canal?", a: "Fat, lymphatic vessels, and Deep Inguinal Lymph Node of Cloquet (Rosenmüller)", s: "Femoral Triangle" },
    { q: "Why is Femoral Hernia more prone to strangulation than Inguinal Hernia?", a: "Rigid unyielding boundaries (especially sharp edge of Lacunar Ligament) and narrow neck (1.25 cm)", s: "Femoral Triangle" },
    { q: "Is the Femoral Nerve INSIDE or OUTSIDE the Femoral Sheath?", a: "OUTSIDE (lies laterally in the groove between Psoas and Iliacus)", s: "Femoral Triangle" },
    { q: "What are the boundaries of the Femoral Triangle?", a: "Superior: Inguinal ligament; Lateral: Medial border of Sartorius; Medial: Medial border of Adductor longus", s: "Femoral Triangle" },
    { q: "What is the chief powerful extensor of the knee joint?", a: "Quadriceps Femoris (supplied by Femoral Nerve L2, L3, L4)", s: "Anterior Thigh" },
    { q: "What are the 3 muscles of Pes Anserinus and their nerves?", a: "Sartorius (Femoral), Gracilis (Obturator), Semitendinosus (Sciatic/Tibial) — SGS", s: "Medial Thigh" },
    { q: "Why is Adductor Magnus a composite / hybrid muscle?", a: "Dual nerve supply: Adductor part by Obturator Nerve (L2-L4); Hamstring part by Tibial part of Sciatic Nerve (L4)", s: "Medial Thigh" },
    { q: "What passes through the Adductor Hiatus?", a: "Femoral Artery and Vein (changing into Popliteal Artery and Vein in popliteal fossa)", s: "Medial Thigh" },
    { q: "What are the 4 criteria for a true hamstring muscle?", a: "1. Origin from ischial tuberosity, 2. Insertion into leg bones, 3. Crosses 2 joints, 4. Innervated by Tibial nerve", s: "Posterior Thigh" },
    { q: "Why is the Short Head of Biceps Femoris NOT a true hamstring?", a: "Arises from linea aspera, crosses only knee, innervated by Common Fibular (Peroneal) nerve", s: "Posterior Thigh" },
    { q: "Which muscle unlocks the locked knee joint?", a: "Popliteus muscle (laterally rotates femur on fixed tibia at initiation of flexion)", s: "Popliteal Fossa" },
    { q: "List the contents of Popliteal Fossa from superficial to deep", a: "Tibial Nerve → Common Fibular Nerve → Popliteal Vein → Popliteal Artery", s: "Popliteal Fossa" },
    { q: "What is the nerve root value of the Femoral Nerve?", a: "L2, L3, L4 (Posterior divisions of anterior rami of lumbar plexus)", s: "Nerves" },
    { q: "What is the longest cutaneous nerve in the human body?", a: "Saphenous Nerve (branch of posterior division of Femoral Nerve)", s: "Nerves" },
    { q: "What sensory deficit occurs in Deep Fibular Nerve injury?", a: "Loss of sensation in the 1st Interdigital Web Space ONLY (between great toe and 2nd toe)", s: "Nerves" },
    { q: "What is the deformity and gait caused by Common Fibular Nerve injury?", a: "Foot Drop (Equinovarus deformity) with High-Stepping (Cock-Walk) Gait", s: "Nerves" },
    { q: "Why is the Common Fibular Nerve easily injured?", a: "Directly winds around the subcutaneous hard neck of the fibula", s: "Nerves" },
    { q: "What is the deformity caused by Tibial Nerve injury?", a: "Calcaneovalgus deformity (loss of plantarflexion, inability to stand on tiptoes)", s: "Nerves" },
    { q: "What is Tarsal Tunnel Syndrome?", a: "Compression of the Tibial Nerve beneath the flexor retinaculum behind the medial malleolus", s: "Nerves" },
    { q: "What is Meralgia Paresthetica?", a: "Entrapment of the Lateral Cutaneous Nerve of Thigh (L2, L3) under the lateral inguinal ligament (burning outer thigh pain)", s: "Nerves" },
    { q: "What is Hilton's Law?", a: "The nerve supplying a joint also supplies the muscles moving that joint and the skin over their insertions", s: "Nerves" },
    { q: "What is the spinal segment tested by Knee Jerk vs Ankle Jerk?", a: "Knee Jerk = L3, L4 (Femoral N.); Ankle Jerk = S1, S2 (Tibial N.)", s: "Nerves" },
    { q: "Where is the Femoral Pulse palpated?", a: "At the Mid-Inguinal Point (midway between ASIS and Pubic Symphysis)", s: "Practical" }
  ];

  let currentCard = 0;
  let cardOrder = [...Array(flashcards.length).keys()];

  function openFlashcards() {
    document.getElementById('flashcardOverlay').classList.add('active');
    currentCard = 0;
    updateFlashcard();
  }

  function closeFlashcards() {
    document.getElementById('flashcardOverlay').classList.remove('active');
    document.getElementById('flashcardCard').classList.remove('flipped');
  }

  function flipCard() {
    document.getElementById('flashcardCard').classList.toggle('flipped');
  }

  function nextCard() {
    document.getElementById('flashcardCard').classList.remove('flipped');
    setTimeout(() => {
      currentCard = (currentCard + 1) % cardOrder.length;
      updateFlashcard();
    }, 150);
  }

  function prevCard() {
    document.getElementById('flashcardCard').classList.remove('flipped');
    setTimeout(() => {
      currentCard = (currentCard - 1 + cardOrder.length) % cardOrder.length;
      updateFlashcard();
    }, 150);
  }

  function shuffleCards() {
    for (let i = cardOrder.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [cardOrder[i], cardOrder[j]] = [cardOrder[j], cardOrder[i]];
    }
    currentCard = 0;
    document.getElementById('flashcardCard').classList.remove('flipped');
    setTimeout(updateFlashcard, 150);
  }

  function updateFlashcard() {
    const fc = flashcards[cardOrder[currentCard]];
    document.getElementById('fcQuestion').textContent = fc.q;
    document.getElementById('fcAnswer').textContent = fc.a;
    document.getElementById('fcSection').textContent = fc.s;
    document.getElementById('flashcardCounter').textContent = (currentCard + 1) + ' / ' + cardOrder.length;
  }

  // === QUICK REF & SHORTCUTS ===
  function toggleQuickRef() {
    document.getElementById('qrOverlay').classList.toggle('active');
    document.getElementById('qrSidebar').classList.toggle('active');
  }

  function toggleShortcuts() {
    document.getElementById('shortcutsModal').classList.toggle('active');
  }

  // === ARABIC TRANSLATION TOGGLE ===
  function toggleTranslation(sectionId, btn) {
    const panel = document.getElementById('arabic-' + sectionId);
    if (!panel) return;
    const isActive = panel.classList.contains('active');
    
    document.querySelectorAll('.arabic-panel.active').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.translate-btn.active').forEach(b => b.classList.remove('active'));
    
    if (!isActive) {
      panel.classList.add('active');
      btn.classList.add('active');
      setTimeout(() => panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' }), 100);
    }
  }

  // === KEYBOARD SHORTCUTS ===
  document.addEventListener('keydown', function(e) {
    if (e.target.tagName === 'INPUT') return;

    const flashcardOpen = document.getElementById('flashcardOverlay').classList.contains('active');

    if (e.key === 'Escape') {
      closeFlashcards();
      document.getElementById('qrOverlay').classList.remove('active');
      document.getElementById('qrSidebar').classList.remove('active');
      document.getElementById('shortcutsModal').classList.remove('active');
      return;
    }

    if (flashcardOpen) {
      if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') nextCard();
      else if (e.key === 'ArrowRight' || e.key === 'ArrowUp') prevCard();
      else if (e.key === ' ') { e.preventDefault(); flipCard(); }
      return;
    }

    if (e.key === 'ArrowLeft') nextSection();
    else if (e.key === 'ArrowRight') prevSection();
    else if (e.key.toLowerCase() === 's') { e.preventDefault(); document.getElementById('searchInput').focus(); }
    else if (e.key.toLowerCase() === 'f') { e.preventDefault(); openFlashcards(); }
    else if (e.key.toLowerCase() === 'q') { e.preventDefault(); toggleQuickRef(); }
    else if (e.key.toLowerCase() === 'k') { e.preventDefault(); toggleShortcuts(); }
    else if (e.key.toLowerCase() === 'p') { e.preventDefault(); window.print(); }
  });

  // Init Progress
  updateProgress();

  window.addEventListener('pageshow', function(event) {
    if (event.persisted || (window.performance && window.performance.navigation && window.performance.navigation.type === 2)) {
      window.location.reload();
    }
  });

  if ('caches' in window) {
    caches.keys().then(function(names) {
      for (let name of names) caches.delete(name);
    });
  }
</script>

</body>
</html>
"""

html_content = build_full_html()

with open(r"d:\Coding\PT12\final\anatomy2.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open(r"d:\Coding\PT12\final\anatomy2_lower_limb.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Saved updated files successfully!")
